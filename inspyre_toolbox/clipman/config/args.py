#  Copyright (c) 2021-2021. args.py is a part of the ''inspyre-toolbox.clipman' project by Inspyre Softworks D.O. and is licensed under the MIT License. Feel free to copy, share, distribute any code from this project  as you please. If you do; please share where you got it.
#
# Feel free to copy, share, distribute any code from this
# project as you please. If you do; please share where
# you got it.
from argparse import ArgumentParser

from inspy_logger import LEVELS as LOG_LEVELS
from inspyre_toolbox.clipman import __version__


class ArgsParse(ArgumentParser) :
    
    
    def __init__(self, prog, description) :
        """
        
        Initialize the ArgsParse class.
        
        Parameters:
            prog (str): The name of the program. This is for the ArgumentParser class initialization.
            description (str): A description of what the program does.
            
        Attributes:
            NoneType
        
        """
        super(ArgsParse, self).__init__(prog=prog, description=description)
        
        self.add_argument(
                '-l',
                '--log-level',
                action='store',
                choices=LOG_LEVELS,
                help=f'The level at which you would like {prog} to output log messages',
                default='info'
                )
        
        self.add_argument(
                '-M',
                '--max-entries',
                action='store',
                help="The number of entries that should be kept in the clipboard history.",
                default=5,
                type=int
                )
        
        self.add_argument(
                '-p',
                '--password-manager-mode',
                action='store_true',
                default=False,
                required=False,
                help='Activate password-manager mode. (When "" is copied to the clipboard (empty entry) the program '
                     'removes the last entry from history.'
                )
        
        self.add_argument(
                '-V',
                '--version',
                action='version',
                version=f"{prog} v{__version__}"
                )
