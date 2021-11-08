#  Copyright (c) 2021. __init__.py is a part of the ''inspyre-toolbox.clipman' project by Inspyre Softworks D.O. and is licensed under the MIT License. Feel free to copy, share, distribute any code from this project  as you please. If you do; please share where you got it.

from inspyre_toolbox.clipman.config import LOG_DEVICE
from inspyre_toolbox.clipman.gui.sys_tray import sys_tray as SYS_TRAY
from inspyre_toolbox.clipman.gui.windows.edit import EditPasteWindow
from inspyre_toolbox.clipman.gui.windows.main import MainWindow
from inspyre_toolbox.clipman.gui.windows.popups import confirm_action as confirm_action_popup

_log = LOG_DEVICE.add_child('gui')

main_win_running = None
main_win = None

app_running = True


def run() :
    """
    
    Run the GUI for Inspyre-Toolbox::Clipman.
    
    Parameters:
        None
        
    Returns:
        None
    
    """
    global main_win_running, main_win, app_running, cb_history
    log = LOG_DEVICE.add_child('gui.run')
    
    log.debug("Creating main window")
    win = MainWindow()
    main_win_running = win.running
    
    app_running = True
    
    main_win = win.window
    
    selected_entry = None
    
    win_entries = None
    
    while app_running :
        tray_event = SYS_TRAY.read(timeout=100)
        
        if main_win_running is None :
            main_win_running = True
            win.create_window()
            main_win = win.window
        
        while main_win_running :
            event, values = main_win.read(timeout=100)
            
            if win_entries is None :
                win_entries = cb_history
            
            if len(cb_history) >= 1 :
                main_win['CLEAR-HIST_BUTTON'].update(disabled=False)
            
            if event == 'CLOSE_BUTTON' :
                log.debug("Close main window")
                
                log.debug("Main window closed!")
                main_win_running = False
                win.close_window()
                break
            
            if event is None :
                log.debug("Closing main window")
                main_win_running = False
                win.close_window()
                log.debug("Main window closed!")
                break
            
            if 'ENTRY_' in event :
                selected_entry = cb_history[int(event.split('_')[1]) - 1]
                for prefix in win.disabled_button_prefixes :
                    main_win[prefix.upper() + '_BUTTON'].update(disabled=False)
            
            if '_BUTTON' in event :
                if 'EDIT' in event :
                    edit_win = EditPasteWindow(selected_entry)
                    edit_win.run()
                
                if 'CLEAR-HIST' in event :
                    log.info("Received 'clear history' directive.")
                    log.debug("Confirming with user...")
                    if confirm_action_popup("Are you sure you want to clear the clipboard history?", 'history clear') :
                        log.info("Received confirmation via popup, proceeding to delete history")
                        cb_history = []
                        log.info("History deleted.")
            
            if tray_event == 'Exit' :
                exit_app()
        if tray_event == 'Exit' :
            exit_app()
        if tray_event == 'Show History' :
            log.debug("Showing window")
            main_win_running = True
            win.create_window()
            main_win = win.window


def exit_app() :
    """
    
    Exit all GUI parts of the application cleanly.
    
    Parameters:
        None
        
    Returns:
        None
    
    """
    global main_win_running, main_win, app_running
    log = LOG_DEVICE.add_child('gui.exit_gui')
    log.debug("Received call to quit GUI")
    app_running = False
    main_win_running = False
    
    tray_running = False
