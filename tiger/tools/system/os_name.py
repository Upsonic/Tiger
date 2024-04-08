import platform

def os_name():
    system_name = platform.system()
    if system_name == 'Windows':
        return 'Windows'
    elif system_name == 'Darwin':
        return 'macOS'
    elif system_name == 'Linux':
        return 'Linux'
    else:
        return 'Unknown OS'


tool_name = "system.os_name"
tool_obj = os_name
tool_requirements = []