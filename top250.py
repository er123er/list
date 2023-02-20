import time
import requests
import parsel
import csv
from parsel import Selector

kaishi = time.time()
tou = {
	'电影名称',
	'电影导演主演',
	'电影链接',
	'电影评分',
	'电影评价',
}
f = open('豆瓣.csv', mode='a+', encoding='utf-8', newline='')
tou = csv.DictWriter(f, fieldnames=tou)
tou.writeheader()
p = 0
for i in range(0, 250, 25):
	print(f'第{p}页')
	p += 1
	url = f'https://movie.douban.com/top250?start={i}&filter='
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
		              'Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53 '
	}
	
	lianjie = requests.get(url, headers=headers)
	lianjie_1 = parsel.Selector(lianjie.text)
	lianjie_dagai = lianjie_1.css('#content > div > div.article > ol > li > div > div.info').getall()
	for i in lianjie_dagai:
		ii = Selector(text=i)
		lj = ii.css('div.hd > a::attr(href)').get()
		mc = ii.css('div.hd > a > span::text').get()
		jl = ii.css('div.bd > p:nth-child(1)::text').get()
		jl_2 = ii.xpath('//*[@class="bd"]/p[1]/text()[2]').get()
		pinglun = ii.css('div.bd > div > span:nth-child(4)::text').get()
		pinglun = pinglun.strip()
		try:
			pingjia = ii.css('div.bd > p.quote > span::text').get()
			pingjia = pingjia.strip()
		except:
			pingjia = '无'
		
		# print(lj.strip(), mc.strip(), jl.strip(), jl_2.strip(), pinglun, pingjia)
		dic = {
			'电影名称': mc.strip(),
			'电影导演主演': jl.strip() + jl_2.strip(),
			'电影链接': lj.strip(),
			'电影评分': pinglun,
			'电影评价': pingjia,
		}
		tou.writerow(dic)

f.read()
jiesu = time.time()
sj = jiesu - kaishi
print(f'总共时间:{sj:.2f}')
