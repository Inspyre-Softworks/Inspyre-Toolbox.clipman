#  Copyright (c) 2021-2021. __init__.py is a part of the ''inspyre-toolbox.clipman' project by Inspyre Softworks D.O. and is licensed under the MIT License. Feel free to copy, share, distribute any code from this project  as you please. If you do; please share where you got it.
from inspyre_toolbox.clipman.config import LOG_DEVICE
from PySimpleGUI import PopupOKCancel


def confirm_action(question: str, action: str = None):
    """
    Produce a popup that confirms some action with the end-user.
    
    Parameters:
        question (str): The question the pop-up should ask the user.
                        (Ex: 'Do you really want to clear clipboard history?', Required)
                        
        action (str): The action that the resulting popup window is supposed to be confirming, for placing in the
                      popup window title. The title begins with 'Confirm '.
                      
                      (Ex: 'history clear' (this would make the title of the popup 'Confirm history clear'),
                      Optional (defaults to; '')
                      
    Returns:
         bool(True): Returned if the user confirmed the action via the produced popup.
         
         bool(False): Returned if the user did not confirm the action via the produced popup.
    
    """
    log = LOG_DEVICE.add_child('gui.windows.popups.confirm_action')
    log.debug("Started confirm_action function to produce a popup confirming an action")
    if action is None :
        action = ''
    answer = PopupOKCancel(
            question,
            title=f'Confirm {action}',
            keep_on_top=True
            )

    return answer == 'OK'
