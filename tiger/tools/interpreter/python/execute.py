

def execute(cell:str) -> str:
    try:
        from IPython import get_ipython

        ipython = get_ipython()
        result = ipython.run_cell(cell)
        log = str(result.result)
        if result.error_before_exec is not None:
            log += f"\n{result.error_before_exec}"
        if result.error_in_exec is not None:
            log += f"\n{result.error_in_exec}"
        return log
    except Exception as e:
        return e
        

tool_name = "interpreter.python.execute"
tool_obj = execute
tool_requirements = ["ipython"]
