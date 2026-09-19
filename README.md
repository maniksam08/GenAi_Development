# 🤖 GenAI Development

A collection of small, focused chatbots and AI agents built while learning **LangChain** and applied **Generative AI** — covering retrieval-augmented generation (RAG), SQL-querying agents, web-search agents, and basic conversational bots.

Each script/notebook is a standalone experiment exploring a different GenAI pattern — from plain Q&A to agents that reason over structured data and documents.

---

## ✨ What's Inside

| File | What it does | Key tech |
|---|---|---|
| `QnA_bot.py` | Basic question-answering chatbot | LangChain |
| `Qna_chatbot_groq.py` | Q&A chatbot powered by Groq's LLM inference | LangChain, Groq, Streamlit |
| `RAG_pdf_bot.py` | Retrieval-Augmented Generation bot that answers questions from PDF documents using vector search | LangChain, ChromaDB, Vector Embeddings, Streamlit |
| `SQl_agent.py` | Agent that converts natural language into SQL queries and runs them against a database | LangChain, SQLite |
| `Google_Search_agent.py` / `Google_search_agent.ipynb` | Agent that performs live web/Google search to answer queries | LangChain, Google Search API |
| `Basic_AI_Agent` | A minimal AI agent scaffold — starting point for building tool-using agents | LangChain |

*(Mark which scripts use Streamlit accurately against your code — update the table above to match.)*

---

## 🧠 Concepts Explored

- **RAG (Retrieval-Augmented Generation)** — chunking documents, generating vector embeddings, and retrieving relevant context before generation (`RAG_pdf_bot.py`)
- **SQL Agents** — letting an LLM reason over a database schema and generate/execute SQL from natural language (`SQl_agent.py`)
- **Search Agents** — giving an LLM access to a live search tool so it can answer questions beyond its training data (`Google_Search_agent.py`)
- **Vector Databases** — using ChromaDB to store and query document embeddings for semantic search
- **Fast Inference** — using Groq for low-latency LLM responses

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** LangChain
- **UI:** Streamlit (for interactive bots)
- **Vector Store:** ChromaDB
- **Database:** SQLite
- **LLM Providers:** Groq (and others depending on script)

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.9+
- API keys for the LLM provider(s) used in each script (e.g., Groq, OpenAI, Google Search)

### Installation

```bash
git clone https://github.com/maniksam08/GenAi_Development.git
cd GenAi_Development
pip install -r requirements.txt
```

Streamlit is included in `requirements.txt` if any of your bots use it — otherwise install separately with `pip install streamlit`.

### Running a bot
Each file is a standalone script. Plain scripts run directly:

```bash
python SQl_agent.py
```

Bots with a **Streamlit UI** are launched with the `streamlit run` command instead:

```bash
streamlit run RAG_pdf_bot.py
```

This opens the chatbot in your browser at `http://localhost:8501`.

Set the required API keys as environment variables (or in a `.env` file) before running — e.g. `GROQ_API_KEY`, `GOOGLE_API_KEY`, depending on which bot you're running.

---

## 🚧 Notes

This repo is a learning sandbox for exploring different GenAI/agentic patterns with LangChain — not a single unified application. Each script is intentionally simple and self-contained so the core idea (RAG, SQL agents, search agents, etc.) stays easy to follow. More experiments will be added as I explore further into agentic AI.

Feedback, suggestions, and contributions are welcome.

---

## 📄 License

Open for learning purposes — feel free to fork and experiment.
