from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Setup your browser
driver = webdriver.Chrome()

# Opens youtube
driver.get("https://www.youtube.com/")

# Wait for the page to load
time.sleep(2)

# Search for the video
elem = driver.find_element(By.NAME, "search_query")
elem.send_keys("ncs background music")
elem.send_keys(Keys.RETURN)
# Get the video duration
time.sleep(2)

# Click on the first video
video = driver.find_element(By.XPATH ,'//*[@id="video-title"]/yt-formatted-string')
video.click()

# Wait for the page to load
# time.sleep(2)
ad_end_time = time.time() + 30 # The ad is expected to last 30 seconds
if time.time() < ad_end_time:
    time.sleep(1)
else:
    # The ad has finished playing
    pass
# Get the video duration
duration_element = driver.find_element(By.XPATH, '//span[@class="ytp-time-duration"]')
duration_text = duration_element.get_attribute("innerHTML")
duration_parts = duration_text.split(":")
duration_seconds = int(duration_parts[-1]) + int(duration_parts[-2]) * 60

# Wait for the video to finish playing
time.sleep(duration_seconds)

# Close the browser
driver.close()

