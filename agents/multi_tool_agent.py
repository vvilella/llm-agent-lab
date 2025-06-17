from langchain.agents import Tool, initialize_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI



# Simples calculadora
@tool
def calculator(expression: str) -> str:
    """Avalia uma expressão matemática simples."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Erro: {str(e)}"

# Simula uma ferramenta de busca
@tool
def fake_search(query: str) -> str:
    """Simula uma busca online."""
    dados = {
        "capital da Alemanha": "Berlim",
        "presidente do Brasil": "Luiz Inácio Lula da Silva",
    }
    return dados.get(query.lower(), "Não encontrado.")

# LLM base
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Criação do agente
tools = [calculator, fake_search]
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)

# Loop de interação
while True:
    pergunta = input("\nVocê: ")
    if pergunta.lower() in ["sair", "exit"]:
        break
    resposta = agent.run(pergunta)
    print(f"Agente: {resposta}")
