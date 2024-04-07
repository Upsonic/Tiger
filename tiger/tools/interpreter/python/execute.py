from IPython import get_ipython


def execute(cell:str) -> str:
    ipython = get_ipython()
    result = ipython.run_cell(cell)
    log = str(result.result)
    if result.error_before_exec is not None:
        log += f"\n{result.error_before_exec}"
    if result.error_in_exec is not None:
        log += f"\n{result.error_in_exec}"
    return log

tool_name = "interpreter.python.execute"
tool_obj = execute
tool_requirements = ["IPython"]