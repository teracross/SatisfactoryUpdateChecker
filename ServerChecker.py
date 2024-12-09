from selenium import webdriver
from bs4 import BeautifulSoup

def main (self):
  if (findLatestServerVersion > getHostedServerVersion): 
    triggerHostedServerUpdate()

def findLatestServerVersion():
  options =webdriver.ChromeOptions()
  options.add_argument("--headless=new")

  driver = webdriver.Chrome(options=options)
  url = "https://questions.satisfactorygame.com/patchnotes/search?date=All%20Time"
  driver.get(url)
  src  = driver.page_source
  driver.quit()

  soup = BeautifulSoup(src, 'html.parser')
  versions = [int(val.removeprefix("1.0 ")) for values in soup.findAll('div', class_='version_number') for val in values]
  res = versions.sort()
  return res

def getHostedServerVersion():
  NotImplemented

def triggerHostedServerUpdate():
  NotImplemented