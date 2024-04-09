from tinydb import TinyDB, Query
import inspect
import os
import upsonic


def pull(knowledge_name: str) -> str:
    folder = os.path.join(os.path.dirname(
        inspect.getfile(upsonic)),  "upsonic_tiger_knowledge.json")
    db = TinyDB(folder)
    Knowledge = Query()
    result = db.search(Knowledge.knowledge_name == knowledge_name)
    if result:
        return result[0]['description']
    else:
        return None


tool_name = "knowledge.pull"
tool_obj = pull
tool_requirements = ["tinydb==4.8.0"]
