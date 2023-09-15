# Import necessary packages
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service

# Ignore unnecessary warnings
warnings.simplefilter("ignore")

# Initialize the Chrome driver outside of try block
driver = None

try:
    # Define the URL
    url = "https://dictation.io/speech"

    # Set up Chrome options
    chrome_driver_path = 'D:\\Jarvis\\Brain\\chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')
    service = Service(chrome_driver_path)
    chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Disable UI pop-ups for media access
    chrome_options.add_argument("--use-fake-device-for-media-stream")
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
    chrome_options.add_argument(f'user-agent={user_agent}')
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(url)

    # Wait for the page to load
    sleep(15)

    # Execute JavaScript to enable microphone access
    driver.execute_script('navigator.mediaDevices.getUserMedia({ audio: true })')
    sleep(1)

    # Click the "Clear" button to reset
    clear_button_xpath = '/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[2]/a[8]'
    driver.find_element(by=By.XPATH, value=clear_button_xpath).click()
    sleep(1)

    # Click the start button
    start_button_xpath = "/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[1]/a"
    driver.find_element(by=By.XPATH, value=start_button_xpath).click()
    print("Microphone is turned on")

except Exception as e:
    print("Error: Unable to configure the ChromeDriver properly.")
    print("To resolve this error, make sure to set up the ChromeDriver correctly.")
    print(e)

# Continuous loop for capturing and writing text
while True:
    # Get the text from the dictation interface

    text_element_xpath = '/html/body/div[3]/section/div/div/div[2]/div/div[2]'
    text = driver.find_element(by=By.XPATH, value=text_element_xpath).text

    if len(text) == 0:
        pass

    else:
        # Click the "Clear" button to reset
        driver.find_element(by=By.XPATH, value=clear_button_xpath).click()
        text = text.strip()
        
        # Write the text to a file
        output_file_path = "D:\\Jarvis\\Body\\SpeechRecognition.txt"
        with open(output_file_path, "w") as file_write:
            file_write.write(text)

