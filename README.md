# Square MCP Server

A Model Context Protocol (MCP) server that provides access to Square API functionality.

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Set environment variables:
```bash
# Required
export SQUARE_ACCESS_TOKEN=your_access_token_here

# Optional - defaults to 'sandbox' if not set
export SQUARE_ENVIRONMENT=sandbox  # or 'production' for production environment
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

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `SQUARE_ACCESS_TOKEN` | Yes | - | Your Square API access token |
| `SQUARE_ENVIRONMENT` | No | `sandbox` | Square API environment (`sandbox` or `production`) |
