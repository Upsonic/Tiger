

def google(query:str, max_number:int=20) -> list:
    try:
        from googlesearch import search as gsearch
        return list(gsearch(query, stop=max_number))
    except:
        return "An exception occurred"    



tool_name = "search.google"
tool_obj = google
tool_requirements = ["google==3.0.0"]