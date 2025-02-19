import argparse
from .server import mcp

def main():
    """Square MCP: Square API Model Context Protocol Server."""
    parser = argparse.ArgumentParser(
        description="Provides access to Square API functionality through MCP."
    )
    parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()