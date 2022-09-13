import numpy as np
import pandas as pd
import math
from datetime import datetime
import openpyxl 

issue_date = np.datetime64("2018-07-27", "D")  # 발행일
measurement_date = np.datetime64("2019-12-24", "D")  # 평가일
maturity_date = np.datetime64("2020-07-26", "D")  # 만기일
maturity_as_year = (maturity_date - measurement_date).astype(np.float64) / 365
node_count = int((maturity_date - measurement_date).astype(np.float64))
dt = 1  # 연환산 dt.

risk_free_rate = 0.0161
current_price = 43119
dividend_rate = 0.0
peer_volatility = 0.1947

u = math.exp(peer_volatility * math.sqrt(dt))
d = 1 / u
p = (math.exp((risk_free_rate - dividend_rate) * dt) - d) / (u - d)
q = 1 - p

par_value = 40000
bond_conversion_price = 40000
yield_to_maturity = 0.0843
guaranteed_rate = 0.08
coupon_rate = 0.05
ipo_refixing_ratio = 0.7
ipo_refixing_method= "공모가액"
ipo_refixing_date = np.datetime64("2021-01-01", "D")

performance_refixing_date = np.datetime64("2021-04-01", "D")
performance_refixing_conversion_price = 44057

outstanding_shares = 750000
conversion_shares = 250000

conversion_date = np.datetime64("2019-07-27", "D")
conversion_cycle = 1
redemption_date = np.datetime64("2021-07-27", "D")
redemption_cycle = 1


# 주어진 평가일 및 만기일 node 개수를 가지고 date_array 생성
def get_date_array(
    start_date, end_date, node_count
):
    days = (end_date - start_date).astype(np.int64)
    days_list = np.around(np.linspace(start=0, stop=int(days), num=int(node_count) + 1), 0)
    date_array = (np.timedelta64(1, "D") * days_list + np.datetime64(start_date)).reshape(1, int(node_count) + 1).astype("datetime64[D]")
    return date_array



# 주가 이항모형 matrix 생성
def get_binomial_tree(node_count, u, d, s):
    column = np.arange(node_count + 1).reshape(1, node_count + 1)

    row = np.arange(node_count + 1).reshape(node_count + 1, 1)

    matrix = -(row - column)
    print(matrix)
    upside_binomial_tree = np.triu(matrix)
    print(upside_binomial_tree)
    downside_binomial_tree = np.triu(column - upside_binomial_tree)
    print(downside_binomial_tree)
    x = np.power(u, upside_binomial_tree)
    y = np.power(d, downside_binomial_tree)
    stock_binomial_tree = s * (np.power(u, upside_binomial_tree) * np.power(d, downside_binomial_tree))
    return stock_binomial_tree * np.triu(np.ones(node_count + 1))

b = get_binomial_tree(node_count, u, d, current_price)

# 시점별 부채 array 생성
def get_bond_price_array(date_array, issue_date, coupon_rate, guaranteed_rate, par_value):
    issue_date = np.datetime64(issue_date, "D")
    bond_prce_array = par_value  * np.power(1 + guaranteed_rate, ((date_array - issue_date).astype(np.float64) / 365))
    return bond_prce_array

# 시점별 전환우선주 사채요소 array 생성
def get_debt_portion_array(date_array, bond_price_array, yield_to_maturity):
    maturity_date = date_array[0][-1]
    discount_factor_array = np.power(1 + yield_to_maturity, ((maturity_date - date_array).astype(np.float64) / 365))
    bond_price_at_maturuty = bond_price_array[0][-1]
    return bond_price_at_maturuty / discount_factor_array 


# 전환 및 상환 가능여부에 대한 flag matrix 생성
def effective_date_matrix(date_array, base_date):
    row = np.zeros((node_count + 1, 1))
    effective_date_matrix = row + (date_array >= base_date)
    return np.triu(effective_date_matrix)

