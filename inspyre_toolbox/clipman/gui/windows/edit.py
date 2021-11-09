#  Copyright (c) 2021. edit.py is a part of the ''inspyre-toolbox.clipman' project by Inspyre Softworks D.O. and is licensed under the MIT License. Feel free to copy, share, distribute any code from this project  as you please. If you do; please share where you got it.

import PySimpleGUI as gui
from inspyre_toolbox.clipman.config import ARGS, DEV_UNLOCK, LOG_DEVICE


class EditPasteWindow :
    
    
    def __init__(self, clipboard_entry) :
        self.layout = None
        self.window = None
        self.running = False
        self.content = clipboard_entry
    
    
    def create_layout(self):
        layout = [
                [
                        gui.Text("Edit the entry text below:")
                        ],
                [
                        gui.InputText(
                            self.content,
                            size=(200, 200),
                            expand_x=True,
                            expand_y=True,
                            key='ENTRY_TEXT',
                            enable_events=True
                            )
                        ],
                [
                        gui.Button(
                                "Copy",
                                key="EDIT-PASTE-WIN_COPY",
                                tooltip="Exit this window and move text from the window's text area to the "
                                        "clipboard_history",
                                disabled=True
                                ),
                        gui.Button(
                                "Cancel",
                                key="EDIT-PASTE-WIN_CANCEL"
                                ),
                        gui.Button(
                                "Reset",
                                tooltip='Reset entry to previous state.',
                                key="EDIT-PASTE-WIN_RESET",
                                disabled=True
                                )
                        ]
                ]
        if DEV_UNLOCK and ARGS.dev_mode:
            layout.insert(-1, [gui.Button('Unlock All Buttons', key='EDIT-PASTE-WIN_UNLOCK')])

        self.layout = layout
    
    
    def create_window(self) :
        self.create_layout()
        self.window = gui.Window('Edit Clipboard Entry', layout=self.layout)
    
    
    def close_window(self) :
        self.layout = None
        self.window.close()
        self.window = None
        self.running = False
    
    
    def run(self) :
        self.running = True
        
        log = LOG_DEVICE.add_child('config.gui.windows.edit.EditPasteWin.run')
        
        log.debug('Starting window loop.')
        log.debug(f'Running: {self.running}')
        self.create_window()
        while self.running :
            event, values = self.window.read(timeout=100)
            
            if event is None :
                self.running = False
                self.close_window()
                break
            
            e_low = event.lower()
            
            if 'edit-paste-win' in e_low :
                log.debug(f"Received button event: {event}")
                log.debug(f"Current values are: {values}")
                if '_cancel' in e_low :
                    log.debug("Setting 'self.running' to 'False' due to receiving 'Cancel' button-press!")
                    self.running = False
                    self.close_window()
                    break
                
                if '_copy' in e_low :
                    log.debug("Received button-press for 'Copy' button!")
                
                if '_reset' in e_low :
                    log.debug("Received button-press for 'Reset' button!")
            
            log.debug(f'Running: {self.running}')
            if not self.running :
                log.debug('The "running" flag has been set to false! Expect an exit!')
                break
