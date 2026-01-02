import time   ##imports python's built in time module
from selenium import webdriver  ##Imports selenium webdriver which controls the browser
from selenium.webdriver.common.by import By   ##Imports By which helps to locate elements
from selenium.webdriver.chrome.service import Service   ##Used to define how chrome driver started as a service
from webdriver_manager.chrome import ChromeDriverManager   ##automatically downloads and manages chromedriver

##stores the world population live counter url
URL = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"

##defines a function that open browser,read live population and print it continuously
def run_population_loop():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))   #LAunches chromebrowser and chrome driver manager to install driver automatically
    driver.maximize_window()      ##To maximize the browser window
    driver.implicitly_wait(10)    ##sets an implicit waits for 10 secs
    driver.get(URL)               ##opens the world population website in chrome

    # Close cookie popup if visible
    try:
        driver.find_element(By.XPATH, "//button[contains(text(),'Got it')]").click()    ##locator for cookie button
    except:
        pass             ##if popup is not present ignore and continue execution

##Xpath for population counter
    xpath = "//div[contains(@class,'counter-ticker')]"

    print("\nPress CTRL + C to stop\n")     ##telling the user to stop by pressing ctrl+c

    try:                             ##wraps the infinite loop in try so ctrl c can be handled
        while True:                  ##Infinite loop keeps running until user stops it
            text = driver.find_element(By.XPATH, xpath).text    ##reads the population count from webpage
            print("Live Population Count:", text, flush=True)  ##prints the population value to the cmd prompt
            time.sleep(1)                ##pauses execution for 1sec before fetching the next value
    except KeyboardInterrupt:             ##catches ctrl+c interruption from the user
        print("\nStopped by user (CTRL + C)")    ##prints the message stopped by user
    finally:                                          ##ensures browser always closes even if an error occurs
        driver.quit()
   ##flush=True used because it ensures instant output which is very much useful for live updates


if __name__ == "__main__":     ## ensures this script runs only when executed directly not when imported
    run_population_loop()      ##calls the main function and starts the live population tracking

''' Here in the project i have made two separate sections 1.Scripts 2.tests.
 because pytest + infinite loop will not work and pycharm does not handle ctrl+c ,as its the tool behaviour,thus 
 running scripts with pytest not possible'''
'''scripts will automate and runs the webpage also provides count and stops when ctrl +c is pressed
'''


