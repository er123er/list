import re
import os
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import parsel
import requests

fg = 'https://www.1ppt.com/'
if not os.path.exists('第一ppt'):
	os.makedirs('第一ppt')

zhu_url = {}


def zhuye():
	url = 'https://www.1ppt.com/'
	he = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
	}
	html = requests.get(url=url, headers=he)
	html.encoding = html.apparent_encoding
	# print(html.text)
	# ('/html/body/div[5]/div/ul/li')
	t = re.findall('<div class="col_nav i_nav clearfix">(.*?)</div>', html.text, re.S)
	# print(t)
	html_url = re.findall('<li><a href="(.*?)" title="(.*?)" .*?>(.*?)</a></li>', t[0])
	# print(re.findall('<li><a href="(.*?)" title="(.*?)" .*?>(.*?)</a></li>', t[0]))
	for i in html_url:
		# print(url + i[0])
		# print(i[1])
		# if not os.path.exists(f'第一ppt/{i[1]}'):
		# 	os.makedirs(f'第一ppt/{i[1]}')
		zhu_url[i[1]] = url + i[0]


def lie(url):
	he = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
	}
	
	html = requests.get(url=url, headers=he)
	html.encoding = html.apparent_encoding
	# url_s_ = html_html.xpath('/html/body/div[5]/dl/dd/div[2]/ul/li[12]/a/@href').get()
	url_s_ = re.findall("<li><a href='(.*?)'>末页</a></li>", html.text)[0]
	# print(url_s_)
	xxxx = re.compile('\d+')
	kp = xxxx.findall(url_s_)
	kp = kp[-1::][0]
	url_zong = url + url_s_
	url_zong = url_zong.replace(''.join(kp), '**')
	# print(int(kp) + 1)
	# print(url_zong[0:-7])
	# print(url_zong)
	for i in range(1, int(kp) + 1):
		url = url_zong.replace('**', str(i))
		# print(url)
		html = requests.get(url=url, headers=he)
		html.encoding = html.apparent_encoding
		html_html = parsel.Selector(html.text)
		hrml_title = html_html.xpath('/html/body/div[5]/dl/dd/ul/li/h2/a/text()').getall()
		hrml_url = html_html.xpath('/html/body/div[5]/dl/dd/ul/li/h2/a/@href').getall()
		# https://www.1ppt.com/article/90328.html
		with ThreadPoolExecutor(5) as t:
			for mk in hrml_url:
				t.submit(download, 'https://www.1ppt.com' + mk)


def download(url):
	he = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
	}
	html = requests.get(url=url, headers=he)
	html.encoding = html.apparent_encoding
	ghf = re.compile('<li>所属频道：<a href=".*?" target="_blank" >(.*?)</a></li>')
	hrml__mk = ghf.findall(html.text)
	html_html = parsel.Selector(html.text)
	url_s_ = html_html.xpath('/html/body/div[4]/div[1]/dl/dd/ul[1]/li/a/@href').get()
	io = 'https://www.1ppt.com' + url_s_
	html = requests.get(url=io, headers=he)
	html_html = parsel.Selector(html.text)
	html__url = html_html.xpath('/html/body/dl/dd/ul[2]/li[1]/a/@href').get()
	html__title = html_html.xpath('/html/body/dl/dt/h1/a/text()').get()
	time_start = time.time()
	print(f'开始:{html__title}')
	if not os.path.exists('第一ppt/' + hrml__mk[0]):
		os.makedirs('第一ppt/' + hrml__mk[0])
	
	path = '第一ppt/' + hrml__mk[0] + '//' + html__title + '.zip'
	with open(path, 'wb') as f:
		html = requests.get(url=html__url, headers=he)
		f.write(html.content)
	time_end = time.time()
	print(f'结束:{html__title},共用时间{int(time_end - time_start)}')


if __name__ == '__main__':
	time_start = time.time()
	zhuye()
	with ProcessPoolExecutor(2) as t:
		for i in zhu_url.values():
			lie(i)
	time_end = time.time()
	print(f'总共时间{int(time_end - time_start)}')
