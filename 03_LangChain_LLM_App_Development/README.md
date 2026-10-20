# ⛓️ LangChain: LLM Application Development

[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![DeepLearning.AI](https://img.shields.io/badge/DeepLearning.AI-100%25_Verified-FF6F00?style=for-the-badge)](https://www.deeplearning.ai/)

## 📖 Theoretical Foundations & Curriculum
This module focuses on the core orchestration building blocks of LangChain: PromptTemplates, OutputParsers, Chains, and Memory management.

### 🌟 Key Design Patterns
1. **Prompt Engineering & Structured Output:**
   - Enforcing JSON and Pydantic schemas using `PydanticOutputParser` and `JsonOutputParser` to ensure deterministic programmatic consumption.
2. **Sequential & Router Chains:**
   - Multi-step pipelines where output from Step $i$ flows into Step $i+1$.
   - Dynamic classification of input prompts to conditionally invoke domain-specific sub-chains.
3. **Conversational Memory Architectures:**
   - `ConversationBufferMemory`: Retains full raw history. Simple, but suffers from linear token inflation.
   - `ConversationBufferWindowMemory`: Retains only the last $K$ turns. Bounded, but suffers from catastrophic forgetting of early setup instructions.
   - `ConversationSummaryMemory`: Incrementally summarizes dialogue turns using a secondary LLM pass, guaranteeing bounded context costs.

---

## 💻 Code Artifacts
- [`conversational_memory.py`](./conversational_memory.py): Production implementation and benchmark of Buffer vs Summary memory.
- [`demo_chains.py`](./demo_chains.py): Interactive demonstration of prompt chaining and memory scaling.
