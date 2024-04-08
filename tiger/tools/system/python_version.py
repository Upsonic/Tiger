import platform


def python_version():
    return platform.python_version()


tool_name = "system.python_version"
tool_obj = python_version
tool_requirements = []