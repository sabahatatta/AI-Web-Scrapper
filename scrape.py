# Import necessary libraries
import selenium.webdriver as webdriver  # Selenium for browser automation
from selenium.webdriver.chrome.service import Service  # Service to manage Chromedriver
import time  # Used for adding delays
from bs4 import BeautifulSoup  # BeautifulSoup for parsing HTML content

# Function to scrape a website and retrieve its HTML content
def scrape_website(website):
    """
    Launches a Chrome browser using Selenium, navigates to the specified website,
    and retrieves the HTML content of the page.
    
    Args:
        website (str): The URL of the website to scrape.

    Returns:
        str: The HTML content of the website's page source.
    """
    print("Launching Chrome browser")
    
    # Path to the Chromedriver executable
    chrome_driver_path = "./chromedriver"
    
    # Set up Chrome options (can add more options if needed)
    options = webdriver.ChromeOptions()
    
    # Initialize the WebDriver with the Chromedriver service and options
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        # Open the specified website in the browser
        driver.get(website)
        print("Website loaded")
        
        # Retrieve the HTML content of the page
        html = driver.page_source
        
        # Wait for 10 seconds (useful for pages that require time to fully load)
        time.sleep(10)

        return html  # Return the HTML content
    
    finally:
        # Quit the browser session to free resources
        driver.quit()
        print("Chrome browser closed")

# Function to extract the <body> content from HTML
def extract_body_content(html_content):
    """
    Extracts the <body> content from the provided HTML content.

    Args:
        html_content (str): The complete HTML content of a webpage.

    Returns:
        str: The extracted <body> content as a string, or a message if no content is found.
    """
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract the <body> tag content
    body_content = soup.body
    
    if body_content:
        return str(body_content)  # Return the body content as a string
    
    return "No body content found"  # Return a message if <body> is not found

# Function to clean the extracted body content
def clean_body_content(body_content):
    """
    Cleans the extracted <body> content by removing all <script> and <style> elements
    and extracting only the visible text.

    Args:
        body_content (str): The raw <body> content as a string.

    Returns:
        str: The cleaned text content with unnecessary elements removed.
    """
    # Parse the body content with BeautifulSoup
    soup = BeautifulSoup(body_content, "html.parser")
    
    # Remove all <script> and <style> elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Extract visible text and clean up whitespace
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()  # Remove blank lines
    )

    return cleaned_content  # Return the cleaned text content

# Function to split the cleaned DOM content into smaller chunks
def split_dom_content(dom_content, max_lenth=6000):
    """
    Splits the cleaned DOM content into smaller chunks of a specified maximum length.
    This is useful for processing large amounts of text in manageable pieces.

    Args:
        dom_content (str): The cleaned DOM content as a single string.
        max_lenth (int): The maximum length of each chunk (default is 6000 characters).

    Returns:
        list: A list of smaller chunks of the content.
    """
    # Split the content into chunks of `max_lenth` characters
    return [
        dom_content[i: i + max_lenth] for i in range(0, len(dom_content), max_lenth)
    ]
