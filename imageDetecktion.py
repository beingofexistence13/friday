# pip install bardapi datetime
from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID":"awjpc78-pBVnngqICnsMnl49b3IifcS23WOl8FjnnyhOKOhumLha7wDR2KkT9o8VJNeYBA.",
    "__Secure-1PSIDTS":"sidts-CjIBSAxbGaMg6qpTVegRSnnQ5Ajjr085UW9B_CP2hRG45ssmD3040Eaz0kmiPITM_LA93RAA",
    "__Secure-1PSIDCC":"APoG2W855-2gQfY7mpjEx7AAmRNC9vAxDBSA5nXwfGTdOdZ1Z5vPNvmrANUKsscGNeuGNpL0"
}

bard = BardCookies(cookie_dict=cookie_dict)


# Text Modification Function -
def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string

# Image Detection
while True:
    imagename = str(input("Enter Your Image Path : "))
    image = open(imagename,'rb').read()
    bard = BardCookies(cookie_dict=cookie_dict)
    results = bard.ask_about_image('what is in the image?',image=image)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "database//" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))


