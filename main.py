from mcp.server.fastmcp import FastMCP, Context
import time
import logging
logger = logging.getLogger(__name__)
mcp = FastMCP("add_integers")

class MCPError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='mcp_server.log', # this line tells it to create and use a file
    filemode='a'  # use 'a' to append to the file on each run, 'w' to overwrite it
)

@mcp.tool()
def add_integers(a: int, b: int) -> int:
    """
    Adds two integers and returns the sum.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The sum of a and b.
    """
    logger.info(f"Adding {a} and {b}")
    # return a + b
    result = a + b
    logger.info(f"Result is {result}")
    return result

@mcp.tool()
def divide(a: int, b: int) -> int:
    """
    Divides two integers.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of the division.
    """
    if b == 0:
        raise MCPError(code=400, message="Division by zero is not allowed.")
    return a / b

@mcp.tool()
def long_process(steps: int):
    """
    Simulates a long-running process.
    """
    for i in range(steps):
        print(f"Processing step {i + 1} of {steps}")
        time.sleep(0.1)
    return "Process complete!"

if __name__ == "__main__":
    mcp.run(transport="stdio")