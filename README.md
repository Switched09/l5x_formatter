# Introduction
A Python script that reads a .L5X file (which is an XML-based file format used by Rockwell Automation for ControlLogix and CompactLogix PLC programs, then organizes its content in a more indented and readable XML format.

# Script Variables Preparation 
Prior to run the script, update the content of the variables:
**input_file**
**output_file**

With the full path of both .L5X files, the one to read and the final indented file

``` python
# Example usage
input_file =  "/home/user/Documents/PLC_Program/PLC_Program_L5X_File.L5X"          # Path for the Original L5X file
output_file = "/home/user/Documents/PLC_Program/PLC_Program_L5X_File_Ident.L5X"    # Path for the Idented L5X file
```