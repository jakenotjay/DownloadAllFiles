import requests
from bs4 import BeautifulSoup

# ask user for url in console
url = input("Enter a website to extract the URL's from: ")

file_ending = input("Please enter file type to extract: ")

if url == "" or file_ending == "":
    print("Please enter a valid url and file type")
    exit()

# check file ending begins with .
if file_ending[0] != ".":
    file_ending = "." + file_ending

# Make a request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the links that end with ".pdf"
pdf_links = [link["href"] for link in soup.find_all("a") if link["href"].endswith(file_ending)]

# print how many links were found and ask if user wants to continue
print(f"{len(pdf_links)} links found")
continue_ = input("Do you want to continue? (Y/n): ")

if continue_.lower() == "n":
    exit()

# Download each PDF file and write to data folder
for link in pdf_links:
    # inform user of current link
    print(f"Downloading {link}")

    # check if link is relative and add base url if so
    if link[0] == "/":
        link = url + link

    pdf_response = requests.get(link)
    file_name = link.split("/")[-1]
    file_location = f"data/{file_name}"

    with open(file_location, "wb") as f:
        f.write(pdf_response.content)

    # inform user of download completion
    print(f"Downloaded {file_name}")