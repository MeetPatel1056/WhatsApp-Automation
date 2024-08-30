from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
import logging

def export_and_clear_chat(group_name, platform_name="Android", platform_version="12.0", device_name="1377597818004X0", app_package="com.whatsapp.w4b", app_activity="com.whatsapp.HomeActivity", command_executor="http://127.0.0.1:4724"):
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Set up options for Appium
    options = UiAutomator2Options()
    options.platform_name = platform_name
    options.platform_version = platform_version
    options.device_name = device_name
    options.app_package = app_package
    options.app_activity = app_activity
    options.no_reset = True
    options.automation_name = "UiAutomator2"

    # Connect to the Appium server
    driver = webdriver.Remote(
        command_executor=command_executor,
        options=options
    )

    wait = WebDriverWait(driver, 30)

    try:
        logging.info(f"Processing group: {group_name}")

        # Locate the WhatsApp icon with notifications (use dynamic content-desc matching)
        whatsapp_icon = wait.until(
            EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "WA Business")))
        whatsapp_icon.click()

        # Search for the group
        search_btn = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID,"Search")))
        search_btn.click()

        search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='com.whatsapp.w4b:id/search_input']")))

        # Add a small delay to ensure the field is ready
        time.sleep(1)

        # Ensure the search input field is focused
        search_input.click()

        # Input the group name into the search bar
        search_input.send_keys(group_name)

        # Tap on the group name in the search results
        group = wait.until(EC.element_to_be_clickable((By.XPATH, f"(//android.widget.RelativeLayout[@resource-id='com.whatsapp.w4b:id/contact_row_container'])[3]")))
        group.click()

        # Tap the three-dot menu (options)
        menu_btn = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "More options")))
        menu_btn.click()

        # Tap 'More'
        more_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='More']")))
        more_option.click()

        # Tap 'Export chat'
        export_chat = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Export chat']"))
        )
        export_chat.click()

        # Assuming no media, select 'Without media'
        #without_media = wait.until(
        #   EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@resource-id='android:id/button3']")))
        #without_media.click()

        # Select Google Drive
        google_drive_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Drive']"))
        )
        google_drive_option.click()

        save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@resource-id='com.google.android.apps.docs:id/save_button']")))
        save_button.click()

        logging.info(f"Chat exported for group: {group_name}")

        # Clear chat history
        menu_btn = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "More options")))
        menu_btn.click()

        # Tap 'More'
        more_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='More']")))
        more_option.click()

        clear_chat = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Clear chat']"))
        )
        clear_chat.click()

        confirm_clear = wait.until(EC.element_to_be_clickable((By.ID, "android:id/button1")))
        confirm_clear.click()

        logging.info(f"Chat cleared for group: {group_name}")

        time.sleep(2)

        # Navigate back to the main screen
        driver.back()
        driver.back()
        time.sleep(2)  # Give it some time before processing the next group

    except Exception as e:
        logging.error(f"An error occurred while processing group '{group_name}': {str(e)}")
        driver.back()  # Navigate back in case of an error

    finally:
        # Quit the driver when done
        driver.quit()


