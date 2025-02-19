# Square MCP Server

[![smithery badge](https://smithery.ai/badge/@Kvadratni/square-mcp)](https://smithery.ai/server/@Kvadratni/square-mcp)

A Model Context Protocol (MCP) server that provides access to Square API functionality.


## Setup

### Installing via Smithery

To install Square MCP Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@Kvadratni/square-mcp):

```bash
npx -y @smithery/cli install @Kvadratni/square-mcp --client claude
```

### Manual Installation
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
