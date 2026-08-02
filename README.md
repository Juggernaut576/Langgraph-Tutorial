# Langgraph Tutorial

A collection of Jupyter notebooks demonstrating LangGraph workflows for building AI applications with Large Language Models (LLMs).

## Project Structure

```
├── 0_test_installation.ipynb     # Verify LangGraph and dependencies are installed
├── 1_bmi_workflow.ipynb          # Simple BMI calculation workflow
├── 2_simple_llm_workflow.ipynb   # LLM-based Q&A workflow using state graphs
├── prompt_chaining.ipynb         # Multi-step prompt chaining (outline → blog post)
└── README.md                     # This file
```

## Overview

This tutorial covers:
- **LangGraph Basics**: Creating state graphs and nodes
- **LLM Integration**: Connecting to LLM providers (Groq, OpenAI, etc.)
- **Workflow Design**: Building multi-step AI pipelines
- **State Management**: Using TypedDict for workflow state

## Prerequisites

- Python 3.8+
- pip or conda
- API key for an LLM provider (Groq, OpenAI, etc.)

## Setup

1. **Clone or download this repository:**
   ```bash
   git clone https://github.com/Juggernaut576/Langgraph-Tutorial.git
   cd Langgraph-Tutorial
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install langgraph langchain langchain-groq python-dotenv jupyter
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root (do NOT commit this):
     ```
     GROQ_API_KEY=your_groq_api_key_here
     GROQ_MODEL=groq-1
     ```
   - Or export in your terminal (PowerShell example):
     ```powershell
     $env:GROQ_API_KEY="your_groq_api_key_here"
     ```

5. **Start Jupyter:**
   ```bash
   jupyter notebook
   # or
   jupyter lab
   ```

## Notebooks

### 0_test_installation.ipynb
Verifies that LangGraph and required dependencies are correctly installed.

### 1_bmi_workflow.ipynb
Demonstrates a simple workflow for calculating BMI using LangGraph state graphs.

### 2_simple_llm_workflow.ipynb
Builds a Q&A workflow that:
- Accepts a question from state
- Calls an LLM (Groq) to generate an answer
- Returns the answer in the updated state

**Usage:**
```python
initial_state = LLMState(question="What is the capital of France?")
final_state = workflow.invoke(initial_state)
print(final_state)
```

### prompt_chaining.ipynb
Demonstrates prompt chaining with multiple nodes:
1. **Create_outline**: Generates an outline from a blog title
2. **Create_blog_post**: Generates a full blog post using the outline

**Usage:**
```python
initial_state = BlogState(title="Your Blog Topic")
final_state = workflow.invoke(initial_state)
```

## Configuration

To use a different LLM provider:
- **Groq**: Already integrated (set `GROQ_API_KEY`)
- **OpenAI**: Replace imports with `from langchain_openai import ChatOpenAI`
- **Gemini**: Use `from langchain_google_vertexai import ChatVertexAI`

## Important Security Notes

⚠️ **Never commit API keys to version control!**
- Use `.env` files (included in `.gitignore`)
- Use environment variables
- GitHub push protection will block secret detection

## Troubleshooting

**ImportError: No module named 'langgraph'**
```bash
pip install langgraph
```

**API Key not found**
Ensure your `.env` file is in the project root and contains:
```
GROQ_API_KEY=your_key_here
```

**Jupyter not found**
```bash
pip install jupyter
```

## Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Groq API Documentation](https://console.groq.com)
- [LangChain Documentation](https://python.langchain.com/)

## License

MIT License - Feel free to use and modify for educational purposes.

---

**Created:** August 2, 2026  
**Last Updated:** August 2, 2026

