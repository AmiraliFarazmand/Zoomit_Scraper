from bs4 import BeautifulSoup
import requests

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from report.models import Report,Tag 

def add_single_post(title:str, input_tags:list, link:str, article:str):
    new_post = Report.objects.create(title=title, article=article, refrence=link)
    for tag_name in input_tags:
        # if tag_name in ("داستان برند", "آموزش", ):
        #     pass
        Tag.objects.get_or_create(pk=tag_name)
        new_post.tags.add(Tag.objects.get(pk=tag_name)) # Can be modified!!!!!!!!!!!!!!!!!!!!!

    
def extract_some_page(from_page:int, to_page:int):
    wd = webdriver.Edge(keep_alive=True)
    wd.maximize_window()
    
    for page_no in range(from_page, to_page+1)[::-1]:
        url = f"https://www.zoomit.ir/archive/?sort=Newest&publishPeriod=All&readingTimeRange=All&pageNumber={page_no}"
        wd.get(url)
        wd.implicitly_wait(5.56)  
        # Store the ID of the original window
        original_window = wd.current_window_handle
        post_links = wd.find_elements(By.XPATH, "//a[contains(@class, 'BrowseArticleListItemDesktop__WrapperLink')]")

        links = [link.get_attribute('href') for link in post_links]
        # checks if previous posts were added, breaks the loop
        for link in links[::-1]: 
            try:
                if Report.objects.filter(refrence=link).exists():
                    break
                
                response = requests.get(link)

                if response.status_code == 200:
                    html_content = response.text
                    soup = BeautifulSoup(html_content, 'html.parser')

                    title = soup.find(class_="fzMmhL").get_text()

                    tags=[]
                    found_tags = soup.find_all(class_="cHbulB")
                    for tag in found_tags:
                        tags.append(tag.get_text(separator=' ', strip=True))

                    article_text = soup.find(class_ = "fNeDiY").get_text() 
                    for tag in soup.find_all(class_='gOVZGU'):
                        article_text += tag.get_text(separator=' ', strip=True) + ' \n'

                    add_single_post(title, tags, link,article_text)

            except Exception as e:
                print(e, link)
            
    wd.quit()
    print("ENDED!!!!")
