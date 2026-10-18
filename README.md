# LangGraph Tutorial

A collection of Jupyter notebooks that introduce LangGraph through small, runnable examples. The repository includes basic state graphs, branching and parallel workflows, prompt chaining, and LLM-powered applications using Groq.

## Contents

| Notebook | What it demonstrates |
| --- | --- |
| `0_test_installation.ipynb` | Checks that LangGraph can be imported. |
| `1_bmi_workflow.ipynb` | Calculates BMI and assigns a weight category through sequential graph nodes. |
| `2_simple_llm_workflow.ipynb` | Sends a question to a Groq chat model from a LangGraph workflow. |
| `basic_chatbot.ipynb` | Runs a terminal-style chat loop with message state and in-memory conversation checkpoints. |
| `simulating_a_workflowcrash_and_identifying_it_using_persistence.ipynb` | Simulates an interrupted workflow, inspects and resumes from checkpoints, and demonstrates updating state to create a new checkpoint. |
| `batsman_workflow.ipynb` | Calculates cricket batting statistics in parallel and combines them into a summary. |
| `Quadratic_Equation.ipynb` | Builds an equation, calculates its discriminant, and routes to the appropriate root calculation. |
| `prompt_chaining.ipynb` | Generates a blog outline and then uses it to write a post. |
| `LLM_based_review_workflow.ipynb` | Classifies a product review and routes positive or negative reviews to different responses. |
| `8_X_Postgenerator.ipynb` | Generates, evaluates, and iteratively improves short social-media posts. |
| `UPSC_essay_workflow.ipynb` | Evaluates an essay on multiple criteria in parallel and aggregates feedback and scores. |

The notebooks are independent examples; run the cells in a notebook from top to bottom. `check_nb_concat.py`, `check_nb_syntax.py`, `debug_graph.py`, and `show_cell.py` are helper scripts, not tutorial entry points.

## Requirements

- Python 3.10 or newer
- Jupyter Notebook or JupyterLab
- A Groq API key for the LLM-powered notebooks

There is no pinned dependency file in this repository. Install the packages used by the notebooks with:

```bash
python -m pip install langgraph langchain-core langchain-groq python-dotenv pydantic httpx jupyter
```

## Setup

1. Clone the repository and enter its directory:

   ```bash
   git clone https://github.com/Juggernaut576/Langgraph-Tutorial.git
   cd Langgraph-Tutorial
   ```

2. (Recommended) Create and activate a virtual environment:

   **Windows PowerShell**

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS or Linux**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install langgraph langchain-core langchain-groq python-dotenv pydantic httpx jupyter
   ```

4. Configure Groq credentials. Create a file named `.env` in the repository root:

   ```dotenv
   GROQ_API_KEY=your_groq_api_key
   ```

   `GROQ_MODEL` is optional and is used by `UPSC_essay_workflow.ipynb`; its default is `openai/gpt-oss-20b`. Other notebooks specify their model in the notebook code. Keep real API keys private; `.env` is ignored by Git.

   Alternatively, set the key in the current terminal session:

   **Windows PowerShell**

   ```powershell
   $env:GROQ_API_KEY = "your_groq_api_key"
   ```

   **macOS or Linux**

   ```bash
   export GROQ_API_KEY="your_groq_api_key"
   ```

5. Start Jupyter from the repository root so the notebooks can find `.env`:

   ```bash
   jupyter lab
   ```

   You can also use `jupyter notebook`. Open a notebook and run its cells in order.

## Notebook notes

- The examples in `0_test_installation.ipynb`, `1_bmi_workflow.ipynb`, `batsman_workflow.ipynb`, and `Quadratic_Equation.ipynb` do not call an LLM and do not need a Groq key.
- The LLM examples need a valid Groq API key, internet access, and model IDs that are available to your Groq account. Models are selected in the notebook cells; update those IDs if a provider retires or changes a model.
- `basic_chatbot.ipynb` reads `.env` from the repository root and uses an in-memory checkpointer. Its conversation is not saved after the kernel stops. The interactive cell accepts `exit`, `quit`, or `bye` to end the loop.
- `simulating_a_workflowcrash_and_identifying_it_using_persistence.ipynb` uses an `InMemorySaver` and thread ID `"1"` to demonstrate checkpointing. Interrupt the initial run during the 30-second pause in `step2`, inspect the thread's current state and history, then resume it by invoking the graph with `None` and the same thread ID. The final cells show how to retrieve a specific checkpoint and use `update_state` to create a new checkpoint with `input` changed to `"samosa"` while retaining the original checkpoint. Checkpoints are held in memory and are lost when the Python kernel stops; checkpoint IDs are generated at runtime, so use IDs from the current history output.
- `8_X_Postgenerator.ipynb` uses structured output for tweet evaluation and loops through improvement attempts up to its configured iteration limit.
- `UPSC_essay_workflow.ipynb` also reads `GROQ_MODEL` from the environment if set; otherwise it selects its default model.

## Troubleshooting

**`ModuleNotFoundError` for LangGraph, LangChain, or Jupyter**

Install the missing package in the same Python environment selected as the notebook kernel. If needed, select the virtual environment created during setup as the Jupyter kernel.

**Groq reports that an API key is missing**

Confirm that `.env` is in the repository root, that it contains `GROQ_API_KEY=...`, and that Jupyter was started from that directory. You can also set `GROQ_API_KEY` in the environment before starting Jupyter.

**Groq rejects a model name or request**

Check that the model ID in the notebook is currently supported by Groq and that your account has access to it. The model names in educational examples may need updating over time.

## References

- [LangGraph documentation](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangChain documentation](https://python.langchain.com/docs/introduction/)
- [Groq API documentation](https://console.groq.com/docs)
