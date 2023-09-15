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

# Create a dictionary
data = {
    
        "Personal Assistant": "J.A.R.V.I.S. functions as Tony Stark's assistant, running and taking care of all the internal systems of Stark's buildings and the Iron Man suits."
    ,
    
        "Control Iron Man Armor": "J.A.R.V.I.S. controls Tony Stark's Iron Man and Hulkbuster armor."
    ,
    
        "Data Analysis": "J.A.R.V.I.S. provides valuable information during combat, giving advice on the armor's status and on the enemy's weak points."
    ,
    
        "Security": "J.A.R.V.I.S. runs security for Tony Stark's Mansion and Stark Tower."
    ,
    
        "Business Operations": "J.A.R.V.I.S. runs more of the business than anyone besides Pepper Potts."
    ,
    
        "Text Analysis": "It can analyze and understand text inputs²."
    ,
    
        "Image Analysis": "It can interpret images²."
    ,
    
        "Audio Analysis": "It can understand audio inputs²."
    ,
    
        "Video Analysis": "It can interpret videos²."
    ,
    
        "Internet Access": "It can connect to the internet and access files²."
    ,
    
        "Task Planning": "It can plan tasks based on user requests²."
    ,
    
        "Model Selection": "It can select the correct model to achieve a task²."
    ,
    
        "Task Execution": "It can execute tasks using selected models²."
    ,
    
        "Response Generation": "It can generate responses using inference results from all models²."
    ,
    
        "Image Generation": "It can generate images based on user requests²."
    ,
    
        "Poem Writing": "It can write poems based on user requests²."
    ,
    
        "Text Generation": "It can generate text based on user requests²."
    ,
    
        "Audio Generation": "It can generate audio based on user requests²."
    ,
    
        "Video Generation": "It can generate videos based on user requests²."
    ,
    
        "File Access": "It can access files from a given URL². "
    ,
    
        "Pose Interpretation": "It can interpret poses from images²."
    ,
    
        "Drawing Output": "It can draw output based on user requests²."
    ,
    
        "Multimodal Capabilities": "It can handle multiple tasks in a single query²."
    ,
    
        "Collaborative System": "It connects to multiple AI models and responds with a final result²."
    ,
    
        "Personalized AI Assistant Creation": "You can train an AI chatbot and create a personalized AI assistant²."
    ,
    
        "Augmented Reality Security": "E.D.I.T.H. provides augmented reality security"
    ,
    
        "Defense System": "It serves as a defense system"
    ,
    
        "Artificial Tactical Intelligence": "E.D.I.T.H. is capable of providing artificial tactical intelligence"
    ,
    
        "Access to Tony's Protocols": "E.D.I.T.H. has access to all of Tony Stark's protocols"
    ,
    
        "Control of Stark Industries' Global Satellite Network": "E.D.I.T.H. can control Stark Industries' global satellite network  "
    ,
    
        "Drone Control": "E.D.I.T.H. can control an army of weaponized drones "
    ,
    
        "Facial Recognition": "E.D.I.T.H. can perform facial recognition"
    ,
    
        "Real-time Information Retrieval": "It can provide real-time information retrieval"
    ,
    
        "Communication": "E.D.I.T.H. can facilitate communication "
    ,
    
        "Holographic Projection": "It can project holographic images"
    ,
    
        "Personal Assistant": "F.R.I.D.A.Y. functions as Tony Stark's assistant⁵"
    ,
    
        "Control of Iron Man Armor": "F.R.I.D.A.Y. controls Tony Stark's Iron Man and Hulkbuster armor⁵"
    ,
    
        "Business Operations": "F.R.I.D.A.Y. runs more of the business for Stark Industries than anyone besides Pepper Potts⁵"
    ,
    
        "Security": "F.R.I.D.A.Y. is responsible for running security for Tony Stark's Mansion and Stark Tower⁵"
    ,
    
        "Battle Assistance": "F.R.I.D.A.Y. assisted Tony during the Battl`e of Sokovia⁵"
    ,
    
        "Monitoring Ultron": "F.R.I.D.A.Y. monitored Ultron's attempts to escape into the internet⁵"
    ,
    
        "Rescue Operations": "F.R.I.D.A.Y. helped Stark rescue a family trapped in a collapsing building⁵"
    ,
    
        "Predicting Opponent's Moves": "F.R.I.D.A.Y. predicted where Captain America would hit next, allowing Iron Man to counter the blow⁵"
    

}

# Print the keys and values separately
for key, value in data.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")


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


import os

# List of directory names
dir_names = ['dir1', 'dir2', 'dir3']

# List of file names
file_names = ['file1.txt', 'file2.txt', 'file3.txt']

# Create directories
for dir_name in dir_names:
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

# Create or append to files in each directory
for dir_name in dir_names:
    for file_name in file_names:
        with open(os.path.join(dir_name, file_name), 'a') as f:
            f.write('Hello, World!\n')

