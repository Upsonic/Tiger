

def python_version():
    import platform

    return platform.python_version()


tool_name = "system.python_version"
tool_obj = python_version
tool_requirements = []