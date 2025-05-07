from dotenv import load_dotenv
#Load environment variables from .env
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("llama3-8b-8192", model_provider="groq")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("\nFull result:")
print(result)
print("\nContent only:")
print(result.content)