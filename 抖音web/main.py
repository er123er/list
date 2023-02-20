import json

import requests

url = 'https://aiqicha.baidu.com/s?q=%E5%8D%97%E4%BA%AC%E7%A7%91%E6%8A%80&t=0'

he = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
     "Accept-Encoding": 'gzip, deflate, br',
    "Accept-Language": 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    "Connection": 'keep-alive',
    'Cookie': '__bid_n=186584aea847b1260d4207; FPTOKEN=EW4rEBWm8n8e3hpNYRc6wwaryoALNWu4mh2BBCyWAcpKD3y+HqG20dGbVw9dJFrZUjNQjyMWF/3gEgH/P2P5wA1FXre9qiOHLnbqzEiYNmuyc+hg4lYFGPOPVr0b77megM6TLEalcA2dCaOqMe5NAiAncsP0UZXfiSW8fcGTOWZhulp/HJz4q+MpV4tRRIcXhusP4rlMcGgUcYXzrlvpzpeeM34HJYnzS6r6FXt2FknaxN6QxbEDZzP9jMTzll1P1lkDm7gPtn/jwHVkxnxQH21OKsuBxLu3+gHnm07IgIEs9UitClL/UdygRCPAebYRRLFTu3BOqVJogZV3XbjiqF1X+evSDlC9/q2pmXRmIX+X+yDbFk7N0Sx/kzlafdd/AUnoaltV9OmXQCV9ad4yf6MiAVFa9ACZDueA4s/Vd3HSrP4IkNfaPjff0OHiZxJs|lTkYXQg7+JHTEUM4CnYd48k/aAcm6MRGPiKFxm2PJdM=|10|91aed8fb6adecabdb79e39af8bee78c9; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1676813408; _j47_ka8_=57; log_guid=9a628713d6c8e306752b9ef9ff2b6bee; ZX_UNIQ_UID=bec32d785b06a8cac0499b6fa499f4a2; BAIDUID=1776BCBA765DD3D7B4AD81D8F3BC0AB9:FG=1; log_first_time=1676817848775; ZX_HISTORY=%5B%7B%22visittime%22%3A%222023-02-19+22%3A53%3A44%22%2C%22pid%22%3A%22xlTM-TogKuTw1%2ADZoeFlmfgzQABaqPhw%2AAmd%22%7D%5D; ab167681520=c1a519473c8ab8ea16d7cfa3b5f9528e1676818426577; _fb537_=xlTM-TogKuTwKFvlYDQrVl5vy8li%2ArimXvr3KlrKmvGxmd; BAIDUID_BFESS=1776BCBA765DD3D7B4AD81D8F3BC0AB9:FG=1; ab167681880=c7a519473c8ab8ea16d7cfa3b5f9528e1676820648073; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1676820648; log_last_time=1676820648921; ab_sr=1.0.1_ZjRjYzIxYzQ3Yjk1ODQyMjMwNmRkNDE0ZGNjMWY4ZDg0M2I5ZDExMTU5OWMxNDM3ZjgzNDllMzM4YWM1NWE4ZmQxMWNiZjUxNWI2OWM4ZWQ5MTY4NTQ5ZWI4ZmNjZjI4MmIzOThmZDBmYzdiODkyZGNhZWZhMzVhNjMxNTYxZDg3OGJhMjY4YmFhZmQ3NTkzYmE3MGJhZGU4MTBhYTY0YQ==; _s53_d91_=cf2ad441564efd8f1f1fbb830cd217912dc6be0677249c8961118b9a9552a815f6dd4bafac43a2a8d4e3b2b3c899ec97a7310d5ca41857f7ced0a33b683bebdde894846336007ab1350b04d405111c201d00f617dec5898e3c5dd647e30521c0d3368ace7ea6b8cf0be9a6e713897b1528940eb4917179d584cf42467748e04d65c2719aae74bcd672ce0d934b59d768df036021d92181b4e604db1bca79e3c8f2fb0bf3680d7e2444d108139ded02ba557a1dcf845cdac720c62accfe70929a7ee68599581a76a76eb24363886e2e0d; _y18_s21_=491475e9; RT="z=1&dm=baidu.com&si=94d3204c-813a-4f68-8498-e1f7ea7f7f8e&ss=lebi1tyy&sl=h&tt=tx0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1o5qo&ul=1qies"',
    "Host": 'aiqicha.baidu.com',
    "Referer": 'https://aiqicha.baidu.com/s?q=%E5%8D%97%E4%BA%AC%E7%A7%91%E6%8A%80&t=0',
    "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    "sec-ch-ua-mobile": '?0',
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": 'document',
    "Sec-Fetch-Mode": 'navigate',
    "Sec-Fetch-Site": 'same-origin',
    "Sec-Fetch-User": '?1',
    "Upgrade-Insecure-Requests": '1',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50',

}

u = requests.get(url, headers=he)

print(u.text)
