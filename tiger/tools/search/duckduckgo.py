from duckduckgo_search import DDGS


def search(query: str, max_number: int = 20) -> list:
    """

    :param query: str: 
    :param max_number: int:  (Default value = 20)

    """
    return [result["href"] for result in DDGS().text(query, max_results=max_number)]


tool_name = "system.duckduckgo"
tool_obj = search
tool_requirements = ["duckduckgo-search==5.3.0"]
