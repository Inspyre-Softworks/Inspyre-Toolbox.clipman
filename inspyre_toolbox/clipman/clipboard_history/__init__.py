#  Copyright (c) 2021-2021. __init__.py is a part of the ''inspyre-toolbox.clipman' project by Inspyre Softworks D.O. and is licensed under the MIT License. Feel free to copy, share, distribute any code from this project  as you please. If you do; please share where you got it.
from threading import Thread

import clipboard
from inspyre_toolbox.clipman.config import ARGS, LOG_DEVICE

history = []

listener_running = False


class History(object) :
    
    
    def __init__(self, max_entries: int = 5) :
        self.__list = []
        self.__log_name = 'clipboard_history.History'
        log = LOG_DEVICE.add_child(self.__log_name + '.__init__')
        log.debug('Initialized!')
    
    
    def get(self) :
        """
        
        Return the current history.
        
        Returns:
            history (list): The current history list.
        
        """
        return self.__list
    
    
    def add(self, contents) :
        """
        
        Add the value of the 'contents' variable to the history as an entry.
        
        Parameters:
            contents: The contents of the entry you'd like to add to the clipboard history list.
            
        Returns:
            None
        
        """


def listener(max_hist=5) :
    global history, listener_running
    
    log = LOG_DEVICE.add_child('clipboard_history.listener')
    
    log.debug(f"Starting listener with a max history of: {max_hist}")
    
    cb_now = clipboard.paste()
    
    log.debug(f"Current clipboards contents: {cb_now}")
    
    history.append(cb_now)
    
    log.debug("Setting 'listener_running' to True")
    listener_running = True
    
    log.debug("Starting listener loop")
    while listener_running :
        while True :
            log.debug("Checking history length")
            if len(history) >= (max_hist + 1) :
                log.debug("History length too long, pruning!")
                history.remove(history[0])
                log.debug(f"Pruned! Current length: {len(history)}")
            else :
                log.debug("Checking if current clipboard contents differ from last entry in history.")
                if clipboard.paste() != history[-1] :
                    log.debug("Current clipboard differs from latest entry!")
                    if clipboard.paste() == '' and ARGS.password_manager_mode :
                        log.debug("Password-Manager mode active and received an empty paste, removing last entry.")
                        history.remove(history[-1])
                        log.debug("Last clipboard history item removed.")
                    
                    history.append(clipboard.paste())
                    log.info(f"Added to history! Current history length: {len(history)}")
                    break


# Create an object to access for starting the thread
listener_thread = Thread(target=listener, args=[ARGS.max_entries], daemon=True)
