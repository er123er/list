import os
import random
import time
import re
import requests
import ddddocr


def pan(rs):
	if rs.isdigit() == True:
		return rs.isdigit()


def ja(a, d):
	return int(a) + int(d)


def tuxing():
	while True:
		url = 'http://www.400cx.com/platform/loginstickyImg?math=true'
		ocr = ddddocr.DdddOcr(old=True)
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
		}
		tu = requests.get(url=url, headers=headers)
		with open('x.png', 'wb') as f:
			f.write(tu.content)
		with open("x.png", 'rb') as f:
			image = f.read()
		res = ocr.classification(image)
		
		p = list(res)
		sb = list(filter(pan, p))
		if len(sb) == 2:
			os.remove('x.png')
			return tu.cookies, ja(sb[0], sb[1])
		else:
			print(f'不对重新获取{res}')
			time.sleep(random.randint(1, 3))


cook, y = tuxing()

headers = {
	'Host': 'www.400cx.com',
	'Origin': 'http://www.400cx.com',
	'Referer': 'http://www.400cx.com/platform/login.jsp',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
}
zh = input('账号:')
ma = input('密码:')
url = 'http://www.400cx.com/platform/login.do'
data = {
	'dtoUserName': zh,
	'password': ma,
	'dtoUserCode': y
}
time.sleep(random.randint(1, 3))
html = requests.post(url=url, headers=headers, data=data, cookies=cook)
# print(html.text)
header = {
	'Host': 'www.400cx.com',
	# 'Referer': 'http://www.400cx.com/platform/call/main.do',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
}
da = {
	'currentPage': '1',
	'numPerPage': '100',
	'recordCacheGet': 'true',
	'startTime': '',
	'endTime': '',
	'selOption': 'all',
	'keyWords': '',
}
time.sleep(random.randint(1, 3))
xia = 'http://www.400cx.com/platform/call/receivedCallList.do'
htmld = requests.post(url=xia, headers=header, data=da, cookies=cook)
tq = re.compile(
	'<a href="javascript:downRecord\(\'(.*?).*?(.*?)\'.*?\'(.*?)\'.*?\'(.*?)\'.*?\'(.*?)\'.*?\'(.*?)\'.*?\'(.*?)\'\)">下载</a>',
	re.S)
for i in tq.findall(htmld.text):
	bb = {
		'id': list(i)[1],
		'startTime': list(i)[2],
		'callerNo': list(i)[3],
		'begin': list(i)[4],
		'end': list(i)[5],
		'durationTime': list(i)[6],
	}
	vjk = 'http://www.400cx.com/platform/call/downlistenRecordUrl.do?'
	html_p = requests.get(url=vjk, params=bb, headers=header, cookies=cook)
	#print(html_p.json())
	mp3_url = html_p.json()["message"]
	html_mp3 = requests.get(url=mp3_url, headers=header, cookies=cook)
	if not os.path.exists('mp3'):
		os.makedirs('mp3')
	path = 'mp3//' + list(i)[2] + '---' + list(i)[3] + '.mp3'
	with open(path, 'wb') as f:
		f.write(html_mp3.content)
	time.sleep(1)
