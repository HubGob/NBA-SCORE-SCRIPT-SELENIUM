from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

print("NBA LATEST GAMES PLAYOFFS")
year = input("Enter year: ")
month = input("Enter month: ")
day = input("Enter day: ")

url = f"https://www.nba.com/games?date={year}-{month}-{day}"
def setup_driver():
    options = Options()
    options.add_argument("--headless")
   
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# Set up Selenium2025
driver = setup_driver()
driver.get(url)

# Wait for content to load (adjust time as needed)
driver.implicitly_wait(10)

# Find chapter elements - adjust selector based on actual structure
chapter_links = driver.find_elements(By.CSS_SELECTOR, 'div[class*="GamesView_gameCardsContainer__c_9fB"] a[href*="/game/"]')

games = [0,3]
if chapter_links:
    for game in games:
        latest_chapter = chapter_links[game]
        chapter_title = [latest_chapter.text]
        chapter_url = latest_chapter.get_attribute('href')

        separated_items = chapter_title[0].split('\n')
        
        print(separated_items[0])
        print(f'{separated_items[2]} - {separated_items[3]}')
        print(f'{separated_items[7]} - {separated_items[5]}')
        if int(separated_items[3]) > int(separated_items[5]):
            print(f'{separated_items[2]} - WINS')
        else:
            print(f'{separated_items[7]} - WINS')
        print(f"URL: {chapter_url}")
else:
    print("No gemes found")

driver.quit()