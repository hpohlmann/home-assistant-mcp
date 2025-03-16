from mcp.server.fastmcp import FastMCP
from app.config import validate_config
from app.tools import init_tools

# Initialize FastMCP server
mcp = FastMCP("home-assistant")

# Initialize the tools with the FastMCP instance
init_tools(mcp)

if __name__ == "__main__":
    # Validate configuration
    try:
        validate_config()
    except ValueError as e:
        print(f"Configuration error: {str(e)}")
        exit(1)
        
    # Initialize and run the server using stdio transport
    mcp.run(transport='stdio') 