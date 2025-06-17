import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.memory import Memory
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

memory = Memory()

def build_prompt(user_input: str) -> str:
    context = memory.get_last()
    return f"{context}\nUsuário: {user_input}\nAgente:"

def main():
    print("🧠 Memory Agent iniciado. Digite 'sair' para encerrar.")
    while True:
        user_input = input("\nVocê: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            break

        prompt = build_prompt(user_input)
        response = llm([HumanMessage(content=prompt)]).content

        print(f"Agente: {response}")
        memory.add(user_input, response)

if __name__ == "__main__":
    main()
