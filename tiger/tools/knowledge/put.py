from tinydb import TinyDB, Query
import inspect
import os
import upsonic


def put(knowledge_name:str, description:str) -> bool:
    folder = os.path.join(os.path.dirname(inspect.getfile(upsonic)),  "upsonic_tiger_knowledge.json")
    db = TinyDB(folder)
    try:
        Knowledge = Query()
        if db.search(Knowledge.knowledge_name == knowledge_name):
            db.update({'description': description}, Knowledge.knowledge_name == knowledge_name)
        else:
            db.insert({'knowledge_name': knowledge_name, 'description': description})
        return True
    except:
        return False


tool_name = "knowledge.put"
tool_obj = put
tool_requirements = ["tinydb==4.8.0"]