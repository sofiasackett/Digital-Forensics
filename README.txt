Author: Sofia Sackett
Build date: 17 April 2020 
Program: hw3Sackett.py

Purpose:
hw3Sackett.py traverses a given directory and looks for JPEG files and any appended data. 
If the program finds appended data it will decode the message and hash the original file.
The program will print the path to the output file, Sackettoutput.txt, as well as the time the script completes.

How to Execute:
hw3Sackett.py can be run from the command line on Windows by opening a command prompt with root privileges.

1. Within the command prompt, navigate to the location of the hw3Sackett.py file using cd.
2. Simply enter the name of the program <<hw3Sackett.py>> and the program will begin.
3. Enter the path to the directory of interest. Please begin with the drive letter and end with the root directory you want to investigate.
   For example, C:\Users\username\Desktop\HelloFolder would investigate the contents of the HelloFolder.
4. When the script is finished running, it will print the location of the output file and the time the script finished executing.

Special Requirements:
There are no special requirements to run hw3Sackett.py, however the program was built to function on a Windows machine.
All imported libraries are native to Python and don't need to be downloaded from external sources.

Troubleshooting:
If the program will not accept your file path, ensure that you are using backslashes and that you are starting from your drive letter.
There is no need to add a slash to the end of your file path.
If the libraries are giving you trouble, perhaps because you are using an older version of python, all necessary libraries can be installed from the command line with pip.