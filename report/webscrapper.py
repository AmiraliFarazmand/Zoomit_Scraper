import requests
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
from report.models import Report,Tag 


def add_single_post(title:str, input_tags:list, link:str, article:str, date_str:str):
    '''
    Adds a instance to report model based on inputs
    '''
    published_date = published_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    new_post = Report.objects.create(title=title, article=article, refrence=link, published_date=published_date)
    for tag_name in input_tags:
        Tag.objects.get_or_create(pk=tag_name)
        new_post.tags.add(Tag.objects.get(pk=tag_name)) 
        json_data = {
            "title": title,
            "tags": input_tags,
            "refrence": link,
            "article": article,
            "published_date": date_str,
        }
    try:
        response = requests.post("https://amiralifzd.pythonanywhere.com/", json=json_data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send data: {e}")    


def process_link(link:str):
    '''
    Checks if it could extract data from link as a Zoomit post does it and then call add_single_post function
    otherwise it raise exception and prints it  
    '''
    try:
        if Report.objects.filter(refrence=link).exists():
            return
        response = requests.get(link)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            title = soup.find(class_="fzMmhL").get_text()
            tags = []
            found_tags = soup.find_all(class_="cHbulB")
            published_time = soup.find("meta", {"property": "article:published_time"})
            if published_time:
                published_time = published_time["content"]
            else:
                published_time = "2002-02-29T17:45:00Z"
                
            for tag in found_tags:
                tags.append(tag.get_text(separator=' ', strip=True))
            article_text = soup.find(class_="fNeDiY").get_text()
            for tag in soup.find_all(class_='gOVZGU'):
                article_text += tag.get_text(separator=' ', strip=True) + ' \n'
            add_single_post(title, tags, link, article_text, published_time)
    except Exception as e:
        print("EXCEPTION:", e, link)


def extract_some_page(from_page:int, to_page:int):  
    '''
    Crawl several pages zoomit.ir/archive and extracts a list of their links.
    then call proccess_link for each of them 
    '''
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    hub_url = "http://selenium-hub:4444/wd/hub"
    wd = webdriver.Remote(command_executor=hub_url,options=chrome_options)
    all_links =[]
    try:
        for page_no in range(from_page, to_page + 1):
            url = f"https://www.zoomit.ir/archive/?sort=Newest&publishPeriod=All&readingTimeRange=All&pageNumber={page_no}"
            wd.get(url)
            wd.implicitly_wait(5.56)
            post_links = wd.find_elements(By.XPATH, "//a[contains(@class, 'BrowseArticleListItemDesktop__WrapperLink')]")
            links = [link.get_attribute('href') for link in post_links]
            all_links.extend(links)
        all_links = list(reversed(all_links))
    finally:
        wd.quit()
    with ThreadPoolExecutor(max_workers=5) as executor: 
        executor.map(process_link, all_links)
    print("extract_some_page WAS DONE!!!!")
    

def extract_first_page():
    '''
    Crawl first page of zoomit.ir/archive and extracts a list of its links.
    then call proccess_link for each of them 
    '''
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    hub_url = "http://selenium-hub:4444/wd/hub"
    wd = webdriver.Remote(command_executor=hub_url,options=chrome_options)
    all_links =[]
    try:
        url = "https://www.zoomit.ir/archive/?sort=Newest&publishPeriod=All&readingTimeRange=All&pageNumber=1"
        wd.get(url)
        wd.implicitly_wait(5.56)
        post_links = wd.find_elements(By.XPATH, "//a[contains(@class, 'BrowseArticleListItemDesktop__WrapperLink')]")
        links = [link.get_attribute('href') for link in post_links]
        all_links.extend(links)
        all_links = list(reversed(all_links))
    finally:
        wd.quit()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(process_link, all_links)
    print("extract_first_page WAS DONE!!!!")