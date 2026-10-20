# 🚀 AI Engineering & Autonomous Agents Interactive Portfolio

[![GitHub Pages](https://img.shields.io/badge/Live_Demo-GitHub_Pages-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://eng-ahmed-rifai.github.io/AI-Engineering-Interactive-Portfolio/)
[![Streamlit](https://img.shields.io/badge/Interactive_App-Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://share.streamlit.io/)
[![DeepLearning.AI](https://img.shields.io/badge/DeepLearning.AI-100%25_Verified-FF6F00?style=for-the-badge&logo=deeplearning)](https://www.deeplearning.ai/)
[![LangChain](https://img.shields.io/badge/LangChain-0.2.x-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Cyclic_Multi_Agent-0052CC?style=for-the-badge)](https://langchain-ai.github.io/langgraph/)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Open_Weights-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-34A853.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> **Architect & Engineer:** [Eng. Ahmed Rifai](https://github.com/Eng-Ahmed-Rifai)  
> **Credential Authority:** DeepLearning.AI & Coursera (Completed at 100.00% Grade Perfection)  
> **Repository Purpose:** Master showcase hub featuring interactive web simulators, production multi-agent architectures, and direct links to dedicated individual project repositories.

---

## 🌐 Live Interactive Web Showcase

Experience the entire portfolio directly in your browser without local setup:

👉 **[Launch Interactive Web Simulator (GitHub Pages)](https://eng-ahmed-rifai.github.io/AI-Engineering-Interactive-Portfolio/)**

---

## 📂 Dedicated Project Repositories

Each project has its own standalone repository with production code, Jupyter notebooks, unit tests, and comprehensive architectural documentation:

| # | Project Name | Scope & Technical Architecture | Standalone Repository |
|---|---|---|:---:|
| 1 | **AI Agents in LangGraph** | Stateful multi-agent graphs, `MemorySaver` persistence checkpoints, Human-in-the-Loop review gates, and cyclic reflection. | [View Repository ↗](https://github.com/Eng-Ahmed-Rifai/AI-Agents-in-LangGraph) |
| 2 | **LangChain: Chat with Your Data** | Production RAG pipeline, `RecursiveCharacterTextSplitter`, ChromaDB vector embeddings, and Maximal Marginal Relevance (MMR). | [View Repository ↗](https://github.com/Eng-Ahmed-Rifai/LangChain-Chat-with-Your-Data) |
| 3 | **LangChain: LLM Application Development** | Orchestration primitives, Sequential & Router chains, Pydantic structured output parsing, and conversational memory scaling. | [View Repository ↗](https://github.com/Eng-Ahmed-Rifai/LangChain-LLM-Application-Development) |
| 4 | **Open Source Models with Hugging Face** | Open-weights foundation models, multimodal inference pipelines (Summarization, NLI Zero-Shot, Whisper), and quantization. | [View Repository ↗](https://github.com/Eng-Ahmed-Rifai/Open-Source-Models-with-Hugging-Face) |

---

## 🏗️ Master Architecture: LangGraph Cyclic State Machine

```mermaid
flowchart TD
    subgraph LangGraphEngine ["LangGraph Stateful Reasoning Engine"]
        Start([User Prompt / Task]) --> RouterNode{"Router / Supervisor"}
        
        RouterNode -->|"Needs Retrieval"| ToolNode["Tool Execution Node (Tavily / ChromaDB)"]
        RouterNode -->|"Needs Complex Plan"| PlanNode["Task Planning & Decomposition"]
        RouterNode -->|"Draft Complete"| ReflectionNode["Self-Critique & Rubric Evaluation"]
        
        ToolNode --> StateUpdate["State Checkpoint (MemorySaver)"]
        PlanNode --> StateUpdate
        StateUpdate --> RouterNode
        
        ReflectionNode -->|"Score < 90%"| RevisionNode["Agent Revision Loop"]
        RevisionNode --> RouterNode
        
        ReflectionNode -->|"Critical Tool / Final Draft"| HITLNode{"Human-in-the-Loop Interruption"}
        HITLNode -->|"Approved"| FinalNode([Output Response / Report])
        HITLNode -->|"Feedback Provided"| RevisionNode
    end
```

---

## 🚀 Running the Streamlit Cloud Dashboard Locally

```bash
# Clone the showcase repository
git clone https://github.com/Eng-Ahmed-Rifai/AI-Engineering-Interactive-Portfolio.git
cd AI-Engineering-Interactive-Portfolio

# Create virtual environment & activate
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit application
streamlit run streamlit_app.py
```

---

## 📜 Verified Coursera & DeepLearning.AI Credentials

All 4 specialized laboratory curriculums were officially completed by **Eng. Ahmed Rifai** with **100.00% Grade Perfection**:
- **AI Agents in LangGraph** — DeepLearning.AI (Completed October 21, 2026 | Grade: 100%)
- **LangChain Chat with Your Data** — DeepLearning.AI (Completed October 21, 2026 | Grade: 100%)
- **LangChain for LLM Application Development** — DeepLearning.AI (Completed October 21, 2026 | Grade: 100%)
- **Open Source Models with Hugging Face** — DeepLearning.AI (Completed October 21, 2026 | Grade: 100%)

---

## 📄 License & Attribution
This repository is licensed under the [MIT License](LICENSE).  
*Built with AI Agent assistance.*
