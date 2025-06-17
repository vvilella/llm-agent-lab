import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.memory import Memory

def test_memory_add_and_retrieve():
    mem = Memory()
    mem.add("Qual seu nome?", "Sou um agente.")
    result = mem.get_last(1)
    assert "Qual seu nome?" in result
    assert "Sou um agente." in result
