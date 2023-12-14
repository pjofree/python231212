# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #오늘의 유머 베스트 게시판
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        # url 주소 확인
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        #list = soup.findAll('a', attrs={'class':'list_subject'})
        list = soup.find_all('td', attrs={'class':'subject'})

        # <td class="subject">
        #   <a href="/board/view.php?table=bestofbest&amp;no=472421&amp;s_no=472421&amp;page=1" target="_top">카페인에 너무 의존하면 생기는 일</a>
        #   <span class="list_memo_count_span"> [15]</span>  
        #   <span style="margin-left:4px;">
        #   <img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> 
        # </td>

        for item in list:
                try:
                    title = item.find("a").text.strip()
                    #print(title)
                    if (re.search('한국', title)):
                        print(title)
                except:
                        pass
        
