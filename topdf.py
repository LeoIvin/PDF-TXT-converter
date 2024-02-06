import os
from pdfdocument.document import PDFDocument

# Get the source and target directories from the user
source_dir = input("Enter the source directory: ")
target_dir = input("Enter the target directory: ")

# Create the target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Loop through all files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith(".txt"):
        # Open the text file
        with open(os.path.join(source_dir, filename), "r", encoding='utf-8') as file:
            # Read the text
            text = file.read()
        
        # Create a new filename
        new_filename = os.path.splitext(filename)[0] + ".pdf"
        
        # Create a PDF document
        pdf = PDFDocument(os.path.join(target_dir, new_filename))
        pdf.init_report()
        pdf.h2('Text File Content')
        pdf.p(text)
        pdf.generate()
