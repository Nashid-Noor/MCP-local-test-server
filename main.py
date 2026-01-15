import random
from fastmcp import FastMCP

mcp= FastMCP(name='Demo server')

@mcp.tool
def roll_dice(roll:int=1) -> list[int]:
    return [random.randint(1,6) for _ in range(roll)]

@mcp.tool
def add(a:float, b:float) -> float:
    return a+b

if __name__=="__main__":
    mcp.run()
    