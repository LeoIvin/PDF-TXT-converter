import os
from PyPDF2 import PdfReader

# Specify the directories
source_dir = r"C:\Users\HP\Documents\all html"
target_dir = r"C:\Users\HP\Documents\all pdf"

# Create the target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Loop through all files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith(".pdf"):
        # Open the PDF file
        with open(os.path.join(source_dir, filename), "rb") as file:
            # Create a PDF file reader object
            pdf_reader = PdfReader(file)
            
            # Initialize an empty string to hold the text
            text = ""
            
            # Loop through all the pages and extract the text
            for page in pdf_reader.pages:
                text += page.extract_text()
        
        # Create a new filename
        new_filename = os.path.splitext(filename)[0] + ".txt"
        
        # Write the text to a new file in the target directory
        with open(os.path.join(target_dir, new_filename), "w", encoding='utf-8') as f:
            f.write(text)
print("Successful!")