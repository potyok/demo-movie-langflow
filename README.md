# Demo for using Langflow with a custom MCP server

This project includes a sample implementation for integrating your own MCP server with Langflow.

## Setup

Clone the repository to get the implementation of a custom MCP server that handles operations related to movies and screenings.

### Setup Langflow

The installation steps of Langflow can be found on this [website](https://docs.langflow.org/get-started-installation).

### Setup MCP server

Run this command in the root folder of the project:

```bash
pip install -r requirements.txt
```

Then navigate into the `src` folder and start the MCP server with:

```bash
python main.py
```

Once the MCP server has started, the following message should appear on the console:

```bash
INFO:     Started server process [...]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

## Connect Langflow with the MCP server

After Langflow is started, you have to set the details of the MCP server in the `Settings/MCP servers`.

<img src="imgs/setup_mcp.png" alt="Setup MCP"/>

Then create a simple agent flow and add an `MCP tools` component to it:

<img src="imgs/simple_flow.png" alt="Add MCP tool"/>

You can find the exported flow in the `data` folder.
