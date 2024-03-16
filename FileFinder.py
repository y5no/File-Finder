import os

def search_files(keyword):
    any_file_found = False
    keyword = keyword.lower()
    for root, dirs, files in os.walk(os.path.sep):
        for file in files:
            if keyword.lower() in file.lower():
                file_path = os.path.join(root, file)
                print(f"File '{file}' found at: {file_path}")
                any_file_found = True
    if not any_file_found:
        print(f"No file containing '{keyword}' found")

if __name__ == "__main__":
    while True:
        print("\n=== Yunos File Finder ===")
        keyword = input("Enter File to Look For: ")

        if keyword.lower() == 'exit':
            break

        search_files(keyword)
