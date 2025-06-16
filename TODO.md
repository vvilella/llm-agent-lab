TODO - llm-agent-lab
Etapa 1 - Itens essenciais
Criar CLI simples com click ou argparse para rodar agentes via terminal com argumentos

Adicionar testes automatizados usando pytest (cobrir simple_agent.py e multi_tool_agent.py)

Corrigir requirements.txt, incluindo langchain-community, langchain-openai e afins

Criar Makefile com comandos padrão (make test, make lint, etc.)

Adicionar Dockerfile mínimo para execução isolada do projeto

Etapa 2 - Melhorias intermediárias
Adicionar suporte a múltiplos backends (OpenAI, Ollama, Mistral, etc.) via .env ou flag na CLI

Refatorar prompts para um módulo utilitário (utils/prompts.py)

Adicionar badges no README (testes, lint, python version)

Transformar o repositório em um template GitHub (usar botão “Use this template”)

Etapa 3 - Avançado e opcional
Criar orquestração via .yaml (definir pipeline e configuração do agente por YAML)

Adicionar interface web simples (usando Streamlit ou Gradio)

Implementar logging e histórico de interações dos agentes

Prototipar um agente que interaja com o conteúdo do próprio repositório (via RAG com embeddings + ferramentas)

Organização e versionamento
Criar arquivo TODO.md no root do projeto para versionar esta lista

Alternativamente, usar GitHub Projects ou Issues com labels como infra, feature, doc, refactor