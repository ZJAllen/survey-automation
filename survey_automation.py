from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from datetime import date, time, datetime

# Booleans for the while loops below.
running = True
start = True
submit = False

# This is the time the browser will open and navigate to the form.
# Update these to fit your needs
# datetime(YEAR, MONTH, DAY, HOUR, MINUTE, SECOND)
open_time = datetime(2021, 4, 7, 11, 50, 0)

# This is the time the browser will submit the form.
# Update these to fit your needs
# datetime(YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, MICROSECOND)
submit_time = datetime(2021, 4, 7, 11, 5, 0, 100)

# Enter the survey URL here. This is just a dummy survey.
# survey_url = "https://www.surveymonkey.com/r/PZCCPLC"
survey_url = "https://www.surveymonkey.com/r/ZK53G8T"

# # These are just for testing. Uncomment as needed.
# name_input = "Last, First"
# number_input = "123456789"

opts = Options()

while running:
    while start:
        if datetime.now() >= open_time:
            # This triggers at the start time
            # This way it will open the browser ahead of time so you
            # can fill in the info.

            # Instantiate the brower instance
            browser = Chrome(options=opts)

            # Navigate to the survey url
            browser.get(survey_url)

            # Grabs ahold of the survey form for later.
            application_form = browser.find_element_by_name("surveyForm")

            # # These are just for testing. I got tired of typing them in manually.
            # # Uncomment as needed.
            first_input = browser.find_elements_by_tag_name("input")[0]
            first_input.send_keys(name_input)
            second_input = browser.find_elements_by_tag_name("textarea")[0]
            second_input.send_keys(number_input)

            # Set the start bool to True to let the program know we've opened
            # the form and are waiting for the submit time
            start = False

    while not submit:
        if datetime.now() >= submit_time:
            # This triggers at the submit time
            # Make sure all the required fields are populated and
            # the program will do the rest

            # This will submit the form
            application_form.submit()

            # Change the flags so we can get out of these nested While loops
            submit = True
            running = False


# This closes the webdriver. Otherwise you end up with a
# ton of open Chrome instances and it really bogs you down.
browser.quit()
