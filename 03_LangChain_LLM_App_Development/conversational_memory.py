"""
Comparative Analysis & Implementation of Conversational Memory Types
Author: Ahmed Mohamed Abdullatif Rifai
Credential: DeepLearning.AI & Coursera (100.00% Verified)
"""

from typing import List, Dict

class ConversationBufferMemory:
    """Stores full raw dialogue history verbatim."""
    def __init__(self):
        self.history: List[Dict[str, str]] = []

    def save_context(self, user_input: str, ai_output: str):
        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "assistant", "content": ai_output})

    def load_memory_variables(self) -> str:
        return "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in self.history])

    def estimate_tokens(self) -> int:
        text = self.load_memory_variables()
        return len(text.split()) * 2

class ConversationSummaryMemory:
    """Incrementally compresses conversation history into a running semantic summary."""
    def __init__(self):
        self.running_summary: str = ""
        self.turn_count: int = 0

    def save_context(self, user_input: str, ai_output: str):
        self.turn_count += 1
        # Simulated incremental summarization
        if not self.running_summary:
            self.running_summary = f"User inquired about {user_input[:40]} and assistant explained core principles."
        else:
            self.running_summary += f" Dialogue continued on {user_input[:30]}."

    def load_memory_variables(self) -> str:
        return f"Current Dialogue Summary: {self.running_summary}"

    def estimate_tokens(self) -> int:
        text = self.load_memory_variables()
        return len(text.split()) * 2

def run_memory_benchmark(turns: int = 5):
    buffer_mem = ConversationBufferMemory()
    summary_mem = ConversationSummaryMemory()

    sample_dialogues = [
        ("How does LangChain manage state across multi-turn sessions?", "LangChain provides memory abstractions that serialize history into string or message formats."),
        ("What are the tradeoffs of ConversationBufferMemory?", "BufferMemory maintains 100% fidelity but token consumption scales linearly O(N) with dialogue length."),
        ("Explain ConversationSummaryMemory.", "SummaryMemory leverages an auxiliary LLM prompt to compress past messages into an evolving state."),
        ("Which one is better for 50-turn customer service chatbots?", "SummaryMemory or WindowMemory is strictly required to prevent token budget exhaustion."),
        ("Can we combine both approaches?", "Yes, ConversationSummaryBufferMemory keeps recent messages in raw buffer and flushes older ones into summary.")
    ]

    print(f"{'Turn':<6} | {'Buffer Memory Tokens':<22} | {'Summary Memory Tokens':<22}")
    print("-" * 55)

    for i in range(min(turns, len(sample_dialogues))):
        user_msg, ai_msg = sample_dialogues[i]
        buffer_mem.save_context(user_msg, ai_msg)
        summary_mem.save_context(user_msg, ai_msg)
        print(f"#{i+1:<5} | {buffer_mem.estimate_tokens():<22} | {summary_mem.estimate_tokens():<22}")

if __name__ == "__main__":
    run_memory_benchmark()
