import freeGPT
import sys
import os


project_dir = "C:\\Users\\Mohtasham\\Downloads\\"
sys.path.append(project_dir)


async def askGPT3(query):
    if type(query) is str:
        resp = await getattr(freeGPT, "gpt3").Completion.create(query)
        return resp
    return None


