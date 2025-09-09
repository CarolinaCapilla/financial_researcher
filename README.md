# FinancialResearcher Crew

Welcome to the FinancialResearcher Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## What this project does

This project uses two collaborating AI agents to research a company and produce a polished market report:

- Researcher: gathers up‑to‑date information about the target company using web search tools.
- Analyst: synthesizes the findings into a structured, reader‑friendly report.

The agents run sequentially, and the final report is saved to `output/report.md`. By default, the target company is `Tesla` (see `src/financial_researcher/main.py`).

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

## Setup

1. Create a `.env` file in the project root and add your API keys:

```
OPENAI_API_KEY=...
GROQ_API_KEY=...
SERPER_API_KEY=...
```

Models/providers are fully customizable per agent via the `llm` field in `src/financial_researcher/config/agents.yaml` using the `provider/model` format (e.g., `openai/gpt-4o-mini`, `groq/llama-3.3-70b-versatile`). Set only the API keys in `.env` for the providers you choose to use.

2. (Optional) Change the default company by editing the `inputs` dict in `src/financial_researcher/main.py`.
### Customizing

**Add your API keys to the `.env` file**

- Modify `src/financial_researcher/config/agents.yaml` to define your agents
- Modify `src/financial_researcher/config/tasks.yaml` to define your tasks
- Modify `src/financial_researcher/crew.py` to add your own logic, tools and specific args
- Modify `src/financial_researcher/main.py` to add custom inputs for your agents and tasks

- Change models/providers per agent by updating the `llm` value in `src/financial_researcher/config/agents.yaml`; ensure the matching API key exists in `.env`.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the financial-researcher Crew, assembling the agents and assigning them tasks as defined in your configuration.
The final report is written to `output/report.md`.

Alternative run methods:

```bash
# Using uv and the provided script entrypoints
uv run run_crew

# Or directly invoke Python
python -m financial_researcher.main
```

## Understanding Your Crew

The financial-researcher Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the FinancialResearcher Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
