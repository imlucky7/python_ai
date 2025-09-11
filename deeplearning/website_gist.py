from bs4 import BeautifulSoup
import requests
from IPython.display import HTML, display
from perplexity_client import PerplexityClient
from chatgpt_client import ChatGPTClient

# The url from one of the Batch's newsletter
url = 'https://www.deeplearning.ai/the-batch/the-world-needs-more-intelligence/'

# Getting the content from the webpage's contents
response = requests.get(url)

# Print the response from the requests
#print(response)

# Using beautifulsoup to extract the text
soup = BeautifulSoup(response.text, 'html.parser')
# Find all the text in paragraph elements on the webpage
all_text = soup.find_all('p')

# Create an empty string to store the extracted text
combined_text = ""

# Iterate over 'all_text' and add to the combined_text string
for text in all_text:
    combined_text = combined_text + "\n" + text.get_text()

# Print the final combined text
#print(combined_text)

prompt = f"""Extract the key bullet points from the following text.

Text:
{combined_text}
"""
'''
px = PerplexityClient()
response = px.ask(prompt)
print(response)
'''

gptClient = ChatGPTClient()
response = gptClient.ask(prompt)
print(response)

print("\nStreaming a poem about AI:\n")
for chunk in gptClient.stream("Write a poem about AI."):
    print(chunk, end="")
