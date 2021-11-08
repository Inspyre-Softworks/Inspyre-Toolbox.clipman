"""Console script for inspyre_toolbox.clipman."""
#  Copyright (c) 2021. cli.py is a part of the ''inspyre-toolbox.clipman' project by Inspyre Softworks D.O. and is licensed under the MIT License. Feel free to copy, share, distribute any code from this project  as you please. If you do; please share where you got it.

import sys

from inspyre_toolbox.clipman.clipboard_history import listener_thread
from inspyre_toolbox.clipman.config import ARGS
from inspyre_toolbox.clipman.gui import run as run_gui


def main() :
    """Console script for inspyre_toolbox.clipman."""
    
    listener_thread.start()
    
    run_gui()
    
    print("Arguments: " + str(ARGS))
    print(
        "Replace this message by putting your code into "
        "inspyre_toolbox.clipman.cli.main"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
