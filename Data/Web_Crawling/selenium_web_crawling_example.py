# 소득세액공제 

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import pandas as pd 

# 크롬 드라이버 객체 생성
driver = webdriver.Chrome()

# 페이지 열기
url = "https://www.shinhan.com/hpe/index.jsp#050101040000"
driver.get(url)

# driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/ul/li[2]/a').click()

q_list=[]

##click to 질문
for k in range(1,7):
    try:
        print("페이지 수 : ",k)
        print("--------------------------------")

      #  driver.find_element(By.XPATH,f'//*[@id="pl_pageNav_page_{k}"]').send_keys(Keys.ENTER)
      #  driver.find_element(By.XPATH,f'/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[4]/ul/li[{k+2}]/a').send_keys(Keys.ENTER)
        new_page = f'//*[@id="pl_pageNav_page_{k}"]'
        print(new_page)
        wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, new_page)))
        
        try:
            for i in range(1,11):
                print("질문 수 : ",i)
                #/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/div/table/tbody/tr[1]/td[2]/nobr/a
                q_path=f'/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/div/table/tbody/tr[{i}]/td[2]'
              #  wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, q_path)))
               
                driver.find_element(By.XPATH, q_path).click()
                time.sleep(3)
                ##get text
#                 dt_elements = driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/dl/dt/span[2]")
#                 dd_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/dl/dd/span[2]")
                
                dt_elements = driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/dl/dt/span[1]")
                dd_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/dl/dd/span[1]")
           
                print("dt_elements", dt_elements[0].get_attribute('innerText'))
                print("dd_elements", dd_elements[0].get_attribute('innerText'))
                dt_list = []
                dd_list = []
                for i in range(len(dt_elements)):

                    #dt = dt_elements[i].text.replace("\n"," ").strip()
                    #dd = dd_elements[i].text.replace("\n"," ").strip()
                    dt = dt_elements[i].get_attribute('textContent').replace("\n"," ").strip()
                    dd = dd_elements[i].get_attribute('textContent').replace("\n"," ").strip()
                    
                    dt_list.append(dt)
                    dd_list.append(dd)
                    dict_elements = {'Instruction':dt_list[0],'Context':'','Response':dd_list[0],'Category':'open_qa'}
                    dict_elements['JSON']=f'{dict_elements}'
                    print(dict_elements)
                    q_list.append(dict_elements)
                     
                # 목록으로 돌아가기 
                back_to_list_path = '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/a'
                driver.find_element(By.XPATH, back_to_list_path).click()
                time.sleep(3)
              #  wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, back_to_list_path)))
                
        except Exception as e:
            print(e)
            print('질문 없습니다!')
                 
    except Exception as e:
        print(e)
        print('페이지 없습니다!')
    print("--------------------------------")
raw_data = pd.DataFrame(q_list)
raw_data.to_excel(excel_writer='example_소득세액공제.xlsx')