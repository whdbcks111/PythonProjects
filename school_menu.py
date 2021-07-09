import requests
from bs4 import BeautifulSoup


def getMenu(school_name):
    result = {}
    web_content = requests.get('https://search.naver.com/search.naver?query=' + school_name + ' 급식')
    bs = BeautifulSoup(web_content.content, 'html.parser')
    if len(bs.select('li.menu_info')) == 0:
        return None
    for tag in bs.select('li.menu_info'):
        date = ' '.join(tag.select('strong')[0].string.split()[0:2])
        month = date.split('월')[0]
        day = date.split(' ')[1].split('일')[0]
        menu_type = tag.select('strong')[0].string.split('[')[1].split(']')[0]
        menu_list = list(map(lambda x: x.string, tag.select('ul>li')))
        if not month + '.' + day in result.keys():
            result[month + '.' + day] = {}
        result[month + '.' + day][menu_type] = menu_list

    return result
