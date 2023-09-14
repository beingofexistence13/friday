

# def print_cookies(url):
#     chrome_options = Options()
#     chrome_options.headless = True
#     chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     driver = webdriver.Chrome(options=chrome_options)
#     chrome_options.add_argument('--log-level=3')
#     driver.maximize_window()
#     driver.get(url)
#     # Get all the cookies of the website
#     cookies = driver.get_cookies()
    
#     # Print each cookie
#     for cookie in cookies:
#         print(f'Name: {cookie["name"]}, Value: {cookie["value"]}')

# url = 'https://bard.google.com'  # replace with your url
# print_cookies(url)

# def print_cookies(url):
#     response = requests.get(url)
#     cookies = response.cookies
#     print(response.cookies)

#     for cookie in cookies:
#         print(f'Name: {cookie.name}, Value: {cookie.value}')
#         print("hello")

# url = 'https://bard.google.com'  # replace with your url
# print_cookies(url)

# import requests

# def get_cookies(url):
#     response = requests.get(url)
#     return response.cookies

# url = 'https://bard.google.com'  # replace with your url
# cookies = get_cookies(url)
# for cookie in cookies:
#     # print(f'Name: {cookie.name}, Value: {cookie.value}')
#     print(cookie.name)
# print(get_cookies(url))

    # def cookie_data(data, filename):
    #     # paragraphs = data.split('\n\n')
    #     with open(filename, 'w') as file:
    #         file.write(data)
    #     # data = paragraphs[:2]
    #     # separator = ', '
    #     # joined_string = separator.join(data)
    #     # return joined_string
