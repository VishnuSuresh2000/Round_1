from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome()
    webdriver_wait = WebDriverWait(driver, 10)
    driver.get("https://mathup.com/games/crossbit?mode=championship")
    for attempt in range(1, 11):
        print("Attempt: ", attempt)
        webdriver_wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h3[text()='Primary Goal']"))
        )
        button_element = webdriver_wait.until(
            EC.visibility_of_element_located((By.XPATH, '//div[text()="Start"]'))
        )
        button_element.click()
        difficulty_level_element = webdriver_wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[text()='Difficulty']/following-sibling::div")
            )
        )
        print("Difficulty level: ", difficulty_level_element.text)
        driver.refresh()


main()
