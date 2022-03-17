from speed_test import speedTest
from twitter import twitter
import time

# My Paid for Internet speeds (made up values)
DOWN = 150
UP = 10

speedTest = speedTest()
# Run the speed test
check_speed_click = speedTest.click_speed_test()

if check_speed_click:
    # collect speed data
    speed_data = speedTest.get_speed_data()
    download_speed = speed_data["download_speed"]
    upload_speed = speed_data["upload_speed"]

    # send a tweet if speed data is less than your Internet plan
    if download_speed < DOWN or upload_speed < UP:
        time.sleep(5)
        twitter = twitter()
        twitter.twitter_login_button()
        twitter.twitter_login_process()
        twitter.tweet(speed_data)



