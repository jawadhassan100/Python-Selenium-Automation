from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
time.sleep(2)
elem = driver.find_element(By.NAME, "search_query")
elem.send_keys("ncs background music")
elem.send_keys(Keys.RETURN)
time.sleep(2)
video = driver.find_element(By.XPATH ,'//*[@id="video-title"]/yt-formatted-string')
video.click()
time.sleep(5)
duration_element = driver.find_element(By.XPATH, '//span[@class="ytp-time-duration"]')
duration_text = duration_element.get_attribute("innerHTML")
duration_parts = duration_text.split(":")
duration_seconds = int(duration_parts[-1]) + int(duration_parts[-2]) * 60

# Wait for the video to finish playing
time.sleep(duration_seconds)
# play_button = driver.find_element(By.XPATH ,'//*[@id="movie_player"]/div[29]/div[2]/div[1]/button')
# play_button.click()
# time.sleep(60)
driver.quit()

