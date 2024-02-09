import os
import re
from bs4 import BeautifulSoup


input_folder = r"C:\Users\HP\Documents\all txt" # specify your input directory
output_folder = r"C:\Users\HP\Documents\cleaned txt" # specify your outut directory

os.makedirs(output_folder, exist_ok=True)

# Get a list of all the text files in the input folder
file_names = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

# For each file
for file_name in file_names:
    # Open the file and read its content
    with open(os.path.join(input_folder, file_name), 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove HTML tags
    soup = BeautifulSoup(content, 'html.parser')
    content = soup.get_text()

    # Lowercase the text
    content = content.lower()

    # Remove URLs
    content = re.sub(r'http\S+|www\S+|https\S+', '', content, flags=re.MULTILINE)

    # Remove emojis
    content = content.encode('ascii', 'ignore').decode('ascii')

    # Remove extra whitespaces
    content = re.sub(r'\s+', ' ', content).strip()

    # Save the cleaned data as a new file in the output folder
    with open(os.path.join(output_folder, file_name), 'w', encoding='utf-8') as f:
        f.write(content)
