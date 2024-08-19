from dotenv import find_dotenv, load_dotenv
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import CommaSeparatedListOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

load_dotenv(find_dotenv())

model = AzureChatOpenAI(
    openai_api_type="azure",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY")
)

csv_parser = CommaSeparatedListOutputParser()
str_parser = StrOutputParser()

# By conparision, this block is less flexible, but more direct
# from langchain_core.messages import HumanMessage, SystemMessage
# messages = [
#     SystemMessage(content="You are a helpful assistant in translation from English to German."),
#     HumanMessage(content="Such a lovely weather today! Let's go out!")
# ]

system_template = "You are a helpful assistant in {domain}:"
system_message = SystemMessagePromptTemplate.from_template(system_template)

# human_template = "{input_string}\n{format_instructions}"
human_template = "{input_string}"
human_message = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])

chain = chat_prompt | model | str_parser

reply = chain.invoke({
    "domain": "Physics",
    "input_string": "Write a short story about Standard Model of particle physics for a 6 year old."
})

print(reply)

