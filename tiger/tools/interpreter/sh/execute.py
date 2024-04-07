from subprocess import Popen, PIPE


def execute(script:str) -> str:
    process = Popen(script, stdout=PIPE, shell=True, stderr=PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()
    log = stdout
    if stderr:
        log += f"\n{stderr}"
    return log


tool_name = "interpreter.sh.execute"
tool_obj = execute
tool_requirements = []