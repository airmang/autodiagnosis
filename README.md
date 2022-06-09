# autodiagnosis
###### 안산부곡중학교 1학년 방과후 수업 중 Selenium을 이용한 웹크롤링 프로젝트

셀레니움을 이용하여 자가진단 자동화 프로그램을 만들어보자.

## 1. 파이썬 설치 및 셀레니움 설치

  pip install selenium

해당 명령어를 입력하여 셀레니움 패키지를 설치해준다.

## 2. 크롬드라이버 설치
현재 사용하고 있는 크롬 브라우저의 버전을 확인하고
크롬 드라이버 홈페이지에 들어가서

[크롬드라이버설치페이지](https://chromedriver.chromium.org/downloads)


![image](https://user-images.githubusercontent.com/38392618/172553246-217c6e9a-404a-4c45-b92e-cc1496fafc56.png)

크롬드라이버를 설치 하고 프로젝트를 저장할 폴더에 압축해제 하여 저장한다.

## 3. 셀레니움과 크롬드라이버 작동 확인

```python
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
url_path = 'https://hcs.eduro.go.kr/#/loginWithUserInfo'
driver.get(url_path)
driver.implicitly_wait(5)
driver.maximize_window()
```
