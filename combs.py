import os
from bs4 import BeautifulSoup

# Specify your directories
source_dir = input("Enter Directory: ")
target_dir = input("Enter Directory: ")

# Create the target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Loop through all files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith(".html") or filename.endswith(".htm"):
        # Create Beautiful Soup object
        with open(os.path.join(source_dir, filename), "r", encoding='utf-8') as f:
            soup = BeautifulSoup(f, "html.parser")
        
        # Extract text from the HTML
        text = soup.get_text()
        
        # Create a new filename
        new_filename = os.path.splitext(filename)[0] + ".txt"
        
        # Write the text to a new file in the target directory
        with open(os.path.join(target_dir, new_filename), "w", encoding='utf-8') as f:
            f.write(text)
