
def close(app_name) -> bool:
    """

    :param app_name: str:

    """
    try:
        from AppOpener import close
        close(app_name, throw_error=True)
        return True
    except:
        return False



tool_name = "app.close"
tool_obj = close
tool_requirements = ["AppOpener==1.7"]
