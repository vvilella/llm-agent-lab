# 🧠 Walkthrough técnico: Agente com múltiplas ferramentas

Este exemplo usa um agente LangChain com duas ferramentas:
- `calculator`: executa expressões matemáticas.
- `fake_search`: simula uma ferramenta de busca (com respostas vazias, como teste).

---

## 🔧 Código-fonte analisado: `multi_tool_agent.py`

### 1. Inicialização

```python
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
tools = [calculator, fake_search]
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)
```

> **Comentário**: O agente é inicializado no modo `zero-shot-react-description`, que o instrui a **"pensar em voz alta"** com base apenas na descrição das ferramentas. Isso ativa um comportamento reflexivo e exploratório.

---

## 🧪 Teste interativo: sessão real

### Prompt 1: **"Quanto é 23 * 4?"**

```txt
Thought: I should use the calculator tool to multiply 23 by 4.
Action: calculator
Action Input: "23 * 4"
Observation: 92
Final Answer: 92
```

> ✅ **Correto**. O agente identificou que é uma conta e usou a ferramenta certa sem rodeios.

---

### Prompt 2: **"Qual é a capital da Alemanha?"**

```txt
Thought: I should use the fake_search tool to find the answer.
Action: fake_search → Observation: Não encontrado.
(repetido em várias variações linguísticas)
Action: calculator (2 + 2) → Observation: 4
Final Answer: Berlin
```

> 🧠 **Interessante**:
- Ele **tentou múltiplas buscas** com variações linguísticas: português, inglês e alemão.
- Mesmo com **respostas vazias**, ele continuou tentando.
- Usou até `calculator` como fallback (!).
- Finalmente, **"chutou com confiança"** – e acertou.

---

## 🤯 Por que ele acertou mesmo com as ferramentas falhando?

- O modelo `gpt-3.5-turbo` **tem conhecimento treinado**: mesmo sem a ferramenta, pode inferir a resposta.
- O agente **"finge" que está raciocinando via ferramentas**, mas é o LLM que decide como continuar.
- Esse tipo de fallback **é comum em agents zero-shot** quando ferramentas não ajudam.

---

## 🧃 Lições tiradas

| Situação | Comportamento | Insight |
|---------|----------------|--------|
| Pergunta factual | tentou search (simulado) | mesmo falhando, persistiu |
| Falhas contínuas | tentou outras línguas | LLM explora variações |
| Falha total | tentou calculator (!?) | improvisação estranha |
| Resposta final correta | sem evidência externa | conhecimento embutido no modelo |

---

## 🛠️ Melhorias possíveis

- Trocar `fake_search` por `SerpAPI`, `Tavily` ou `GoogleCustomSearch`.
- Usar `ReAct-style agents` com LangGraph para rastrear contexto e evitar loops inúteis.
- Adicionar logging e memória para ver como ele melhora ao longo do tempo.

---

## 📌 Conclusão

Este exemplo mostra como mesmo um agente simples consegue:

- Interpretar perguntas,
- Usar ferramentas específicas,
- Lidar com falhas e improvisar,
- Acertar por conhecimento prévio.

> Um ótimo primeiro passo antes de incluir memória, RAG e agentes com múltiplos modos de decisão.