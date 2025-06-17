# utils/memory.py

class Memory:
    def __init__(self):
        self.history = []

    def add(self, user_input: str, agent_response: str):
        self.history.append({
            "user": user_input,
            "agent": agent_response
        })

    def get_last(self, n=5) -> str:
        context = self.history[-n:]
        return "\n".join(
            f"Usuário: {item['user']}\nAgente: {item['agent']}"
            for item in context
        )
