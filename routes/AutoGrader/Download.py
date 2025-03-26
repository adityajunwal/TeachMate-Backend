import gdown
import re
import os

def download_pdf(drive_link, output_path="Test_answersheet.pdf"):
    # Done to filter out non-test oriented PDFs, Currently only accepts 1 file
    if drive_link != "https://drive.google.com/file/d/1afdSIKGLuhpo_r3kSJD3swcoCZ-AAMlp/view?usp=sharing":
        return False

    # Extract File ID using regex
    match = re.search(r"/d/([a-zA-Z0-9_-]+)", drive_link)
    if not match:
        print("Invalid Google Drive link.")
        return False

    file_id = match.group(1)  # Extracted File ID

    # If file exists, remove it
    if os.path.exists(output_path):
        os.remove(output_path)

    # Download the file
    gdown.download(f"https://drive.google.com/uc?export=download&id={file_id}", output_path, quiet=False)
    print(f"Downloaded successfully as {output_path}")
    return output_path


