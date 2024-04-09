from tinydb import TinyDB, Query
import inspect
import os
import upsonic


def delete(knowledge_name: str) -> bool:
    folder = os.path.join(os.path.dirname(
        inspect.getfile(upsonic)), "upsonic_tiger_knowledge.json")
    db = TinyDB(folder)
    try:
        Knowledge = Query()
        db.remove(Knowledge.knowledge_name == knowledge_name)
        return True
    except:
        return False


tool_name = "knowledge.delete"
tool_obj = delete
tool_requirements = ["tinydb==4.8.0"]
