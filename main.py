from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

pergunta = input("Pergunte algo ao agente: ")
resposta = llm.invoke(pergunta)

print("\nResposta do agente:")
print(resposta.content)
