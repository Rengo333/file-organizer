import datetime
import os
from pathlib import Path


def main():

    # dict of lists of file suffixes ( you can add anything you want)
    list_of_directories = {
        "Picture_Folder": [".jpeg", ".jpg", ".gif", ".png", ".bmp"],
        "Video_Folder": [".wmv", ".mov", ".mp4", ".mpg", ".mpeg", ".mkv"],
        "Zip_Folder": [".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".zip"],
        "Music_Folder": [".mp3", ".msv", ".wav", ".wma"],
        "PDF_Folder": [".pdf"],
        "TXT_Folder": [".txt"],
        "CSV_Folder": [".csv"],
    }

    # format for creating directories
    file_format_dict = {
        final_file_format: directory
        for directory, file_format_stored in list_of_directories.items()
        for final_file_format in file_format_stored
    }

    # loop to check input
    while True:
        # getting path from a user
        path_inp = input("Please enter where you want to sort the files:")
        if not check_path(path_inp):
            continue
        path = path_inp
        # path used when creating directories
        path_for_os = Path(path)
        sorted_by = input(
            "Please enter if you want to sort by a month or a day: ")
        if not check_sort(sorted_by)[0]:
            continue
        else:
            month_or_day = check_sort(sorted_by)[1]

        # getting confirmation else exit the program
        confirmation = input(f"Are you sure you want to sort the files by a {sorted_by} at {path_inp}?(y/n): ")
        if confirmation == "y":
            break
        elif confirmation == "n":
            quit()
        else:
            print("Please enter 'y' for yes or 'n' for no.")

    file_organizer(path, path_for_os, month_or_day, file_format_dict)

    # creating folder for everything that is not in list of suffixes
    try:
        path_other_folder = path + "/" + "Other_Folder"
        os.mkdir(path_other_folder)
    except FileExistsError:
        print("Failed to create a new folder. Other_Folder may already exist")

    # deleting empty folders and putting the rest of files in other folder
    for dir in os.scandir(path):
        try:
            if "_Folder" in os.path.basename(dir):
                continue

            elif os.path.isdir(dir):
                os.rmdir(dir)
            else:
                os.rename(str(Path(dir)), path_other_folder + "/" + os.path.basename(dir))

        except OSError:
            print(f"Failed to remove a directory {os.path.basename(dir)}. Directory is not empty")


# check path input
def check_path(path_inp):

    if '\\' in path_inp:
        for char in path_inp:
            if char == '\\':
                char.replace('\\', "/")
        if os.path.exists(path_inp):
            return True

    elif "/" not in path_inp or not os.path.exists(path_inp):
        print("This is not a valid path.")
        return False

    elif os.path.exists(path_inp):
        return True


# check sort by input
def check_sort(sorted_by):

    if sorted_by == "day":
        month = 7
        return [True, month]
    elif sorted_by == "month":
        day = 10
        return [True, day]
    else:
        print("Please type 'month' or 'day'.")
        return False


def file_organizer(path, path_for_os, month_or_day, file_format_dict):

    # returns files in the directory
    for entry in os.scandir(path):

        # skip directories
        if entry.is_dir():
            continue

        # get path of a file
        file_path = Path(entry)

        # name of a file
        file_name = os.path.basename(entry)
        # suffix (e.g. .txt, .pdf)
        final_file_format = file_path.suffix.lower()

        if final_file_format in file_format_dict:

            # getting last modified data
            m_time = os.path.getmtime(file_path)
            dt_m = datetime.datetime.fromtimestamp(m_time)

            # sorting by a day[:7] or a month[:10]
            last_modified = str(dt_m)[:month_or_day]

            # merging paths
            file_directory_path = Path(file_format_dict[final_file_format])
            directory_path = path_for_os.joinpath(file_directory_path)
            new_file_path = directory_path.joinpath(last_modified)

            # creating folder and moving files
            os.makedirs(new_file_path, exist_ok=True)
            os.rename(file_path, new_file_path.joinpath(file_name))


if __name__ == "__main__":
    main()
