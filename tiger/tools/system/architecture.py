def architecture():
    import platform

    return platform.architecture()[0]


tool_name = "system.architecture"
tool_obj = architecture
tool_requirements = []
