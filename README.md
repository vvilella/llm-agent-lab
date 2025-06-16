# LLM Agents Lab

> Practical, well‑documented examples of building LLM‑based agents with Python & LangChain (OpenAI + open‑source back‑ends).

---

## ✨ Why this repo exists

* Executives, architects and developers falam muito sobre *agents* e *AI‑first workflows*, mas falta referência **curta, opinativa e com código**.
* Aqui você encontra **passo a passo real**, sem hype: do Hello‑World até agentes com ferramentas, memória e orquestração.
* Cada exemplo serve de apoio aos posts do [Victor Nardi Vilella](https://www.linkedin.com/in/…): ver, copiar, adaptar e discutir.

---

## 🗺️ Road‑map rápido

| Etapa                                   | Status | Pasta/alvo                     |
| --------------------------------------- | ------ | ------------------------------ |
| **Setup** – venv, key, teste mínimo     | ✅      | `main.py`                      |
| Agente simples (zero‑shot)              | ✅      | `examples/simple_agent.py`     |
| Agente multi‑tool (calculator, search)  | 🔜     | `examples/multi_tool_agent.py` |
| Memória & history                       | 🔜     | `agents/memory_agent.py`       |
| RAG com embeddings + StackSpot AI       | 🔜     | `rag/`                         |
| Orquestração híbrida (OpenAI + Mistral) | 🔜     | `orchestration/`               |

---

## 🖥️ Requisitos rápidos

```bash
Python 3.10+
Poetry (opcional) ou pip + venv
Conta OpenAI (ou outro provider) com chave ativa.
```

---

## ⚙️ Instalação (5 passos)

```bash
# 1 Clone
git clone https://github.com/<seu-usuario>/llm-agent-lab.git
cd llm-agent-lab

# 2 Crie ambiente\python3 -m venv .venv
source .venv/bin/activate

# 3 Instale deps
pip install -r requirements.txt

# 4 Configure a chave
cp .env.example .env
# edite .env e cole sua OPENAI_API_KEY

# 5 Teste
python main.py
```

---

## 🏃 Uso rápido

```bash
python main.py
Pergunte algo ao agente: Quando Roma foi fundada?
Resposta do agente: Roma foi fundada em 21 de abril de 753 a.C.
```

Para uso interativo contínuo, rode:

```bash
python examples/simple_agent.py
```

---

## 🧩 Estrutura de pastas

```
llm-agent-lab/
├── agents/           # Implementações de agentes customizados
│   └── __init__.py
├── examples/         # Scripts de uso rápido / demos
│   └── simple_agent.py
├── utils/            # Helpers (prompt, logging, etc.)
├── tests/            # Pytest (TDD)
├── main.py           # Entrypoint minimalista
├── requirements.txt  # Deps chave
├── .env.example      # Exemplo de env
└── README.md
```

---

## 🔑 Gerenciamento de chaves

* **Nunca** comite `.env` – ele já está no `.gitignore`.
* Para múltiplos providers, crie variáveis como `MISTRAL_API_KEY`, `OPENROUTER_API_KEY` e carregue via `dotenv`.

---

## 🧠 Conceitos rápidos usados aqui

* **Zero‑shot reasoning** – prompt simples, sem exemplo.
* **Tool‑usage** – LangChain "tools" permitem chamar APIs externas.
* **Memory** – guarda histórico para simular contexto longo.
* **RAG** – Retrieval Augmented Generation; busca + geração.

Links de referência em `/docs/links.md`.

---

## 🤝 Contribuindo

1. Fork ➡️ Branch ➡️ PR
2. Siga o estilo Black + Ruff (`make lint`)
3. Adicione testes quando possível.

---

## 📜 Licença

MIT – faça bom uso e cite este repo nos seus projetos! 🙌

---

## 🙏 Agradecimentos & Inspiração

* [LangChain](https://github.com/langchain-ai/langchain)
* [OpenAI Python SDK](https://github.com/openai/openai-python)
