def check_package(package: str) -> bool:
    from importlib_metadata import distribution, PackageNotFoundError

    try:
        distribution(package)
        print(f"'{package}' is installed.")
        return True
    except PackageNotFoundError:
        print(f"'{package}' is not installed.")
        return False


tool_name = "interpreter.python.check_package"
tool_obj = check_package
tool_requirements = ["importlib_metadata"]
