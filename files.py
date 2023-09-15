import os
import re

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


# List of directory names
dir_names = ['dir1', 'dir2', 'dir3']

# List of file names
file_names = ['file1.txt', 'file2.txt', 'file3.txt']

# Create directories
for key in data.items():
    # Original Directory Names
    dir_names = key
    # Replace whitespace with underscores
    dir_names = re.sub(r'\s', '_', dir_names)
    # Convert to lowercase
    dir_names = dir_names.lower()
    if not os.path.exists(dir_names):
        os.makedirs(dir_names)

# Create or append to files in each directory
for key in data.items():
    for key,value in data.items():
        # Original Directory Names
        dir_names = key
        # Replace whitespace with underscores
        dir_names = re.sub(r'\s', '_', dir_names)
        # Convert to lowercase
        dir_names = dir_names.lower()
        file_name = f"{dir_names}.md"
        with open(os.path.join(dir_names, file_name), 'a') as f:
            f.write('\n Hello, World!\n')


# Original sentence
sentence = "This is a Test Sentence."
# Replace whitespace with underscores
sentence = re.sub(r'\s', '_', sentence)
# Convert to lowercase
sentence = sentence.lower()
print(sentence)


