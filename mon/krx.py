from time import time
import requests
import ast
from datetime import datetime
import texttable
from slacker import Slacker

# http://open.krx.co.kr/contents/MKD/01/0110/01100305/MKD01100305.jsp 해당 사이트 까서 만들었음
TOKEN = "xoxb-3634858928-1333358269123-YtJxVWYGvsVvIiaBVn3QP6M9"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

otp_url = 'http://open.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=/MKD/01/0110/01100305/mkd01100305_01&name=form&_=1654218920715'
otp = requests.get(otp_url,
                   params={'bld': '/MKD/01/0110/01100305/mkd01100305_01', 'name': 'form', '_': round(time() * 1000)},
                   headers=headers).text

holiday_url = 'http://open.krx.co.kr/contents/OPN/99/OPN99000001.jspx'
holiday_resp = requests.post(holiday_url, data={'search_bas_yy': datetime.now().year, 'gridTp': 'KRX',
                                                'pagePath': '/contents/MKD/01/0110/01100305/MKD01100305.jsp',
                                                'code': otp},
                             headers=headers)
holiday = ast.literal_eval(holiday_resp.content.decode('utf-8'))['block1']

table = texttable.Texttable()
table.set_deco(table.HEADER)
table.set_cols_dtype(['t', 't', 't'])

table_list = [['일자', '요일', '명칭']]
today = datetime.now()
today = datetime(today.year, today.month, today.day)
for d in holiday:
    dt = datetime.strptime(d['calnd_dd'].strip(), '%Y-%m-%d')
    if dt >= today:
        table_list.append([d['calnd_dd'].strip(), d['kr_dy_tp'].strip(), d['holdy_nm'].strip()])
table.add_rows(table_list)

slacker = Slacker(TOKEN)
slacker.chat.post_message('#auto_algosignal', "```\n%s\n```" % (table.draw()))
