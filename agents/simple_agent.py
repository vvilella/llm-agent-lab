from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Inicializa o modelo LLM com temperatura moderada
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

print("Digite sua pergunta (ou 'sair' para encerrar):\n")

# Loop interativo
while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando agente. Até mais!")
        break
    resposta = llm.invoke(pergunta)
    print("Agente:", resposta.content)
