# linkedin_publication_importer

## LinkedIn Publication Automation Script

This Python script automates the process of adding academic publications to your LinkedIn profile. It extracts publication information from a PDF file and automatically adds them to your LinkedIn profile using Selenium WebDriver.

## Features

- Extracts publication information from a PDF file
- Automatically logs into LinkedIn
- Adds publications to your LinkedIn profile
- Handles multiple publications in batch

## Requirements

- Python 3.x
- Required Python packages:
  - selenium
  - pdfplumber
  - webdriver_manager (for Chrome WebDriver)

## Installation

1. Clone this repository or download the script
2. Install the required packages:
```bash
pip install selenium pdfplumber webdriver_manager
```

## Usage

1. Prepare your PDF file with publications in the following format:
```
● Title of the paper, Authors (optional), Conference/Journal Year
```
For example:
```
● Deep Learning for Computer Vision, John Doe, Jane Smith, CVPR 2023
```

2. Update the following in `main.py`:
   - Your LinkedIn credentials (username and password)
   - Path to your PDF file containing publications

3. Run the script:
```bash
python main.py
```

## Important Notes

- The script uses Selenium WebDriver with Chrome browser
- Make sure you have Chrome browser installed
- The script includes appropriate delays to handle LinkedIn's loading times
- LinkedIn's element IDs may change over time, requiring updates to the selectors
- Use this script responsibly and in accordance with LinkedIn's terms of service
- Consider adding appropriate delays between actions to avoid being flagged as automated behavior

## PDF Format Requirements

Your PDF file should contain publications in the following format:
- Each publication should start with a bullet point (●)
- Format: "● Title, Authors (optional), Conference/Journal Year"
- Example: "● Machine Learning Advances, John Doe, CVPR 2023"

## Security Note

- Never commit your LinkedIn credentials to version control
- Consider using environment variables or a configuration file for sensitive information
- The current implementation has hardcoded credentials for demonstration purposes only

## Disclaimer

This script is provided for educational purposes only. Use it responsibly and in accordance with LinkedIn's terms of service. Automated actions on LinkedIn should be used with caution to avoid account restrictions. 
