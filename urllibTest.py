# -*- coding: utf-8 -*-

import socket
from urllib import request, parse, error
from bs4 import BeautifulSoup, NavigableString
import lxml

# 测试
def request_baidu():
    
    response = urllib.request.urlopen('http://www.baidu.com')
    print(response.read().decode('utf-8'))

def request_error_TO():
    data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf8')

    # print(data)

    try:
        response = urllib.request.urlopen('http://httpbin.org/', timeout=0.1, data=data)
        print(response.read())
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')

def response_test():
    response = urllib.request.urlopen('http://httpbin.org/')
    print(type(response)) #  <class 'http.client.HTTPResponse'>
    print(response.status, response.getheaders(), response.getheader('server'))
    """
    status : 200
    headers: [('Access-Control-Allow-Credentials', 'true'), ('Content-Type', 'text/html; charset=utf-8'), ('Date', 'Thu, 25 Jul 2019 06:58:38 GMT'), ('Server', 'nginx'), ('Content-Length', '9593'), ('Connection', 'Close')]
    getheader('server'): nginx
    
    """
    for header in response.getheaders():
        print(header)
    
    headersDict = dict(response.getheaders())
    print(headersDict.keys())

# test beautiful soup
def bs_test():
    
    response = urllib.request.urlopen('http://httpbin.org/')
    html = response.read()
    print(html)
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        print(tag.get('href'), None)
        
# 原始socket 测试
def socket_test():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if(len(data) < 1):
            break
        print(data.decode())
    mysock.close()

# 实现手机号归属地查询功能

