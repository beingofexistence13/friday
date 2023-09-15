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

import csv

# Open the CSV file with utf-8 encoding
with open('readme.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Print each row in the CSV file
    for row in reader:
        print(row)
