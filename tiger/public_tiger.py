from upsonic import Tiger_Admin


import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

api_url = os.getenv("API_URL")
access_key = os.getenv("ACCESS_KEY")

tiger_client = Tiger_Admin(api_url, access_key)

import os
import importlib.util


def get_file_dict(directory):
    file_dict = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                spec = importlib.util.spec_from_file_location("", filepath)
                foo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(foo)

                file_dict[filepath] = {
                    "tool_name": foo.tool_name,
                    "tool_obj": foo.tool_obj,  # storing the function's name as string
                    "tool_requirements": foo.tool_requirements,
                }

    return file_dict


directory = os.path.join(os.path.dirname(__file__), "tools")


currently_index = tiger_client.get_all()

for each in get_file_dict(directory).values():
    tool_name = each["tool_name"]
    tool_obj = each["tool_obj"]
    tool_requirements = each["tool_requirements"]

    if tool_name in currently_index:
        currently_index.remove(tool_name)

    tiger_client.set(tool_name, tool_obj)
    tiger_client.clear_requirements(tool_name)
    [
        tiger_client.add_requirement(tool_name, requirement)
        for requirement in tool_requirements
    ]
    print(tool_name)


for each in currently_index:
    tiger_client.delete(each)
