import os
import smtplib
import datetime
import win32print
import win32api
import time
import pygetwindow as gw
import pyautogui

# Defining Printers and Labels
LabelPrinter = "<Your Printer Name>"
A4Printer = "<Your Printer Name>"
Label = "<Your File Name>.pdf"
A4 = "<Your File Name>.pdf"
LabelStatus = False
A4Status = False

# Mailing Recipients
Recipient = '<Your Recipient Email'

# Initialize Global Variables
current_printer = win32print.GetDefaultPrinter()
itemindirectory = os.listdir(r'G:\<whatever>\<whatever>') #Replace with your Directory

# Display Current Printer
print(f"Current Printer: {current_printer}")

# Set Printer Function
def SetPrinter(TargetPrinter):
    global current_printer
    for attempt in range(3):  
        if current_printer != TargetPrinter:
            try:
                win32print.SetDefaultPrinter(TargetPrinter)
                time.sleep(5)  
                current_printer = win32print.GetDefaultPrinter()
                if current_printer == TargetPrinter:
                    print(f"Printer has been set to {TargetPrinter}")
                    return True  # Successfully set the printer
                else:
                    print(f"Attempt {attempt + 1}: Failed to set to {TargetPrinter}, current printer is still {current_printer}")
            except win32api.error as e:
                print(f"Unable to set {TargetPrinter} as default. Error: {e}")
        else:
            return True  # Printer was already set
    return False  # Failed to set printer after attempts

# Refresh Directory Function
def refreshDirectory():
    global itemindirectory
    os.listdir(r'G:\<whatever>\<whatever>') #Replace with your Directory
    print("Initial Directory Refresh Complete")
    time.sleep(10)
    itemindirectory = os.listdir(r'G:\<whatever>\<whatever>')
    print(f"""Final Directory Refresh Complete.
          Here are the items in the directory:
          {itemindirectory}
          """)

# Print File Function
def printfile():
    global LabelStatus, A4Status  # Declare these variables as global
    refreshDirectory()
    file_printed = False
    os.chdir(r'G:\<whatever>\<whatever>') #Replace with your Directory
    for i in itemindirectory:
        if i == Label:
            if SetPrinter(LabelPrinter):
                closeAdobeAcrobat()
                os.startfile(Label, 'print')  
                print(f"{Label} has been printed via {win32print.GetDefaultPrinter()}")
                file_printed = True
                LabelStatus = True
                time.sleep(5)
                closeAdobeAcrobat()
        elif i == A4:
            if SetPrinter(A4Printer):
                closeAdobeAcrobat()
                os.startfile(A4, 'print') 
                print(f"{A4} has been printed via {win32print.GetDefaultPrinter()}")
                file_printed = True
                A4Status = True
                time.sleep(5)
                closeAdobeAcrobat()
    if not file_printed:
        print("No match found in directory. No files were printed")

# Define Current Date and Time
now = datetime.datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Email Alert Function
def EmailAlert():
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('<Your Email', 'Your Password')
    conn.sendmail('<Sender Email>', Recipient, msg)
    conn.quit()

# Close Adobe Acrobat
def closeAdobeAcrobat():
    # Attempt to find and close Adobe Acrobat
    for window in gw.getWindowsWithTitle('Adobe Acrobat'):
        if 'Adobe Acrobat' in window.title:  
            window.close() 

# Execute Functions
printfile()

# Email Content
msg = f"""Subject:Label Print Status.        
Hello <Person's Name>,

Your label has been printed on {dt_string}.
    
    Label Print Status: 
        Label: {'Printed' if LabelStatus else 'Not Printed'}
        A4: {'Printed' if A4Status else 'Not Printed'}

- <Your Name>"""

EmailAlert()
