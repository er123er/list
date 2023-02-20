import time
from prettytable import PrettyTable

import requests

email = 'feikevipxyf@qq.com'
url = 'https://www.tuia.cn/account/login'
data = {
	'email': email,
	'password': 'feike123',
	'remember': 'true',
	'validations': 'true',
}
ua = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
}
html = requests.post(url=url, data=data, headers=ua)
cook = html.cookies


# 推广数据
def promote():
	k = 'https://www.tuia.cn/advert/queryAdvertData?'
	params = {
		'name': '',
		'email': '',
		'companyName': '',
		'type': '2',
		'startDate': '2022-01-01',
		'endDate': '2022-08-31',
		'currentPage': '1',
		'pageSize': '50',
	}
	html_k = requests.get(url=k, headers=ua, cookies=cook, params=params)
	len_ = len(html_k.json()['data']['list'])
	print('推广数据')
	table = PrettyTable(['推广计划名称', '客户公司名称', '时间', '曝光量(次)', '点击(次)', '点击率', '访问PV', '转化PV'])
	for i in range(len_):
		table.add_row([html_k.json()['data']['list'][i]['name'], html_k.json()['data']['list'][i]['companyName'],
		               html_k.json()['data']['list'][i]['time'], html_k.json()['data']['list'][i]['exposureCount'],
		               html_k.json()['data']['list'][i]['clickCount'],
		               str(html_k.json()['data']['list'][i]['clickRate'])+'%', html_k.json()['data']['list'][i]['visitPv'],
		               html_k.json()['data']['list'][i]['effectPv']])
	# html_k.json()['data'][i]['consumeTotalDecimal']
	print(table)


# 后端数据回传

def hd():
	url = 'https://www.tuia.cn/dataBack/queryData?'
	params = {
		'startDate': '2022-01-01',
		'endDate': '2022-08-31',
		'currentPage': '1',
		'pageSize': '15',
		'id': '22215',
		'advertPlanId': '22215',
	}
	html_k = requests.get(url=url, headers=ua, cookies=cook, params=params)
	len_ = len(html_k.json()['data']['list'])
	print('后端数据回传')
	table = PrettyTable(['日期', '推广计划名称', '链接名称', '落地页链接', '总消耗', '点击（次）', '点击率', '考核指标'])
	for i in range(len_):
		table.add_row([html_k.json()['data']['list'][i]['curDate'], html_k.json()['data']['list'][i]['advertName'],
		               html_k.json()['data']['list'][i]['name'], html_k.json()['data']['list'][i]['promoteUrl'],
		               html_k.json()['data']['list'][i]['consumeTotal'],
		               html_k.json()['data']['list'][i]['efClickPv'],
		               str(html_k.json()['data']['list'][i]['efClickRadio']) + '%',
		               html_k.json()['data']['list'][i]['defaultAssessmentIndex']])
	# html_k.json()['data'][i]['consumeTotalDecimal']
	print(table)


# 测试链接数据
def lj():
	url = 'https://www.tuia.cn/promote_test/advert_promote_data?'
	params = {
		'startDate': '2022-01-01',
		'endDate': '2022-08-31',
		'advertId': '22215',
		'advertPlanId': '22215',
	}
	html_k = requests.get(url=url, headers=ua, cookies=cook, params=params)
	len_ = len(html_k.json()['data'])
	print('测试链接数据')
	table = PrettyTable(['名称', '落地页地址', '发券量', '点击（次）', '点击率', '访问PV', '转化PV', '点击均价', '总消耗'])
	for i in range(len_):
		table.add_row([html_k.json()['data'][i]['name'], html_k.json()['data'][i]['promoteUrl'],
		               html_k.json()['data'][i]['coupons'], html_k.json()['data'][i]['efClickPv'],
		               html_k.json()['data'][i]['efClickRadio'], html_k.json()['data'][i]['promoteVisitPv'],
		               html_k.json()['data'][i]['efPv'], html_k.json()['data'][i]['consumeAvg'],
		               html_k.json()['data'][i]['consumeTotalDecimal']])
	# html_k.json()['data'][i]['consumeTotalDecimal']
	print(table)


if __name__ == '__main__':
	promote()
	time.sleep(3)
	hd()
	time.sleep(3)
	lj()
