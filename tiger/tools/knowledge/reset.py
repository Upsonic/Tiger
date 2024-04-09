import inspect
import os

import upsonic
from tinydb import Query, TinyDB


def reset() -> None:
    folder = os.path.join(
        os.path.dirname(inspect.getfile(upsonic)), "upsonic_tiger_knowledge.json"
    )
    db = TinyDB(folder)
    try:
        # Empty the database
        db.truncate()
    except:
        print("Error occurred while resetting the knowledge database.")


tool_name = "knowledge.reset"
tool_obj = reset
tool_requirements = ["tinydb==4.8.0"]
