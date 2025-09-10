# FinancialResearcher Crew

An intelligent financial research assistant powered by collaborating AI agents. It performs company research, generates structured market reports, and outputs results as Markdown. Built on crewAI for a clean multi‑agent architecture.

## 🚀 Features

- **AI‑Powered Company Research**: Plans and executes research on a target company
- **Multi‑Agent Architecture**: Separate agents for researching and analysis/writing
- **Configurable Models/Providers**: Choose models per agent via `llm` in `agents.yaml`
- **CLI & UV Integration**: Run with `crewai run`, `uv run run_crew`, or Python module
- **Structured Output**: Saves a polished report to `output/report.md`
- **Modular Design**: Easy to extend with tools, tasks, and new agents

## 🏗️ Architecture

The system consists of two specialized AI agents orchestrated by crewAI:

- **Researcher Agent**: Gathers up‑to‑date information about the target company using web search tools (Serper).
- **Analyst Agent**: Synthesizes findings into a clear, structured report.
- **Crew Orchestrator**: Runs agents sequentially as defined in `tasks.yaml`.

By default, the target company is `Tesla` (see `src/financial_researcher/main.py`). The final report is written to `output/report.md`.

## 📋 Prerequisites

- Python 3.10–3.13
- API keys for the providers you choose:
  - `OPENAI_API_KEY` (if using OpenAI models)
  - `GROQ_API_KEY` (if using Groq models)
  - `SERPER_API_KEY` (for web search)
- Optional: `uv` for fast, reproducible installs

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/financial-researcher.git
   cd financial-researcher
   ```

2. **Install dependencies**
   - With uv (recommended):
   ```bash
   pip install uv
   uv sync
   ```
   - Or with pip:
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=...
   GROQ_API_KEY=...
   SERPER_API_KEY=...
   ```

   Models/providers are customizable per agent via the `llm` field in `src/financial_researcher/config/agents.yaml` using the `provider/model` format (e.g., `openai/gpt-4o-mini`, `groq/llama-3.3-70b-versatile`). Provide only the API keys for the providers you choose to use.

## 🚀 Usage

### Run from the CLI

```bash
crewai run
```

Alternative run methods:

```bash
# Using uv and the provided script entrypoints
uv run run_crew

# Or directly invoke Python
python -m financial_researcher.main
```

### Programmatic usage

```python
from financial_researcher.crew import FinancialResearcher

inputs = {"company": "Tesla"}
result = FinancialResearcher().crew().kickoff(inputs=inputs)
print(result.raw)
```

## 📁 Project Structure

```
financial_researcher/
├── knowledge/
│   └── user_preference.txt
├── output/
│   └── report.md            # Generated report output
├── src/
│   └── financial_researcher/
│       ├── config/
│       │   ├── agents.yaml  # Agents and their models/providers
│       │   └── tasks.yaml   # Task definitions and output path
│       ├── crew.py          # Crew/agents/tasks wiring
│       ├── main.py          # Entrypoints and default inputs
│       └── tools/
│           └── custom_tool.py
├── pyproject.toml           # Dependencies and scripts (uv compatible)
├── uv.lock                  # uv lockfile
└── README.md
```

## 🔧 Configuration

### Agent configuration

- Edit `src/financial_researcher/config/agents.yaml` and set each agent's `llm` as `provider/model`.
- Ensure the corresponding provider API key is present in `.env`.

### Task configuration

- Edit `src/financial_researcher/config/tasks.yaml` to adjust task descriptions, context, and `output_file` location.

### Environment

- Add only the API keys you intend to use in `.env`: `OPENAI_API_KEY`, `GROQ_API_KEY`, `SERPER_API_KEY`.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m "Add amazing feature"`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 🐛 Troubleshooting

### Common issues

1. **Missing/invalid API keys**: Verify your `.env` contains the correct keys for the providers you selected.
2. **Model/provider mismatch**: Ensure `llm` is in `provider/model` form and the provider's key exists.
3. **Serper tool errors**: Confirm `SERPER_API_KEY` is set and valid.
4. **CLI not found**: Use `uv run run_crew` or `python -m financial_researcher.main` if `crewai` CLI isn’t on PATH.
5. **uv not found**: `pip install uv`, then `uv sync`.

## 🔄 Future Enhancements

- [ ] Add CLI flags to pass `company` and output path at runtime
- [ ] Offer a simple web UI with streaming outputs

## 📞 Support

If you encounter issues or have questions, please open an issue in this repository with details and steps to reproduce.
