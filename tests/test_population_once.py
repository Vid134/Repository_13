import pytest                      ##imports the pytest framework which is used to write and run testcases
from selenium import webdriver    ##Imports selenium webdriver which controls the browse
from selenium.webdriver.common.by import By   ##Imports By which helps to locate elements
from selenium.webdriver.chrome.service import Service    ##Used to define how chrome driver started as a service
from webdriver_manager.chrome import ChromeDriverManager  ##automatically downloads and manages chromedriver

##stores the world population live counter url
URL = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"

''' Marks the test as a population-related test.Majorly used for running selectee tests,organosing test suites 
and generating reports'''
@pytest.mark.population
def test_world_population_once():   ##defines pytest function
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))   #LAunches chromebrowser and chrome driver manager to install driver automatically
    driver.maximize_window()       ##to maximise the window
    driver.implicitly_wait(10)      ##sets an implicit waits for 10 secs
    driver.get(URL)                   ##opens the world population website in chrome

    # Close cookie popup if visible
    try:
        driver.find_element(By.XPATH, "//button[contains(text(),'Got it')]").click()  ##locator for cookie button
    except:
        pass

##Xpath for population counter
    xpath = "//div[contains(@class,'counter-ticker')]"
    text = driver.find_element(By.XPATH, xpath).text ##Locates the live population counter element and extracts the text
    print("Population from pytest:", text)   ##prints the population count

    assert text.strip() != ""  # just to mark test as passed

    driver.quit()   ##closes the browser
 ##pytest=verification