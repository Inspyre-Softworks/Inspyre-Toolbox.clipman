#  Copyright (c) 2021. __init__.py is a part of the ''inspyre-toolbox.clipman' project by Inspyre Softworks D.O. and is licensed under the MIT License. Feel free to copy, share, distribute any code from this project  as you please. If you do; please share where you got it.

from pathlib import Path

from inspy_logger import InspyLogger
from inspyre_toolbox.clipman import __summary__ as DESC
from inspyre_toolbox.clipman.config.args import ArgsParse

PROG = 'InspyreToolbox::Clipman'

DEV_LOCK = Path("~/.cache/Inspyre-Softworks/Clipman/dev.lock").expanduser()

arg_parser = ArgsParse(
        prog=PROG,
        description=DESC
        )

DEV_UNLOCK = DEV_LOCK.exists()

if DEV_UNLOCK :
    arg_parser.add_argument(
            '-D',
            '--dev-mode',
            action='store_true',
            default=False,
            help='Activate program in dev-mode.',
            )

ARGS = arg_parser.parse_args()

if DEV_UNLOCK and ARGS.dev_mode:
    ARGS.log_level = 'debug'

ISL = InspyLogger(PROG, ARGS.log_level)

ROOT_LOGGER = ISL.device.start()

LOG_DEVICE = ISL.device

print(ISL.device.l_lvl)
