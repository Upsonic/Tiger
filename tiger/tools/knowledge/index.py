

def index() -> list:
    """ """
    import inspect
    import os

    import upsonic
    from tinydb import Query
    from tinydb import TinyDB


    folder = os.path.join(os.path.dirname(inspect.getfile(upsonic)),
                          "upsonic_tiger_knowledge.json")
    db = TinyDB(folder)
    return [knowledge["knowledge_name"] for knowledge in db.all()]


tool_name = "knowledge.index"
tool_obj = index
tool_requirements = ["tinydb==4.8.0"]
