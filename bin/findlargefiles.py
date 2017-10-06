#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# findlargefiles.py Searches a file location and subdirectories for
# files larger than a given size.
"""
findlargefiles.py Searches a file location and subdirectories for
files larger than a given size.
Useful for phones which might hide files in FileExplorer.
Directly prints results if run directly.
May also be imported, yielding results one by one.

Created on Sun Sep  3 20:35:12 2017

@author: david.antonini // toonarmycaptain
"""

import os


def search_folder(location, min_file_size):
    file_not_found_errors_count = 0
    files_found_count = 0
    total_size = 0
    print(f'Files larger than {min_file_size:.2f} MB in location: {location}')
    for foldername, subfolders, filenames in os.walk(location):
            for filename in filenames:
                try:
                    actual_size = os.path.getsize(os.path.join(foldername,
                                                               filename))
                    if min_file_size*1024**2 <= actual_size:
                        print(f'{foldername}\\{filename} - '
                              f'{(actual_size/1024**2):.2f} MB')
                        yield foldername, filename, actual_size
                        files_found_count += 1
                        total_size += actual_size
                except FileNotFoundError:
                    file_not_found_errors_count += 1
                    print(f'FileNotFoundError: {filename}')
    print(f'Files found: {files_found_count}')
    print(f'Total size: {(total_size/1024**2):.2f} MB')
    if file_not_found_errors_count > 0:
        print(f'FileNotFoundErrors: {file_not_found_errors_count}')


if __name__ == '__main__':
    print('This program searches for files larger than a given size '
          'in a given location.')

    while True:
        location = input("Where would you like to search? ")
        if os.path.exists(location):
            break
        else:
            print('Please enter a valid path.')
    while True:
        try:
            min_file_size = float(input('Please enter file size in MB: '))
            break
        except ValueError:
            print('Please enter numeric input only.')

    search_folder(location, min_file_size)

    for foldername, filename, actual_size in search_folder(location,
                                                           min_file_size):
        print(f'{foldername}\\{filename} - {(actual_size/1024**2):.2f} MB')
