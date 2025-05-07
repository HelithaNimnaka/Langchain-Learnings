from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
#model = ChatOpenAI(model="gpt-4o")
model = init_chat_model("llama3-8b-8192", model_provider="groq")


# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes."),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()   #StrOutputParser() to get string content.
# chain = prompt_template | model

# Run the chain
result = chain.invoke({"topic": "lawyers", "joke_count": 3})

# Output
print(result)
