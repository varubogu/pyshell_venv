#! /usr/bin/env python3
import asyncio
import argparse
import os
import sys
import logging
import pyshell_venv_async as psv

#------------------------------------------------------------------------------
# example.py
#------------------------------------------------------------------------------
#
# Try executing it as follows:
#
#   python3 example.py
#   python3 example.py --env-name my_venv
#

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(stream_handler)

file_handler = logging.FileHandler("pyshell_venv_example.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

parser = argparse.ArgumentParser()
parser.add_argument("--env_name", type=str, default="")
parser.add_argument("--local_project_dir", type=str, default="")
args = parser.parse_args()



async def main():
    l = f"""
--------------------------------
pyshell_venv example
--------------------------------
sys.base_prefix: {sys.base_prefix}
sys.prefix: {sys.prefix}
sys.executable: {sys.executable}
os.name: {os.name}
current_process_id: {os.getpid()}
sys.argv: {sys.argv}
is_async: True
is_in_venv: {await psv.is_in_venv()}
--------------------------------
"""
    logger.info(l)
    is_in_venv = await psv.is_in_venv()
    logger.info(f"is_in_venv: {is_in_venv}")
    if not is_in_venv:
        require_package = "numpy"
        if "env_name" in args:
            result: int = await psv.execute(
                require_package_text=require_package,
                env_name=args.env_name
            )
        else:
            result: int = await psv.execute(
                require_package_text=require_package
            )
        sys.exit(result)

    # This code runs in a virtual environment.
    import numpy as np
    ary = np.array([1, 2, 3])
    logger.info(ary)
    sys.exit(0)




if __name__ == "__main__":
    asyncio.run(main())
