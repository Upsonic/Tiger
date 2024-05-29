

def open_url(url) -> bool:
    """

    :param url: str:

    """
    import webbrowser

    try:
        webbrowser.open(url)
        return True
    except:
        return False



tool_name = "browser.open_url"
tool_obj = open_url
tool_requirements = []