# ipo 리픽싱 관련 주식 비율 matrix 생성
def get_ipo_price_refixing_matrix(stock_binomial_tree, date_array, conversion_price, refixing_ratio, refixing_method, refixing_date):
    adjusted_conversion_price = 0
    if refixing_method == "전환가액":
        adjusted_conversion_price = conversion_price * refixing_ratio
    else:
        adjusted_conversion_price = conversion_price / refixing_ratio

    refixing_effective_date_matrix = effective_date_matrix(date_array, refixing_date)
    refixing_conversion_ratio_tree = np.where(stock_binomial_tree <= adjusted_conversion_price, conversion_price / (stock_binomial_tree * refixing_ratio), 1)
    ipo_price_refixing_matrix = np.where(stock_binomial_tree > 0, refixing_conversion_ratio_tree * refixing_effective_date_matrix, 0)
    
    return ipo_price_refixing_matrix

# 실적 리픽싱 관련 주식 비율 matrix 생성
def get_performance_price_refixing_matrix(stock_binomial_tree, date_array, performance_refixing_conversion_price, refixing_date):
    refixing_effective_date_matrix = effective_date_matrix(date_array,refixing_date)
    performance_price_refixing_matrix = np.zeros(stock_binomial_tree.shape)
    performance_price_refixing_matrix.fill(performance_refixing_conversion_price)
    refixing_conversion_ratio_tree = np.where(stock_binomial_tree <= performance_refixing_conversion_price, (performance_price_refixing_matrix / stock_binomial_tree)  , 1)
    performance_price_refixing_matrix = np.where(refixing_effective_date_matrix > 0 , refixing_conversion_ratio_tree, 0)
    return performance_price_refixing_matrix

# 전환 및 상환 가능여부에 대한 flag array 생성
def get_cycle_flag_array(date_array, base_date, cycle, dt):
    node_count = date_array.shape[-1]
    flag_array = np.zeros(node_count)
    measurement_date = date_array[0][0] # 평가일
    base_index = date_array.shape[-1]
    base_date = measurement_date if measurement_date > base_date else base_date # 평가일과 basedate 중 더 최신날짜 기준일잡기
    
    cycle_base_date = date_array[0][-1]
    cycle_dt = conversion_cycle / 12 / dt
    cycle_index = 0

    while base_date < cycle_base_date:
        index = int(round(base_index - cycle_index, 0))
        flag_array[index - 1] = 1
        cycle_index = cycle_index + cycle_dt 
        cycle_base_date = date_array[0][index - 1]
    return flag_array.reshape(1, node_count)

# 희석효과 matrix 생성
def get_dilution_effect_matrix(stock_binomial_tree, debt_portion_array, conversion_ratio_matrix, outstanding_shares, conversion_shares):
    issued_shares = conversion_ratio_matrix * conversion_shares + outstanding_shares
    market_cap = (outstanding_shares * stock_binomial_tree + conversion_shares * debt_portion_array)
    dilution_effect_matrix = np.where(stock_binomial_tree > 0, market_cap / issued_shares / stock_binomial_tree, 0)
    return dilution_effect_matrix

# 시점별 RCPS 내재가치 matrix 생성
def get_RCPS_value_matrix(stock_binomial_tree, conversion_ratio_matrix, dilution_effect_matrix, debt_portion_array, bond_price_array ,conversion_flag_array, redemption_flag_array):
    conversion_value_matrix = stock_binomial_tree * conversion_ratio_matrix * dilution_effect_matrix * conversion_flag_array
    redemption_value_matrix = np.tile(debt_portion_array * redemption_flag_array, debt_portion_array.shape[::-1])
    bond_value_matrix = np.tile(bond_price_array, bond_price_array.shape[::-1]) 
    RCPS_value_matrix = np.maximum.reduce((conversion_value_matrix, redemption_value_matrix, bond_value_matrix))
    return np.triu(RCPS_value_matrix)



