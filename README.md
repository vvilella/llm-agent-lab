# LLM Agents Lab

> Exemplos práticos, testáveis e bem organizados de agentes LLM com Python & LangChain (OpenAI e outros backends open‑source).

![CI](https://github.com/vvilella/llm-agent-lab/actions/workflows/ci.yml/badge.svg)

---

## ✨ Por que esse repositório existe?

- Todo mundo fala de *LLM agents* e *AI‑first workflows*, mas faltam exemplos **concretos, didáticos e opinativos** com código.
- Aqui você encontra **implementações reais**, passo a passo, com foco técnico e aplicável.
- Cada exemplo complementa os conteúdos publicados por [Victor Nardi Vilella](https://www.linkedin.com/in/…), com base para discussão, aprendizado e experimentação.

---

## 🗺️ Roadmap rápido

| Etapa                                   | Status | Pasta/alvo                     |
| --------------------------------------- | ------ | ------------------------------ |
| **Setup** – venv, chave, teste mínimo   | ✅     | `main.py`                      |
| Agente simples (zero‑shot)              | ✅     | `examples/simple_agent.py`     |
| Agente multi‑tool (calculator, search)  | 🔜     | `examples/multi_tool_agent.py` |
| Memória & histórico de contexto         | ✅     | `agents/memory_agent.py`       |
| RAG com embeddings + StackSpot AI       | 🔜     | `rag/`                         |
| Orquestração híbrida (OpenAI + Mistral) | 🔜     | `orchestration/`               |

---

## 🖥️ Requisitos rápidos

```bash
Python 3.10+
Poetry (opcional) ou pip + venv
Conta OpenAI (ou outro provider) com chave ativa.
```

---

## ⚙️ Instalação local

```bash
# 1. Clone o repositório
git clone https://github.com/vvilella/llm-agent-lab.git
cd llm-agent-lab

# 2. Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instale as dependências principais
pip install -r requirements.txt

# 4. Adicione suas chaves de API
cp .env.example .env
# edite o arquivo .env com sua OPENAI_API_KEY

# 5. (Opcional) Instale extras para testes e lint
pip install pytest ruff
```

---

## 🏃 Uso rápido

### ➤ Testar um agente básico (sem memória)

```bash
python examples/simple_agent.py
```

### ➤ Usar um agente com **memória de interações**

```bash
python agents/memory_agent.py
```

> O agente manterá um histórico interno da conversa. Experimente:
> 
> `Você: Quem descobriu o Brasil?`  
> `Você: E quantos anos faz isso?`

---

## 🧠 Componentes principais

- **Memory** → Guarda o histórico das últimas interações (em memória).
- **LangChain + OpenAI** → Interface para LLMs (com suporte futuro a Mistral e OpenRouter).
- **Tools** → (Em breve) Integração com ferramentas externas via agentes multi-step.
- **Prompt contextual** → Geração adaptativa de resposta com base no histórico da conversa.

---

## 🧪 Testes & Lint

```bash
# Rodar testes unitários
pytest

# Rodar lint com ruff
ruff .
```

---

## 🧩 Estrutura de pastas

```
llm-agent-lab/
├── agents/           # Agentes com mais lógica (ex: memória, multi-tool)
│   └── memory_agent.py
├── examples/         # Scripts simples e diretos
│   └── simple_agent.py
├── utils/            # Módulos auxiliares (ex: memória, prompts)
│   └── memory.py
├── tests/            # Testes automatizados
│   └── test_memory.py
├── main.py           # Entrypoint mínimo para hello-world
├── .env.example      # Exemplo de configuração
├── requirements.txt  # Dependências principais
├── README.md         # Este documento
└── .github/
    └── workflows/
        └── ci.yml    # Pipeline GitHub Actions
```

---

## 🔐 Gerenciamento de chaves

- Nunca comite `.env` — ele já está no `.gitignore`.
- Para múltiplos providers, use:
  - `OPENAI_API_KEY`
  - `MISTRAL_API_KEY`
  - `OPENROUTER_API_KEY`

Todas são carregadas via `dotenv`.

---

## 📚 Referências & Glossário

- **Zero‑shot reasoning** → Prompt simples, sem exemplos.
- **Tool usage** → Agente que chama APIs e ferramentas externas.
- **Memory agent** → Agente que usa histórico para manter contexto.
- **RAG** → Retrieval-Augmented Generation (busca antes de gerar).
- Links extras em `/docs/links.md`.

---

## 🤝 Contribuindo

1. Fork ➡️ Branch ➡️ Pull Request.
2. Use Black + Ruff para formatação.
3. Adicione testes quando possível.
4. Ideias são bem-vindas nas Issues!

---

## 📜 Licença

MIT – use, compartilhe e cite! 🙌

---

## 🙏 Agradecimentos & Inspiração

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangChain OpenAI](https://github.com/langchain-ai/langchain-openai)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
