from time import perf_counter
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


URL = "https://mathup.com/games/crossbit?mode=daily_challenge"


def main():
    driver = webdriver.Chrome()
    webdriver_wait = WebDriverWait(driver, 10)
    driver.get(URL)
    time_to_load = []
    for attempt in range(1, 11):
        star_counter = perf_counter()
        webdriver_wait.until(
            EC.visibility_of_element_located((By.XPATH, '//div[text()="Start"]'))
        )
        end_counter = perf_counter()
        print(
            "Attempt: ",
            attempt,
            "Time to load start button: ",
            (load_time := end_counter - star_counter),
            " Seconds",
        )
        time_to_load.append(load_time)
        driver.get(URL)
    average = sum(time_to_load) / 10
    print("Average time to load the start button: ", average, " Seconds")


main()
