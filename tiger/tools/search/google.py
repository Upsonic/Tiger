from googlesearch import search as gsearch

def google(query:str, max_number:int=20) -> list:
    return list(gsearch(query, stop=max_number))


tool_name = "search.google"
tool_obj = google
tool_requirements = ["google==3.0.0"]