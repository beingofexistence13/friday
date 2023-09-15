

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

# import os
# import json

# # Path to your JSON file
# json_file_path = '/path/to/your/json/file.json'

# # Read the JSON file
# with open(json_file_path, 'r') as f:
#     json_content = json.load(f)

# # Path to your root directory
# base_path = '/'

# for item in json_content:
#     for key, value in item.items():
#         # Create a directory for each key in the root directory
#         dir_path = os.path.join(base_path, key.strip())
#         os.makedirs(dir_path, exist_ok=True)

#         # Create a .md file in each directory
#         file_path = os.path.join(dir_path, f'{key.strip()}.md')
        
#         # Write the value into the .md file
#         with open(file_path, 'a') as f:
#             f.write(value.strip() + '\n')
# import csv

# # Open the CSV file
# with open('readme.csv', 'r') as file:
#     reader = csv.reader(file)

#     # Print each row in the CSV file
#     for row in reader:
#         print(row)

# import csv

# # Open the CSV file with utf-8 encoding
# with open('readme.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)

#     # Print each row in the CSV file
#     for row in reader:
#         print(row)






import csv

# # Open the CSV file with utf-8 encoding
# with open('readme.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     data = list(reader)
    
#     # Print the number of rows
#     print("Number of rows:", len(data))
    
#     # Print the number of columns
#     print("Number of columns:", len(data[0]) if data else 0)
# import pandas as pd

# # Read the CSV file
# df = pd.read_csv('readme.csv')

# # Print the contents of the DataFrame
# print(df.tail)

# import pandas as pd

# # Read the CSV file
# df = pd.read_csv('readme.csv')

# # Print the column names
# print("Columns:")
# print(df.columns.tolist())

# # Print each row
# print("\nRows:")
# for index, row in df.iterrows():
#     print(row.tolist())



# import pandas as pd

# # Read the JSON file
# df = pd.read_json('readme.json')

# # Print the contents of the DataFrame
# print(df)




# import json

# # Open the JSON file
# with open('readme.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# Print the contents of the JSON file
# print(data)

# # Print the keys and values separately
# for key, value in data.items():
#     print(f"Key: {key}")
#     print(f"Value: {value}\n")



# import os

# # List of directory names
# dir_names = ['dir1', 'dir2', 'dir3']

# # List of file names
# file_names = ['file1.txt', 'file2.txt', 'file3.txt']

# # Create directories
# for dir_name in dir_names:
#     os.makedirs(dir_name)

# # Create files in each directory
# for dir_name in dir_names:
#     for file_name in file_names:
#         with open(os.path.join(dir_name, file_name), 'w') as f:
#             f.write('Hello, World!')























