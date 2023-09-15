# Installing and Importing all these packages 🖤

from time import sleep # Inbuilt
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.options import Options # pip install selenium
from selenium.webdriver.common.by import By # pip install selenium
import warnings # Inbuilt
from selenium.webdriver.chrome.service import Service

# Configuring the webdriver to automate the program for utilizing ChatGPT as a backend model.

warnings.simplefilter("ignore")

try:
    Link = "https://gpt4login.com/use-chatgpt-online-free/"
    chrome_driver_path = 'Brain\\chromedriver.exe'
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(Link)

except Exception as e:
    print("To resolve this error, you should set up the ChromeDriver properly.")
    print("*For the successful execution of this program, it is essential to configure and set up the ChromeDriver.")
    print(e)

# Storing the previous conversation ID for reference.

def FileReader():
        
    try:
        File = open("Brain\\Chatnumber.txt","r")
        Data = File.read()
        File.close()
        return Data

    except Exception as e:
        print(e)

# Reading the previous conversation ID for reference.

def FileWriter(Data):

    try:
        File = open("Brain\\Chatnumber.txt","w")
        File.write(Data)
        File.close()

    except Exception as e:
        print(e)

# Initiating the primary execution phase while utilizing ChatGPT as the backend model.

def ChatGPTBrain(Query):
    Query = str(Query)

    try:
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/div/textarea").send_keys(Query)
        sleep(1)

    except:
        print("*The Input button or Input Section does not appear to be readily accessible or available within the current context or environment.*")
        print("*Consider modifying the path for the 'Input' element, which is available on the website.*")

    try:
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/button/span").click()

    except:
        print("*The Send.Keys() function or button does not appear to be readily accessible or available within the current context or environment.*")
        print("*Consider modifying the path for the 'Send' button, which is available on the website.*")

    try:
        Data = str(FileReader())

    except:
        print("*Could Not Be able to access the file Where Chatnumber is saved for reference.")

    while True:

        sleep(0.5)
        
        try:

            try:
                AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
                Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).is_displayed()
                if str(Answer)=="True":
                    break

            except:
                # print("*The response text element cannot be located. Please ensure that you update its selector or locator.")
                pass

        except:
            pass
    
    try:
        AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
        Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).text

    except:
        print("*The response text element cannot be located. Please ensure that you update its selector or locator.")

    NewData = int(Data) + 2
    FileWriter(Data=str(NewData))
    return Answer

# Commencing the main execution phase.

def MainExecutionChatGPT():

    print("")
    print("Initiating the GPT-4 model.")
    FileWriter(Data='3')

    while True:
            
        try:
            File = open("Body\\SpeechRecognition.txt","r")
            Data = File.read()
            File.close()
            FileHistory = open("Brain\\HistoryChat.txt","r")
            DataHistory = FileHistory.read()
            FileHistory.close()

            if str(Data)==str(DataHistory):
                sleep(0.5)
                pass

            else:
                Result = ChatGPTBrain(Data)
                print(Result)

                FileHistory = open("Brain\\HistoryChat.txt","w")
                FileHistory.write(Data)
                FileHistory.close()

        except Exception as e:
            print(e)
        
MainExecutionChatGPT()
