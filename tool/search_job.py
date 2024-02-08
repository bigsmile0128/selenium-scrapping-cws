
# ブラウザ操作のライブラリを読み込み
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
import time

from bs4 import BeautifulSoup

from tool.database import *
from tool.bid import *
from utils.notification import *


def search_jobs():
        


    ################################################################################
    options = Options()
    # options.add_argument('--disable-extensions')       # すべての拡張機能を無効にする。ユーザースクリプトも無効にする
    # options.add_argument('--proxy-server="direct://"') # Proxy経由ではなく直接接続する
    options.add_argument('--proxy-bypass-list=*')      # すべてのホスト名
    options.add_argument('--start-maximized')          # 起動時にウィンドウを最大化する
    # options.add_argument('--incognito')                # シークレットモードの設定を付与
    # options.add_argument('--headless')      
    # options.add_argument('--user-data-dir=C:\\Users\\Bigsmile\\AppData\\Local\\Google\\Chrome\\User Data')    
    # options.add_argument('--profile-directory=Profile 3')

    #Chromeの立ち上げ
    driver = webdriver.Chrome(options=options)

    try:
        
        # first login
        driver.get("https://crowdworks.jp/login?ref=toppage_hedder")
        
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        # HTMLが取得出来なかった場合はエラー内容を保管する
        except Exception as e:
            search_jobs()


        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
    except:
        search_jobs()

    category_urls = ["https://crowdworks.jp/public/jobs/search?category_id=226&keep_search_criteria=true&order=new&hide_expired=true",
            'https://crowdworks.jp/public/jobs/search?category_id=242&keep_search_criteria=true&order=new&hide_expired=true',
            # 'https://crowdworks.jp/public/jobs/search?category_id=84&keep_search_criteria=true&order=new&hide_expired=true',
            # 'https://crowdworks.jp/public/jobs/search?category_id=230&keep_search_criteria=true&order=new&hide_expired=true',
            ]

    url_index = 0

    while True:
        try:

            driver.get (category_urls[url_index%2])

            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "result_jobs")))
            # HTMLが取得出来なかった場合はエラー内容を保管する
            except Exception as e:
                url_index = url_index + 1
                continue

            url_index = url_index + 1
            
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            job_lists = soup.select("div.item.job_item")
            
            for job in job_lists:
                job_title = job.select_one("h3.item_title").text
                job_link = "https://crowdworks.jp" + job.select_one("h3.item_title a")['href']
                category = job.select_one("div.sub_category.meta_column").text
                employer_name = job.select_one("span.user-name").text
                payment = job.select_one("div.entry_data.payment").text
                post_date = job.select_one("div.post_date.meta_column").text.replace("掲載日：", "")
                
                # Insert only if the row does not already exist
                if not row_exists(job_title, employer_name, post_date):
                    driver.get(job_link)
                            
                    try:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td.confirm_outside_link")))
                    # HTMLが取得出来なかった場合はエラー内容を保管する
                    except Exception as e:
                        continue
                    
                    html=driver.page_source
                    soup=BeautifulSoup(html,'html.parser')
                    
                    
                    task_text = soup.select_one("td.confirm_outside_link").text
                    
                    try:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.cw-button")))
                    # HTMLが取得出来なかった場合はエラー内容を保管する
                    except Exception as e:
                        print(str(e))
                        continue
                    
                    # proposal_url = driver.find_element(By.XPATH ,"//a[@gtm_event_job_category='apply_click_development']").get_attribute('href')
                    
                    # driver.get(proposal_url)
                    driver.find_element(By.CSS_SELECTOR, "a.cw-button").click()

                    try:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='proposal_conditions_attributes_0_message_attributes_body']")))
                    except Exception as e:
                        cursor.execute('''INSERT INTO jobs (title, link, employer_name, payment, post_date, category, bid) 
                                        VALUES (?, ?, ?, ?, ?, ?, ?)''', (job_title, job_link, employer_name, payment, post_date, category, bid))
                                
                        # Commit the changes to the database
                        connection.commit()
                        print(str(e))
                        continue
                    print("1")
                    # HTMLが取得出来なかった場合はエラー内容を保管する
                    bid = make_bid(job_title, employer_name, task_text, job_link)
                    print("2")

                    driver.find_element(By.XPATH, "//textarea[@id='proposal_conditions_attributes_0_message_attributes_body']").send_keys(bid)

                    print("3")
                    message = f"Employer: {employer_name}\nPayment: {payment}\n Detail: {task_text}"
                                    
                    cursor.execute('''INSERT INTO jobs (title, link, employer_name, payment, post_date, category, bid) 
                                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (job_title, job_link, employer_name, payment, post_date, category, bid))
                            
                    # Commit the changes to the database
                    connection.commit()

                    print("4")
                    driver.switch_to.new_window('tab')
                    print("5")
                    time.sleep(1)
                    driver.get(job_link)
                    driver.switch_to.new_window('tab')
                    time.sleep(1)
                    show_toast(job_title, message, job_link)
                else:
                    pass
            
        except Exception as e:
            print(str(e))
            continue
        

        
        
if __name__ == "__main__":
    search_jobs("https://crowdworks.jp/public/jobs/search?category_id=226&keep_search_criteria=true&order=new&hide_expired=true", "system")