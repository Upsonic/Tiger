
def search(query:str, max_number:int=20) -> list:
    from duckduckgo_search import DDGS


    return [result["href"] for result in DDGS().text(query, max_results=max_number)]


tool_name = "search.duckduckgo"
tool_obj = search
tool_requirements = ["duckduckgo-search==5.3.0"]