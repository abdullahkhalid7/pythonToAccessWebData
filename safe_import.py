def safe_import(module):
    try:
        exec(f'import {module}')
        globals()[module] = eval(module)
    except ModuleNotFoundError as err:
        import os
        os.system(f'pip install {module}')
        exec(f'import {module}')
        globals()[module] =  eval(module)
