import requests
from bs4 import BeautifulSoup
from slacker import Slacker
import texttable


def split_tag_by_br(tag):
    return [BeautifulSoup(_, 'html.parser').get_text(strip=True) for _ in str(tag).split('<br/>')]


TOKEN = "xoxb-3634858928-1333358269123-YtJxVWYGvsVvIiaBVn3QP6M9"

url = 'https://search.naver.com/search.naver?query=공휴일'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

tbody = soup.select_one('#dss_free_uio_cont1 > div > div > table > tbody')

table = texttable.Texttable()
table.set_deco(table.HEADER)
table.set_cols_dtype(['t', 't', 't'])

table_list = [['명칭', '날짜', '요일']]
left = []
right = []
for tr in tbody.select('tr'):
    tds = tr.select('td')
    if len(tds) >= 3:
        is_multiple = len(tds[0].select('br')) != 0
        if is_multiple:
            names = split_tag_by_br(tds[0])
            dates = split_tag_by_br(tds[1])
            dows = split_tag_by_br(tds[2])
            for i in range(len(names)):
                left.append([names[i], dates[i], dows[i]])
        else:
            left.append([tds[0].get_text(strip=True), tds[1].get_text(strip=True), tds[2].get_text(strip=True)])
    if len(tds) >= 6:
        if tds[3].get_text(strip=True) != '':
            is_multiple = len(tds[3].select('br')) != 0
            if is_multiple:
                names = split_tag_by_br(tds[3])
                dates = split_tag_by_br(tds[4])
                dows = split_tag_by_br(tds[5])
                for i in range(len(names)):
                    right.append([names[i], dates[i], dows[i]])
            else:
                right.append([tds[3].get_text(strip=True), tds[4].get_text(strip=True), tds[5].get_text(strip=True)])
table_list += left + right
table.add_rows(table_list)
table.set_header_align(['l', 'l', 'l'])
table.set_cols_align(['l', 'l', 'l'])

slacker = Slacker(TOKEN)
slacker.chat.post_message('#auto_algosignal', "```\n%s\n```" % (table.draw()))
