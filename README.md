# File organizer

Program organizes files in a specified directory
using list of directories, if you want to sort
your files differently you can change names and
move suffixes to different directories.

# Sorting and moving files

You can change this list of directories however you want.
It needs to be dictionary with, key as a folder name and value as
a list of file suffixes.

Example:

> list_of_directories = {"Folder_name": [.suffix1, .suffix2]}

You will find a whole list on line 9.

Another way of sorting in this program is by a day or a month, 
program is going to ask if you want to sort either by a month
or a day and create additional folders to help you find your files by a date.
I personally recommend using month, but its up to your needs.

# Requirements
Additional libraries are required to install. 
It is recommended to use a new virtual envinronment.
Use this command in terminal to install requirements from requirements.txt.

>pip install -r requirements.txt