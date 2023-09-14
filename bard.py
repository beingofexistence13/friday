import io 
from bardapi import BardCookies
import datetime
import pyperclip
import pyautogui
import webbrowser
from time import sleep
import  json
import keyboard
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
import os
import uuid
import pyperclip
import pandas as pd
warnings.simplefilter("ignore")
# pip install bardapi datetime

cookie_dict = {
    "__Secure-1PSID":"awjpc78-pBVnngqICnsMnl49b3IifcS23WOl8FjnnyhOKOhumLha7wDR2KkT9o8VJNeYBA.",
    "__Secure-1PSIDTS":"sidts-CjIBSAxbGaMg6qpTVegRSnnQ5Ajjr085UW9B_CP2hRG45ssmD3040Eaz0kmiPITM_LA93RAA",
    "__Secure-1PSIDCC":"APoG2W855-2gQfY7mpjEx7AAmRNC9vAxDBSA5nXwfGTdOdZ1Z5vPNvmrANUKsscGNeuGNpL0"
}
def CookieScrapper():
    webbrowser.open("https://bard.google.com")
    sleep(2)
    pyautogui.click(x=1737, y=50)
    sleep(1)
    pyautogui.click(x=1559, y=75)
    sleep(1)
    keyboard.press_and_release('ctrl + w')

    # # Get data from clipboard
    # data = pyperclip.paste()

    # # Generate a unique filename
    # filename = f'cookies_{uuid.uuid4().hex}.txt'

    # # Create 'database' directory if it doesn't exist
    # if not os.path.exists('database'):
    #     os.makedirs('database')

    # # Create the unique file in the 'database' directory
    # with open(os.path.join('database', filename), 'w') as f:
    #     f.write(data)

    # print(f'Data written to file: {filename}')
    
    # # Get data from clipboard
    # data = pyperclip.paste()

    # # Generate a unique filename
    # filename_csv = f'cookies_{uuid.uuid4().hex}.csv'

    # # Create 'database' directory if it doesn't exist
    # if not os.path.exists('database'):
    #     os.makedirs('database')

    # # Assuming that the clipboard data is tab-separated, read the data into a DataFrame
    # df = pd.read_csv(io.StringIO(data), sep='\t')

    # # Write the DataFrame to a CSV file in the 'database' directory
    # df.to_csv(os.path.join('database', filename_csv), index=False)

    # print(f'Data written to file: {filename_csv}')


    # Get data from clipboard
    data = pyperclip.paste()

    # Generate a unique filename
    filename_json = f'cookies_{uuid.uuid4().hex}.json'

    # Create 'database' directory if it doesn't exist
    if not os.path.exists('database'):
        os.makedirs('database')

    # Create the unique file in the 'database' directory and write data to it
    with open(os.path.join('database', filename_json), 'w') as f:
        # Convert string data to JSON format and write to file
        json.dump(json.loads(data), f)

    print(f'Data written to file: {filename_json}')
    try:
        json_data = json.loads(data)
        pass

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")

    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    SIDValue = next((item for item in json_data if item["name"] == SID), None)
    TSValue = next((item for item in json_data if item["name"] == TS), None)
    CCValue = next((item for item in json_data if item["name"] == CC), None)

    if SIDValue is not None:
        SIDValue = SIDValue["value"]
    else:
        print(f"{SIDValue} not found in the JSON data.")

    if TSValue is not None:
        TSValue = TSValue["value"]
    else:
        print(f"{TSValue} not found in the JSON data.")

    if CCValue is not None:
        CCValue = CCValue["value"]
    else:
        print(f"{CCValue} not found in the JSON data.")

    cookie_dict = {
        "__Secure-1PSID": SIDValue ,
        "__Secure-1PSIDTS": TSValue,
        "__Secure-1PSIDCC": CCValue,
    }
    # print(cookie_data(data, filename=filenamedate))

    return cookie_dict


try:
    bard = BardCookies(cookie_dict=cookie_dict)
except Exception as e:
    cookie_dict = CookieScrapper()
    bard = BardCookies(cookie_dict=cookie_dict)
    print("Yes, there is a cookie error:", str(e),"And Using CookieScrapper!!!")
else:
    print("NO, no no.. there are no errors :) All Set To Your Query")

# Text Modification Function -
def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string

# Main Execution
while True:
    Question = input("Enter Your Query : ")
    RealQuestion = str(Question)
    results = bard.get_answer(RealQuestion)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "database//" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))



