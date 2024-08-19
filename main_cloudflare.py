from dotenv import find_dotenv, load_dotenv
import os
from langchain_community.llms.cloudflare_workersai import CloudflareWorkersAI
from langchain_core.output_parsers import CommaSeparatedListOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

load_dotenv(find_dotenv())

API_BASE_URL = f"{os.getenv("CLOUDFLARE_API_BASE_URL")}/accounts/{os.getenv("CLOUDFLARE_ACCOUNT_ID")}/ai/run/"
headers = {"Authorization": f"Bearer {os.getenv("CLOUDFLARE_API_TOKEN")}"}

model = CloudflareWorkersAI(
    account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID"),
    api_token = os.getenv("CLOUDFLARE_API_TOKEN"),
    model = "@cf/meta/llama-3.1-8b-instruct"
)

csv_parser = CommaSeparatedListOutputParser()
str_parser = StrOutputParser()

system_template = "You are a helpful assistant in {domain}:"
system_message = SystemMessagePromptTemplate.from_template(system_template)

# human_template = "{input_string}\n{format_instructions}"
human_template = "{input_string}"
human_message = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])

chain = chat_prompt | model | str_parser

reply = chain.invoke({
    "domain": "Math",
    "input_string": "Explain Euler's formula to a 10 year old."
})

print(reply)

# import requests
# def run(model, inputs):
#     input = { "messages": inputs }
#     response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
#     return response.json()


# inputs = [
#     { "role": "system", "content": "You are a friendly assistant in physics" },
#     { "role": "user", "content": "Write a short story about Standard Model of particle physics for a 6 year old."}
# ]
# output = run("@cf/meta/llama-3.1-8b-instruct", inputs)
# if output['success']:
#     response = output['result']['response']
#     print(response)
# else:
#     for err in output['errors']:
#         print("Error: {} - {}".format(err['code'], err['message']))
