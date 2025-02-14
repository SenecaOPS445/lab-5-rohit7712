#!/usr/bin/env python3
# Author ID: 145339222

def read_file_string(file_name):
    file = open(file_name, 'r')
    return file.read()

def read_file_list(file_name):
    file = open(file_name, 'r')
    content = []
    for line in file:
        content.append(line.strip())
    return content

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))



