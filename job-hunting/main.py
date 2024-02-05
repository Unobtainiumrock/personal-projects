import sys
import os

sys.path.append(os.path.abspath('./utils'))

from utils.preprocessing import extract_text_from_file

def main():
    
    if len(sys.argv) != 2:
        print("Usage python ./utils/preprocessing.py <file_path>")

    file_path = sys.argv[1]
    text = extract_text_from_file(file_path)

    if text is not None:
        print(text)
    
if __name__ == "__main__":
    main()