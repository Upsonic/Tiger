def open(app_name) -> bool:
    """

    :param app_name: str:

    """
    try:
        from AppOpener import open

        open(app_name, throw_error=True)
        return True
    except:
        return False


tool_name = "app.open"
tool_obj = open
tool_requirements = ["AppOpener==1.7"]