# 전환, 상환, 보유를 판단한 최종 RCPS matrix 및 할인율 matrix 생성 
def get_option_value_matrix(RCPS_value_matrix, stock_binomial_tree, debt_portion_array, bond_price_array, risk_free_rate, yield_to_maturity, date_array, dt, p, q):
    target_shape = RCPS_value_matrix.shape
    discount_rate_matrix = np.zeros(target_shape)
    option_value_matrix = np.zeros(target_shape)
    option_values = RCPS_value_matrix[:,-1]
    redemption_cases = option_values == bond_price_array[:, -1]
    discount_values = np.where(redemption_cases == True,  yield_to_maturity, risk_free_rate)
    discount_rate_matrix[:,-1] = discount_values
    option_value_matrix[:, -1] = option_values
    
    
    
    # 
    """
        마지막 열의 전부터 첫번째 열까지 반복문
        1. t + 1 시점의 할인율정보와 RCPS가치를 이용하여 t 시점의 RCPS가치를 구한다. (get_option_values_at_t)
        2. t 시점의 RCPS 가치와 내채 RCPS가치를 비교하여 적정한 할인율을 구해서 t 시점의 할인율정보를 업데이트한다. 
    """

    for i in range(1, target_shape[1]):
        
        print(i)
        
        discount_values_at_t1 = discount_rate_matrix[:, -i]        
        option_values_at_t1 = option_value_matrix[: , -i]

        option_values = get_option_values_at_t(option_values_at_t1, discount_values_at_t1,  dt, p, q)
        option_values = np.where(option_values < RCPS_value_matrix[:, -i -1], RCPS_value_matrix[:, -i -1], option_values)
        
        
        print(option_values)
        # option_values와 같은 크기의 ndarray를 초기화
        discount_values = np.zeros(option_values.shape)
        redemption_cases = np.logical_or(option_values == bond_price_array[:, -i - 1], option_values == debt_portion_array[:, -i - 1])
        
        # True인 경우, 상환 
        # False인 경우, 그 외 전부 risk_free_rate로 초기화
        discount_values = np.where(redemption_cases == True, yield_to_maturity, risk_free_rate)

        holding_cases_indices = np.where(option_values > RCPS_value_matrix[:, -i - 1])
        discount_values_at_t1 = update_holding_cases(discount_values, discount_values_at_t1, holding_cases_indices, p, q)
        # t+1 시점의 가중평균이 필요한 경우만 따로업데이트
        
        stock_binomial_values_at_t = stock_binomial_tree[:, -i - 1]
        
        
        discount_rate_matrix[:, -i - 1] = np.where(stock_binomial_values_at_t > 0, discount_values, 0)
        option_value_matrix[: , -i - 1] = np.where(stock_binomial_values_at_t > 0, option_values, 0)
        
        
    
    return (option_value_matrix, discount_rate_matrix)


def get_option_values_at_t(option_values_at_t1, discount_values_at_t1,  dt, p, q):
    option_values_at_t = np.zeros(option_values_at_t1.shape)
    
    for i in range(len(option_values_at_t) - 1):
        
        option_values_at_t[i] = (option_values_at_t1[i] * np.exp(-discount_values_at_t1[i] * dt) * p) + (option_values_at_t1[i+1] * np.exp(-discount_values_at_t1[i+1] * dt) * q)
        
                                                                                                        
    return option_values_at_t

def update_holding_cases(discount_values, discount_values_at_t1, indices, p, q):
    for i in indices:
        discount_values[i] = discount_values_at_t1[i] * p + discount_values_at_t1[i + 1] * q
            
    return discount_values

from openpyxl import Workbook
#with pd.ExcelWriter('output.xlsx', mode='a') as writer:  
#    numpy_to_dataframe(writer, stock_binomial_tree, "stock_binomial_tree")
#    numpy_to_dataframe(writer, date_array, "date_array")
#    numpy_to_dataframe(writer, ipo_refixing_conversion_ratio_matrix, "ipo_refixing_conversion_ratio_matrix")
#    numpy_to_dataframe(writer, performance_refixing_conversion_ratio_matrix, "performance_refixing_conversion_ratio_matrix")
#    numpy_to_dataframe(writer, conversion_ratio_matrix, "conversion_ratio_matrix")
#    numpy_to_dataframe(writer, bond_price_array, "bond_price_array")
#    numpy_to_dataframe(writer, debt_portion_array, "debt_portion_array")
#    numpy_to_dataframe(writer, conversion_flag_array, "conversion_flag_array")
#    numpy_to_dataframe(writer, redemption_flag_array, "redemption_flag_array")
#    numpy_to_dataframe(writer, dilution_effect_matrix, "dilution_effect_matrix")
#    numpy_to_dataframe(writer, option_value_matrix, "option_value_matrix")
#    numpy_to_dataframe(writer, RCPS_value_matrix, "RCPS_value_matrix")
#    numpy_to_dataframe(writer, discount_rate_matrix, "discount_rate_matrix")