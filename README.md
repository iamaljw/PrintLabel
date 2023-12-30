## Context and Motivation

This project was born out of a real-world need within an e-commerce business context, specifically aimed at improving the efficiency of printing shipping labels and documents. As someone who helps manage an overseas sister's e-commerce business, I found myself spending a significant amount of time manually printing various types of labels. The process involved manually setting the printer, printing labels, and confirming their completion — a repetitive and time-consuming task.

The e-commerce business required two types of printouts: smaller labels for individual items using a label printer and larger A4 labels for shipping using a regular printer. Manually handling these tasks was prone to errors, such as selecting the wrong printer or missing out on some print jobs.

This system aims to automate the entire process: from detecting the correct type of label to setting the appropriate printer and finally printing and reporting the status of each job. It's designed to run with minimal intervention, freeing up time and reducing manual errors, thus contributing significantly to operational efficiency.

## Features

- **Automatic Printer Selection**: Dynamically sets the printer based on the type of document (Label or A4).
- **Remote Printing Capability**: Allows users to add files to a designated Google Drive folder for printing, suitable for users managing businesses remotely.
- **Status Reporting**: Sends an email notification detailing the status of each print job, ensuring transparency and allowing for quick troubleshooting.
- **Adobe Acrobat Management**: Automatically closes Adobe Acrobat post-printing to maintain system performance and readiness for the next job.

## How to Set Up

1. **Install Python**: Ensure Python is installed on your system.
2. **Install Dependencies**: Install necessary Python libraries using pip: pip install pygetwindow pyautogui win32print win32api 
3. **Configure Printers**: Make sure the correct printers are installed and configured on your system.
4. **Set Up Google Drive Sync**: Ensure the Google Drive folder is synced to a local directory on your system.
5. **Update File names and Directory**: Update the respective variable names according to your needs, and ensure the directory path is updated in the script.
6. **Configure Email**: Set up environment variables or a configuration file to securely store email credentials.

## Usage
1. **Add Files to Print**: Place the files you want to print in the synced Google Drive folder.
2. **Start the Script**: Run the script using Python.
3. **Check Email**: After the script runs, check the specified email for a report on the print jobs.

## How to Contribute

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. 