def search_phone_area():
    # urllib.request
    html = ''
    """
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
               	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Encoding': 'gzip',
		'Accept-Language': 'zh-CN,zh'}
    #dict = {'action': 'mobile','mobile':'15993213784'}
    #data = bytes(parse.urlencode(dict), encoding='gb2312')
    #length = len(data)
    #headers['Content-Length'] = length
    #print(headers)
    mobile = '15993213784'
  
    try :
        req = request.Request(url='http://www.ip138.com:8080/search.asp?action=mobile&mobile='+ mobile, method='GET', headers=headers)
        response = request.urlopen(req)
        #print(response.status, response.getheaders(), response.getheader('server'))
        html = response.read().decode('gb2312')
    except error.HTTPError as e:
        print('[error] ------- ', e.reason)
    """
    html = """
   
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">

    <html><head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type"/>
    <meta content="format=html5; url=http://m.ip138.com/mobile.html" http-equiv="mobile-agent">
    <title>【IP138】― 138查！ http://www.IP138.Com/</title>
    <meta content="IP138,IP地址查询,手机号码归属地,邮政编码,长途电话区号,身份证号码验证专业查询网" name="description"/>
    <meta content="IP138,IP地址查询,手机号码归属地,邮政编码,长途电话区号,身份证号码验证查询,域名查询,whois查询" name="keywords"/>
    <style type="text/css">A:link {
            COLOR: #1c5f82; TEXT-DECORATION: none
    }
    A:visited {
            COLOR: #1c5f82; TEXT-DECORATION: none
    }
    A:hover {
            COLOR: #cc5533; TEXT-DECORATION: underline
    }
    A.red:link {
            COLOR: #ff0000; TEXT-DECORATION: none
    }
    A.red:visited {
            COLOR: #ff0000; TEXT-DECORATION: none
    }
    A.red:hover {
            COLOR: #ff0000; TEXT-DECORATION: underline
    }
    .subt {
            COLOR: #aa3333; FONT-FAMILY: "宋体"; FONT-SIZE: 9pt
    }
    .tdc {
            COLOR: #333333; FONT-FAMILY: "宋体"; FONT-SIZE: 9pt
    }
    .tdc1 {
            COLOR: #ffffff; FONT-FAMILY: "宋体"; FONT-SIZE: 9pt
    }
    .tdc2 {
            COLOR: #008000; FONT-FAMILY: "宋体"; FONT-SIZE: 9pt
    }
    .bdtj {
            BACKGROUND: #6699cc; BORDER-BOTTOM: #6699cc 1px solid; BORDER-LEFT: #6699cc 1px solid; BORDER-RIGHT: #6699cc 1px solid; BORDER-TOP: #6699cc 1px solid; COLOR: #ffffff; FONT-SIZE: 9pt; HEIGHT: 18px
    }
    BODY {
            SCROLLBAR-HIGHLIGHT-COLOR: #f7f7f7; SCROLLBAR-SHADOW-COLOR: #f7f7f7; SCROLLBAR-ARROW-COLOR: #EFF1F3; SCROLLBAR-TRACK-COLOR: #EFF1F3; SCROLLBAR-BASE-COLOR: #f7f7f7
    }
    </style>
    <script language="JavaScript">
    <!--
            function resizeMe(){
                    window.focus();
            }
    //-->
    </script>
    <script language="JavaScript">
    <!--
    if(!String.prototype.trim) {
            String.prototype.trim = function () {
                    return this.replace(/^\s+|\s+$/g,'');
            };
    }
    function checkMobile(){
            var sMobile = document.mobileform.mobile.value.trim();
            if(!(/^1[3|4|5|6|7|8|9][0-9]{5,9}$/.test(sMobile))){
                    alert("不是完整的11位手机号或者正确的手机号前七位");
                    document.mobileform.mobile.focus();
                    return false;
            }
    }
    //-->
    </script>
    </meta></head>
    <body leftmargin="1" onload="javascript:resizeMe()" topmargin="1">
    <center><a href="http://www.ip138.com" target="_blank"><font class="tdc">手机号码归属地专业在线查询网</font></a>
    </center>
    <hr size="1" width="320"/>
    <table align="center" border="1" bordercolor="#3366cc" cellpadding="4" style="BORDER-COLLAPSE: collapse" width="360">
    <form action="" method="get" name="mobileform" onsubmit="return checkMobile();">
    <tr bgcolor="#eff1f3" class="tdc">
    <td align="middle" noswap="" width="130">手机号码(段) </td>
    <td align="middle" width="*"><input class="tdc" maxlength="11" name="mobile"/>
    <input name="action" type="hidden" value="mobile"/> <input class="bdtj" type="submit" value="查 询"/>
    </td>
    </tr>
    </form>
    </table>
    <br/>
    <table align="center" border="1" bordercolor="#3366cc" cellpadding="4" style="border-collapse: collapse" width="360">
    <tr>
    <td align="center" bgcolor="#6699cc" class="tdc1" colspan="2" height="24">++ ip138.com查询结果 ++</td>
    </tr>
    <tr bgcolor="#EFF1F3" class="tdc">
    <td align="center" noswap="" width="138">您查询的手机号码段</td>
    <td align="center" class="tdc2" width="*">15993213784 <a href="http://jx.ip138.com/15993213784/" target="_blank">测吉凶(<font color="red">新</font>)</a></td>
    </tr>
    <tr bgcolor="#EFF1F3" class="tdc">
    <td align="center">卡号归属地</td>
    <td align="center" class="tdc2">河南 周口市</td>
    </tr>
    <tr bgcolor="#EFF1F3" class="tdc">
    <td align="center" noswap="" width="138">卡 类 型</td><td align="center" class="tdc2">移动预付费卡</td>
    </tr>
    <tr bgcolor="#EFF1F3" class="tdc">
    <td align="center">区 号</td>
    <td align="center" class="tdc2">0394</td>
    </tr>
    <tr bgcolor="#EFF1F3" class="tdc">
    <td align="center">邮 编</td>
    <td align="center" class="tdc2">466000 <a href="http://alexa.ip138.com/post/" target="_blank">更详细的..</a></td></tr>
    </table>
    <br>
    <div align="center">
    <script type="text/javascript">
    var cpro_id = "u2299786";
    </script>
    <script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>
    </div>
    <p align="center"><a href="http://qq.3533.com:8080/book.asp?siteid=9&amp;no=15993213784" rel="nofollow" target="_blank">如发现手机号码所在地数据不对.请按此留言.谢谢</a></p>
    <p align="center">手机WAP上网查询手机号地址 wap.ip138.com 用手机随时可以查</p>
    <p align="center"><a href="http://www.ip138.com/sjlink.htm" rel="nofollow" target="_blank">欢迎各网站免费链接本站手机号码查询系统,获取代码按此</a></p>
    <div style="display:none"><script charset="UTF-8" src="http://tajs.qq.com/stats?sId=36241650" type="text/javascript"></script></div>
    </br></body></html>
    """
    soup = BeautifulSoup(html, 'lxml')
    #print(soup.prettify())
    table_cont = soup.find_all('table')
    
    for dom_tr in table_cont[1].find_all('tr'):
        for dom_td in dom_tr:
            if not isinstance(dom_td, NavigableString):
                print(dom_td.string)
            
        
    # 解决办法一
    """
    td_cont = soup.select('table>tr>td:last-child')
    for dom in td_cont:
        print(dom.string)
    """
# request_baidu()
# response_test()
# socket_test()
search_phone_area()
