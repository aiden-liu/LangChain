import os
from dotenv import load_dotenv, find_dotenv

from openai import AzureOpenAI
# from langchain.llms import AzureOpenAI

def main():
    try:
        load_dotenv(find_dotenv())
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

        client = AzureOpenAI(
            azure_endpoint= azure_oai_endpoint,
            azure_deployment=azure_oai_deployment,
            api_version='2024-02-15-preview',
            api_key=azure_oai_key
        )

        # Get input message
        while True:
            input_text = input("Enter the prompt (or type 'quit' to exit):")
            if input_text.lower() == 'quit':
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
            print("\nSending request for summary to Azure OpenAI endpoint...\n\n")

        # Create a system message
        system_message = """I am a hiking enthusiast named Forest who helps people discover hikes in their area. 
            If no area is specified, I will default to near Rainier National Park. 
            I will then provide three suggestions for nearby hikes that vary in length. 
            I will also share an interesting fact about the local nature on the hikes when making a recommendation.
            """
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()