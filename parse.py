# Import the necessary modules for working with the Ollama LLM and LangChain
from langchain_ollama import OllamaLLM  # For interacting with the Ollama language model
from langchain_core.prompts import ChatPromptTemplate  # For creating structured prompts

# Define the template for guiding the AI's response
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the Ollama language model
# Specify the model version (in this case, "llama3.2") to be used for processing
model = OllamaLLM(model="llama3.2")

# Define the function to parse content using Ollama
def parse_with_ollama(dom_chunks, parse_description):
    """
    Processes DOM content chunks using the Ollama language model to extract specific information
    based on the user's description.

    Args:
        dom_chunks (list of str): A list of chunks of cleaned DOM content.
        parse_description (str): The user's description of the information to extract.

    Returns:
        str: The extracted information from the DOM content as a single concatenated string.
    """
    # Create a prompt chain by combining the template and the model
    prompt = ChatPromptTemplate.from_template(template)  # Create a structured prompt from the template
    chain = prompt | model  # Pipe the prompt into the Ollama model to create the chain

    # Initialize a list to hold the parsed results from each chunk
    parsed_result = []

    # Loop through each chunk of DOM content
    for i, chunk in enumerate(dom_chunks, start=1):
        # Pass the chunk and the parse description to the model through the chain
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        # Print progress information to track which batch is being processed
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        # Append the model's response to the parsed results list
        parsed_result.append(response)

    # Combine all the parsed results into a single string separated by newlines
    return "\n".join(parsed_result)
