import os
import shutil
import re
import requests

def move_jpg_files():
    source = input("Enter the source folder path: ")
    destination = input("Enter the destination folder path: ")
    os.makedirs(destination, exist_ok=True)

    count = 0
    for filename in os.listdir(source):
        if filename.lower().endswith(".jpg"):
            shutil.move(os.path.join(source, filename), os.path.join(destination, filename))
            count += 1
    print(f"{count} .jpg files moved to {destination}.")

def extract_emails():
    input_file = input("Enter the input .txt file name: ")
    output_file = input("Enter the output file name for emails: ")

    with open(input_file, 'r') as file:
        text = file.read()

    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')

    print(f"{len(emails)} email(s) saved to '{output_file}'.")

def scrape_webpage_title():
    url = input("Enter the webpage URL: ")
    output_file = input("Enter the output file name for the title: ")

    try:
        response = requests.get(url)
        html = response.text

        match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        if match:
            title = match.group(1).strip()
            with open(output_file, 'w') as file:
                file.write(title)
            print(f"Title saved to '{output_file}': {title}")
        else:
            print("No title found.")
    except Exception as e:
        print("Error fetching the webpage:", e)

def main():
    while True:
        print("\n=== Python Task Automation Menu ===")
        print("1. Move all .jpg files from one folder to another")
        print("2. Extract emails from a .txt file")
        print("3. Scrape the title of a webpage")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            move_jpg_files()
        elif choice == '2':
            extract_emails()
        elif choice == '3':
            scrape_webpage_title()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1–4.")

if __name__ == "__main__":
    main()
