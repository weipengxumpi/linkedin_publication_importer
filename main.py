#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from copy import copy
import pdfplumber
import re


def add_publication_to_linkedin(publication, driver):
    # Go to LinkedIn "Add publication" page
    driver.get("https://www.linkedin.com/in/me/edit/forms/publication/new/")
    time.sleep(3)
    # Fill in the form (update selectors as needed)
    title_id = "single-line-text-form-component-profileEditFormElement-PUBLICATION-profilePublication-ACoAAApiI-8Bx7MN9RSCPxzi-DggwG-iRpSBhW0-1-name"
    publisher_id="single-line-text-form-component-profileEditFormElement-PUBLICATION-profilePublication-ACoAAApiI-8Bx7MN9RSCPxzi-DggwG-iRpSBhW0-1-publisher"
    date_id = "-profileEditFormElement-PUBLICATION-profilePublication-ACoAAApiI-8Bx7MN9RSCPxzi-DggwG-iRpSBhW0-1-date-date-picker"

    driver.find_element(By.ID, title_id).send_keys(publication['title'])
    driver.find_element(By.ID, publisher_id).send_keys(publication['publisher'])
    driver.find_element(By.ID, date_id).send_keys(publication['date'])
    # Add more fields as needed
    # Submit
    # driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
    wait = WebDriverWait(driver, 2)
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Save']]")))
    save_button.click()
    time.sleep(2)

def extract_publications(pdf_path):
    publications = []
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    # break lines
    lines = text.split("●")

    for line in lines:
        if len(line) > 10:
            publications.append(extract_publication_info(line))
    return publications


def extract_publication_info(line):
    # Remove the bullet if present
    line = line.lstrip('●').strip()
    # Split by comma, but keep author names together
    parts = [p.strip() for p in line.split(',')]
    # The title is the first part
    title = parts[0]
    # The last part is the publisher and date (e.g., 'CVPR 2025')
    publisher_date = parts[-1]
    # Try to split publisher and date
    match = re.match(r'(.+?)\s+(\d{4})$', publisher_date)
    if match:
        publisher = match.group(1)
        date = match.group(2)
    else:
        publisher = publisher_date
        date = ''
    return {
        'title': title,
        'publisher': publisher,
        'date': date
    }

def main():
    """
    Main function that serves as the entry point of the program.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    # replace with your own credentials
    driver.find_element(By.ID, "username").send_keys("donald.trump@gmail.com")
    driver.find_element(By.ID, "password").send_keys("makeamericagreatagain")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # replace with your own pdf path
    # each paper in the pdf should be in the format of 
    # "● title, authors (optional), CVPR 2025"
    # you can also use other separators like "•" or "*", 
    # but make sure to update the code accordingly
    pdf_path = "empty.pdf"
    publications = extract_publications(pdf_path)

    for publication in publications:
        print(publication['title'])
        publication['date'] = '01/01/' + publication['date']
        add_publication_to_linkedin(publication, driver)

if __name__ == "__main__":
    main() 
