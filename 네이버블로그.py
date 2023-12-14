import requests
from bs4 import BeautifulSoup

def crawl_naver_blog(search_keyword):
    # 검색어를 이용하여 Naver 블로그 검색 결과 페이지의 URL 생성
    search_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"

    # HTTP GET 요청을 보내고 응답을 받아옴
    response = requests.get(search_url)

    # 응답이 성공적인지 확인
    if response.status_code == 200:
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 블로그 검색 결과가 있는 부분을 선택
        blog_results = soup.select('.sh_blog_top')

        for result in blog_results:
            # 블로그명
            blog_name = result.select_one('.sh_blog_title').text.strip()

            # 블로그 주소
            blog_url = result.select_one('.txt_block a').get('href')

            # 제목
            title = result.select_one('.sh_blog_title').get('title')

            # 포스팅 날짜
            post_date = result.select_one('.txt_inline').text.strip()

            # 결과 출력
            print(f"블로그명: {blog_name}")
            print(f"블로그 주소: {blog_url}")
            print(f"제목: {title}")
            print(f"포스팅 날짜: {post_date}")
            print("\n" + "="*50 + "\n")

    else:
        print(f"오류 발생: {response.status_code}")

if __name__ == "__main__":
    # 검색어 입력 받기
    search_keyword = input("검색어를 입력하세요: ")

    # 크롤링 수행
    crawl_naver_blog(search_keyword)
