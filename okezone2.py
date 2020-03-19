from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome() 
driver.get("https://search.okezone.com/search?q=corona%20virus")

df = pd.DataFrame(columns = ['link', 'title', 'date', 'content'])
pre_links = []
links = []

for i in range(1, 49): #33
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
    # if (i!=1):
    #     wait = WebDriverWait(driver, 10)
    #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"li.next")))
     
    #     allelements = driver.find_elements_by_xpath("//li[@class='next']/a")

    #     for element in allelements:
    #         element.click()

        
        # try:
        #     click=driver.find_element_by_xpath("//*[@id='article-pagination']/ul/li[@class='next']/a")
        #     click.click()
        # except:
        #     try:
        #         click=driver.find_element_by_xpath("//*[@id='article-pagination']/ul/li[8]/a")
        #         click.click()
        #     except:
        #         try:
        #             click=driver.find_element_by_xpath("//*[@id='article-pagination']/ul/li[7]/a")
        #             click.click()
        #         except:
        #             try:
        #                 click=driver.find_element_by_xpath("//*[@id='article-pagination']/ul/li[6]/a")
        #                 click.click()
        #             except:
        #                 try:
        #                     click=driver.find_element_by_xpath("//*[@id='article-pagination']/ul/li[5]/a")
        #                     click.click()
        #                 except:
        #                     click=driver.find_element_by_xpath("//*[@id='article-pagination']/ul/li[4]/a")
        #                     click.click()
    # user_data = driver.find_elements_by_xpath('//*[@class="title"]').get_attribute('href')
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    # fullhtml = bs.find_all(class_='title')
    # soup = BeautifulSoup(fullhtml, 'lxml')
    url = bs.find_all('a', href=True)
    # url = bs.find_element_by_xpath("//div[@class='title']//a").attr('href')
    # user_data = driver.find_all('h1', class='title')
    
    

    for text in url:
        text = text['href']
        text = str(text)
        # text = text[text.index([s for s in text if 'http' in s])]
        text = text.replace('"', '')
        text = text.replace('href=', '')
        pre_links.append(text)
        if ('https' in text):
            if('okezone' in text):
                if (text!='https://www.okezone.com/'):
                    splitted_url = text.split('.')
                    if (splitted_url[0]=='https://news'):
                        links.append(text)
        # print(text)
    click=driver.find_element_by_xpath("//*[@class='next']/a")
    click.click()

pre_links = list(set(pre_links))
all_links = pd.DataFrame(pre_links)
all_links.to_csv(r'C:\Users\Muarrikh Yazka\arin\all_links_okezone_corona_last.csv', header=True)
links = list(set(links))

tmp = 0



wait = WebDriverWait(driver, 10)
for x in links:
    print(str(x))
    driver.get(str(x))
    v_link = x
    print(v_link)
    v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1"))).text
    print(v_title)
    v_date =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.namerep > b"))).text
    print(v_date)
    v_content =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#contentx.read"))).text
    print(v_content)
    df.loc[len(df)] = [v_link, v_title, v_date, v_content]
    tmp+=1
    if (tmp%25==0):
        path = 'C:\\Users\\Muarrikh Yazka\\arin\\okezone_corona_'+str(tmp)+'.csv'
        df.to_csv(path, header=True)

driver.close()

    
    
        
    # driver.findElement(By.xpath("//a/img[contains(@src,'/console/themes/images/new_imgs/status_light_off.png')]")).click()
    # path = 'C:\\Users\\Muarrikh Yazka\\arin\\okezone_corona_'+str(i)+'.csv'
    # df.to_csv(path, header=True)

df.to_csv(r'C:\Users\Muarrikh Yazka\arin\okezone_corona_last.csv', header=True)
print('DONE')






