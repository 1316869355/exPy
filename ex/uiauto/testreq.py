# -*- coding:utf-8 -*-
#! python3
#! Requests

import webbrowser, requests, sys, pyperclip,bs4

print(sys.argv)
#if len(sys.argv) > 1:
#    webbrowser.open(sys.argv[1])

py_page = open('pypage.html', 'wb')
if len(sys.argv) > 1:
    if len(sys.argv) == 2:
        re =requests.get(sys.argv[1])
    else:
        re = requests.get(sys.argv[1] +'baidu?ie='+sys.argv[2]+'&wd='+ sys.argv[2])
    print(re.status_code)
    #print(str(re.text[1:255]))
    for chunk in re.iter_content(1000000):
        py_page.write(chunk)
    py_page.close()
    noStarchSoup = bs4.BeautifulSoup(re.text)
    ele = noStarchSoup.select('div#weather')
    print(ele[0] if len(ele)==1 else ele[1])
else:
    webbrowser.open(pyperclip.paste())

