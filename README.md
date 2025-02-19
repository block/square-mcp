# Square MCP Server

A Model Context Protocol (MCP) server that provides access to Square API functionality.

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Set environment variables:
```bash
export SQUARE_ACCESS_TOKEN=your_access_token_here
```

3. Run the server:
```bash
uv pip install .
square-mcp
```

Or for development:
```bash
source .venv/bin/activate
mcp dev src/square_mcp/server.py
```
