A complete explanation of the code, broken down into sections:

---

### **1. `scrape.py` File: Scraping the Website**

This file contains the functions to scrape a website, extract its `<body>` content, clean it, and split it into chunks.

```python
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
```

#### **Imports:**
- `selenium.webdriver` and `selenium.webdriver.chrome.service.Service`: These are used to automate browser interactions via Chromedriver.
- `time`: Used to introduce delays (e.g., for waiting for content to load).
- `BeautifulSoup`: Used for parsing and processing the HTML content.

---

#### **Function: `scrape_website(website)`**
```python
def scrape_website(website):
    print("Launching Chrome browser")
    
    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver= webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Website loaded")
        html = driver.page_source
        time.sleep(10)

        return html
    
    finally:
        driver.quit()
        print("Chrome browser closed")
```

**Explanation:**
- **Purpose:** This function launches a browser session, navigates to a given website, retrieves its HTML content, and ensures the browser is properly closed after the operation.
- **Steps:**
  1. A Chrome browser instance is started using Selenium and Chromedriver.
  2. The `driver.get(website)` method opens the specified URL.
  3. The page source (`driver.page_source`) is retrieved, representing the website's HTML.
  4. The browser session is closed (`driver.quit()`) in a `finally` block to free resources, ensuring it always executes.

---

#### **Function: `extract_body_content(html_content)`**
```python
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content =soup.body
    if body_content:
        return str(body_content)
    return "No body content found"
```

**Explanation:**
- **Purpose:** Extracts the `<body>` section of the HTML content for processing.
- **Steps:**
  1. `BeautifulSoup` parses the HTML (`html_content`).
  2. The `<body>` tag is accessed via `soup.body`.
  3. If the `<body>` tag exists, its content is returned as a string; otherwise, a message is returned.

---

#### **Function: `clean_body_content(body_content)`**
```python
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip() 
    )

    return cleaned_content
```

**Explanation:**
- **Purpose:** Cleans the extracted `<body>` content by removing unnecessary elements like `<script>` and `<style>` and extracts readable text.
- **Steps:**
  1. `BeautifulSoup` processes the body content.
  2. All `<script>` and `<style>` tags are removed using `extract()`.
  3. Remaining text is cleaned, with blank lines removed and each line stripped of leading/trailing whitespace.

---

#### **Function: `split_dom_content(dom_content, max_length=6000)`**
```python
def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[ i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]
```

**Explanation:**
- **Purpose:** Splits long text content into smaller chunks for easier processing (e.g., sending to an AI model).
- **Steps:**
  1. The function takes the cleaned content (`dom_content`) and splits it into chunks, each of `max_length` characters.
  2. This ensures that processing large text content is manageable.

---

### **2. `parse.py` File: Parsing the Content with AI**

This file contains the logic for parsing the website's cleaned content using the Ollama language model.

---

#### **Imports**
```python
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
```
- `OllamaLLM`: Interface for interacting with the Ollama AI model.
- `ChatPromptTemplate`: Allows you to structure a prompt to provide clear instructions to the AI.

---

#### **Template for AI**
```python
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)
```

**Explanation:**
- **Purpose:** The template ensures that the AI processes the content based on precise instructions.
- **Key Rules:**
  1. Only extract information matching the user's description.
  2. Do not include unnecessary comments or extra content.
  3. If no match is found, return an empty string.
  4. Ensure responses are concise and focused.

---

#### **Function: `parse_with_ollama(dom_chunks, parse_description)`**
```python
def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_result = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_result.append(response)

    return "\n".join(parsed_result)
```

**Explanation:**
- **Purpose:** Processes the DOM content in chunks using the AI model and extracts information based on the user's instructions.
- **Steps:**
  1. A prompt is created using the template.
  2. The prompt is piped to the `OllamaLLM` model to create a processing chain.
  3. Each chunk is sent to the model along with the parse description.
  4. The AI’s response for each chunk is collected and combined into a single result.

---

### **3. `main.py` File: Streamlit Interface**

This file provides the user interface and ties together the scraping and parsing logic.

---

#### **Imports**
```python
import streamlit as st
from scrape import (
        scrape_website,
        extract_body_content, 
        clean_body_content, 
        split_dom_content
)
from parse import parse_with_ollama
```

**Explanation:**
- Import Streamlit for the UI and the functions from `scrape.py` and `parse.py`.

---

#### **Streamlit UI Logic**
```python
st.title("AI Web Scraper")
url = st.text_input("Enter the URL of the website you want to scrape")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", value=cleaned_content, height=500)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content..")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
```

**Explanation:**
1. **Scraping**:
   - User inputs a URL.
   - The website is scraped, and its cleaned content is stored in the session state.

2. **Parsing**:
   - User provides a description of what to extract.
   - Content is parsed using the AI and results are displayed.
