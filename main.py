from fastmcp import FastMCP
import os
import random
import json


# create the fastMCP server instance
mcp = FastMCP("simple calculator server")

# tools: add numbers
@mcp.tool
def add(a : int, b:int) ->int:
    """
    add two numbers together

    args:
    a:first number
    b:second number

    return:
    the sum of a and b
    
    """
    return a+b


# tool : generate random numbers
@mcp.tool
def random_number(min:int=1, max:int  = 100)->int:
    """generate a random number within the range

    return:
    a random number between min and max
    """

    return random.randint(min,max)


# resource: server information
@mcp.resource("info://server")
def server_info() -> str:
    """get information about hte server"""

    info = {
        "name":"simple calculator server",
        "version":"1.0.0.0.1",
        "description":"basic mcp server with math tool",
        "tools":["add","random_number"],
        "author":"my name is sayan"
    }

    return json.dumps(info, indent=2)


# start the server
if __name__ == "__main__":
    mcp.run(transport="http", host = "0.0.0.0", port=8080)
    #mcp.run()