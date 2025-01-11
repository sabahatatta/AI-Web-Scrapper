# Import necessary libraries
import streamlit as st  # Streamlit for creating a user-friendly interface
from scrape import (  # Importing scraping-related functions
    scrape_website,       # Function to scrape a website and retrieve its HTML content
    extract_body_content, # Function to extract the <body> tag content
    clean_body_content,   # Function to clean the extracted body content
    split_dom_content     # Function to split large content into smaller chunks
)
from parse import parse_with_ollama  # Function to process and parse content using the Ollama language model

# Set the title of the Streamlit app
st.title("AI Web Scraper")

# Input field to accept the website URL from the user
url = st.text_input("Enter the URL of the website you want to scrape")

# Button to trigger the scraping process
if st.button("Scrape Site"):
    st.write("Scraping the website")  # Display progress message

    # Step 1: Scrape the website and retrieve the raw HTML content
    result = scrape_website(url)
    
    # Step 2: Extract the <body> content from the scraped HTML
    body_content = extract_body_content(result)
    
    # Step 3: Clean the extracted body content (remove <script>, <style>, etc.)
    cleaned_content = clean_body_content(body_content)

    # Save the cleaned content to the session state for further use
    st.session_state.dom_content = cleaned_content

    # Display the cleaned DOM content in an expandable text area
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", value=cleaned_content, height=500)

# Check if the DOM content is available in the session state
if "dom_content" in st.session_state:
    # Input field to describe what the user wants to parse
    parse_description = st.text_area("Describe what you want to parse?")

    # Button to trigger the parsing process
    if st.button("Parse Content"):
        if parse_description:  # Ensure the user has entered a description
            st.write("Parsing the content..")  # Display progress message

            # Step 4: Split the cleaned DOM content into smaller chunks
            dom_chunks = split_dom_content(st.session_state.dom_content)
            
            # Step 5: Parse the chunks using the Ollama language model
            result = parse_with_ollama(dom_chunks, parse_description)
            
            # Display the parsing result
            st.write(result)
