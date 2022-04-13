#!/usr/bin/python3

"""Run this program in a directory that needs cleaning up. The program sorts
files according to its file format."""

import os
from pathlib import Path

Directories = {
               "HTML": [".html5", ".html", ".htm", ".xhtml"],
               "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png",
                          ".bpg", "svg", ".heif", ".psd"],
               "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm",
                          ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
               "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc",
                             ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps",
                             ".dotx", ".docm", ".dox", ".rvg", ".rtf",
                             ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                             "pptx"],
               "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz",
                            ".7z", ".dmg", ".rar", ".xar", ".zip"],
               "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                         ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav",
                         ".wma"],
               "Plaintext": [".txt", ".in", ".out"],
               "PDF": [".pdf"],
               "XML": [".xml"],
               "EXE": [".exe"],
               "SHELL": [".sh"]
               }

File_Format_Dictionary = {
                          file_format: directory
                          for directory, file_formats in Directories.items()
                          for file_format in file_formats
                          }


def main():
    """The main function of the program. It scans all files in the current
    directory, checks each file suffix with a dictionary of file formats and
    creates a new directory for specified file formats."""
    for entry in os.scandir('.'):
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in File_Format_Dictionary:
            directory_path = Path(File_Format_Dictionary[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))


if __name__ == "__main__":
    main()
