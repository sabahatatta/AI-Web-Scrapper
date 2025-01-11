# AI-Powered Web Scraper

## Overview
This project is an AI-powered web scraper that automates data extraction from dynamic websites using Selenium, Chromedriver, and Streamlit. It integrates a local language model (Ollama) to process and analyze scraped content based on user inputs. The intuitive Streamlit interface makes it easy to scrape, process, and explore data in a user-friendly environment.

## 🌟 Features
- **Automated Web Scraping**: Extracts data from dynamic websites using Selenium and Chromedriver.
- **Dynamic Content Parsing**: Splits scraped DOM content into smaller chunks for efficient processing.
- **AI Integration**: Utilizes Ollama for natural language processing and contextual understanding of the scraped data.
- **Streamlit Dashboard**: Interactive user interface for scraping, content parsing, and viewing results.

## 🛠️ Tech Stack
### Backend
- **Python**: Core programming language for the project.
- **Selenium**: Automates browser interactions for web scraping.
- **BeautifulSoup**: Parses and extracts content from HTML.

### Interface
- **Streamlit**: Provides a web-based, user-friendly interface.

### AI Integration
- **Ollama**: Local language model for analyzing and understanding scraped content.

### Browser Automation
- **Chromedriver**: Ensures compatibility with Google Chrome.

### Environment Management
- **Conda**: Manages dependencies and packages in a virtual environment.

## 📂 Folder Structure
```
├── __pycache__/               # Cached files
├── chromedriver/              # Chromedriver executable and configurations
├── main.py                    # Main Streamlit application
├── parse.py                   # Handles DOM content parsing and chunking
├── scrape.py                  # Core scraping logic using Selenium
├── LICENSE                    # Project license
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
```

## ⚙️ Application Workflow
### 1. Web Scraping
- Enter the target URL in the Streamlit interface.
- Selenium navigates to the website and retrieves its content.
- Captures dynamic content, including JavaScript-rendered elements.

### 2. Content Parsing
- The scraped DOM content is split into manageable chunks.
- The user provides a description of what to extract, and the system parses the content accordingly.

### 3. AI Processing
- Parsed chunks are passed to Ollama for contextual analysis.
- The AI provides summaries or answers based on user queries.

### 4. Streamlit Interface
- View scraping progress, parsed content, and AI-processed results in a user-friendly dashboard.

---

## 🔧 Setup Instructions
### Prerequisites
- **Python 3.10** or later
- **Google Chrome** installed on your system
- **Chromedriver** compatible with your Chrome version
- **Conda** installed for environment management

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/sabahatatta/AI-Web-Scraper.git
   cd AI-Web-Scraper
   ```

2. **Set Up Conda Environment**
   Create and activate the Conda environment:
   ```bash
   conda env create -f conda_env.yml
   conda activate ai-web-scraper
   ```

3. **Install Dependencies**
   Alternatively, install dependencies using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file with the following variables:
   ```plaintext
   CHROMEDRIVER_PATH=/path/to/chromedriver
   ```

5. **Run the App**
   Launch the Streamlit app:
   ```bash
   streamlit run main.py
   ```
   Access the interface at `http://localhost:8501`.

---

## 🛠 Managing ChromeDriver Processes

To ensure ChromeDriver is working correctly and no stale processes are running:

#### **Listing ChromeDriver Processes**
- **Windows**:
  1. Open Command Prompt.
  2. Run:
     ```cmd
     tasklist /FI "IMAGENAME eq chromedriver.exe"
     ```

- **macOS/Linux**:
  1. Open Terminal.
  2. Run:
     ```bash
     ps aux | grep chromedriver
     ```

#### **Terminating ChromeDriver Processes**
- **Windows**:
  ```cmd
  taskkill /F /IM chromedriver.exe
  ```

- **macOS/Linux**:
  ```bash
  pkill chromedriver
  ```

#### **Download ChromeDriver**
1. **Check your Chrome version**:
   - Open Chrome and go to `chrome://settings/help`.

2. **Download ChromeDriver**:
   - Visit [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).
   - Select the version that matches your Chrome browser.

3. **Set the Path**:
   - Place the downloaded ChromeDriver in your PATH or configure its location in the `.env` file:
     ```plaintext
     CHROMEDRIVER_PATH=/path/to/chromedriver
     ```

---

## 🚀 Future Enhancements
- Add support for exporting data in CSV/JSON formats.
- Integrate advanced AI models for richer analysis.
- Implement error handling for failed scraping attempts.
- Improve DOM parsing with customizable rules for specific websites.

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes and push to the branch.
4. Open a pull request.

---

## 📜 License
This project is licensed under the MIT License.

---

Enjoy using the AI-Powered Web Scraper! 🚀 If you have any feedback or suggestions, feel free to let me know.