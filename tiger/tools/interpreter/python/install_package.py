from subprocess import check_call
from importlib_metadata import distribution


def install_package(package:str) -> bool:
    try:
        check_call(["pip", "install", package])
        distribution(package)
        print(f"'{package}' has been successfully installed.")
        return True
    except Exception as e:
        print(f"An error occurred while installing '{package}': ", e)
        return False


tool_name = "interpreter.python.install_package"
tool_obj = install_package
tool_requirements = ["importlib_metadata"]