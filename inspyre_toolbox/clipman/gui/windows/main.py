#  Copyright (c) 2021-2021. main.py is a part of the ''inspyre-toolbox.clipman' project by Inspyre Softworks D.O. and is licensed under the MIT License. Feel free to copy, share, distribute any code from this project  as you please. If you do; please share where you got it.
import PySimpleGUI as gui

from inspyre_toolbox.clipman.clipboard_history import history


class MainWindow(object) :
    
    
    def __init__(self) :
        self.layout = None
        self.window = None
        
        self.running = None
        self.disabled_button_prefixes = ['edit', 'copy', 'del']
    
    
    def create_layout(self) :
        self.layout = [
                [gui.Text("Below are your latest clipboard entries")]
                ]
        counter = 0
        for entry in history :
            counter += 1
            print(f'Entry: {entry}')
            print(counter)
            entry_layout = [
                    gui.Radio(
                        entry[:15] + '...', group_id='CLIPBOARD_HISTORY', key=f'ENTRY_{counter}',
                        enable_events=True
                        ),
                    ]
            print(len(entry_layout))
            self.layout.append(entry_layout)
        button_layout = [
                gui.Button('Edit Entry', disabled=True, key='EDIT_BUTTON'),
                gui.Button('Copy Entry', disabled=True, key='COPY_BUTTON'),
                gui.Button('Delete Entry', disabled=True, key='DEL_BUTTON'),
                gui.Button('Clear History', disabled=True, key='CLEAR-HIST_BUTTON'),
                gui.Button('Close Window', key='CLOSE_BUTTON')
                
                ]
        self.layout.append(button_layout)
    
    
    def create_window(self) :
        self.create_layout()
        self.window = gui.Window(title='Clipman', layout=self.layout)
    
    
    def close_window(self) :
        if self.window is not None :
            self.window.close()
            self.window = None
            self.layout = None
        return None
