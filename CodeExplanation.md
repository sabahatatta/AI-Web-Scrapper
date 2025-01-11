You can save the scraped, cleaned, and parsed data to a file for future use. Here's how you can integrate saving functionality into your `main.py` Streamlit app:

---

### **Steps to Save the Data**
1. **Choose File Format**: Decide on a format to save the data. Common options are:
   - **Text file (`.txt`)**: Simple for plain text data.
   - **CSV (`.csv`)**: For tabular data.
   - **JSON (`.json`)**: For structured data.

2. **Streamlit's Download Button**: Use `st.download_button` to allow users to download the data directly from the interface.

---

### **Updated Code with Save Option**
Below is the updated version of your `main.py` file with functionality to save the parsed result:

```python
import streamlit as st
from scrape import (
        scrape_website,
        extract_body_content, 
        clean_body_content, 
        split_dom_content
)
from parse import parse_with_ollama


st.title("AI Web Scraper")
url = st.text_input("Enter the URL of the website you want to scrape")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    # Store cleaned content in the session state
    st.session_state.dom_content = cleaned_content

    # Show DOM content in an expander
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", value=cleaned_content, height=500)

if "dom_content" in st.session_state:
    # Text area for parsing instructions
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content..")

            # Split content and parse it with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)

            # Display parsed result
            st.write(result)

            # Add functionality to save the result
            file_name = "parsed_result.txt"  # You can change this to .json or .csv if needed
            st.download_button(
                label="Download Parsed Result",
                data=result,
                file_name=file_name,
                mime="text/plain"  # MIME type for plain text files
            )
```

---

### **How It Works**
1. **Scrape and Parse Workflow**:
   - The user enters the URL and scrapes the website.
   - Once scraped, the cleaned content is stored in the session state (`st.session_state`).
   - The user describes the parsing goal, and the parsed result is displayed.

2. **Save Functionality**:
   - After parsing, the `st.download_button` is displayed.
   - This button allows users to download the parsed result as a `.txt` file.

---

### **Alternative File Formats**
#### **For JSON File**
Replace the `st.download_button` code with:
```python
import json

# Convert result to JSON (use a dictionary if structured data is required)
result_json = json.dumps({"parsed_result": result})

st.download_button(
    label="Download Parsed Result",
   