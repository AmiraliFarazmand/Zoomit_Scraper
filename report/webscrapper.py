import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from report.models import Report,Tag 

def add_single_post(title:str, input_tags:list, link:str, article:str):
    new_post = Report.objects.create(title=title, article=article, refrence=link)
    for tag_name in input_tags:
        Tag.objects.get_or_create(pk=tag_name)
        new_post.tags.add(Tag.objects.get(pk=tag_name)) # Can be modified!!!!!!!!!!!!!!!!!!!!!
    
def extract_some_page(pages_count:int):
    for page_no in range(pages_count):
        url = f"https://www.zoomit.ir/archive/?sort=Newest&publishPeriod=All&readingTimeRange=All&pageNumber={page_no}"
        wd = webdriver.Edge(keep_alive=True)
        wd.maximize_window()
        wd.get(url)
        wd.implicitly_wait(7.56)  
        # Store the ID of the original window
        wait = WebDriverWait(wd, 8.8)
        original_window = wd.current_window_handle
        post_links = wd.find_elements(By.XPATH, "//a[contains(@class, 'BrowseArticleListItemDesktop__WrapperLink')]")

        links = [link.get_attribute('href') for link in post_links]
        # checks if previous posts were added, breaks the loop
        for link in links: 
            if Report.objects.filter(refrence=link).exists():
                break
            post = wd.switch_to.new_window('tab')
            wd.get(link)    
            wd.implicitly_wait(1.15)
            xpath="//*[@id=\"__next\"]/div[2]/div[1]/main/article/header/div/div/h1"
            title = wd.find_element(By.XPATH, xpath).text

            xpath_pattern = '//*[@id="__next"]/div[2]/div[1]/main/article/header/div/div/div[2]/div[1]/a/span'
            span_elements = wd.find_elements(By.XPATH, xpath_pattern)
            tags = []
            for elm in span_elements:
                tag_text = elm.text
                tags.append(tag_text)
            article = wd.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[1]/main/article/div/div[5]/div/div/div").text
            wd.close()

            
            #Switch back to the old tab or window
            wd.switch_to.window(original_window)

        wd.quit()
