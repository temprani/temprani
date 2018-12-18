#!/usr/bin/env python3

output_dict={}
import sys

def handle_data(a):
    key=a.split(':')[0]
    value=a.split(':')[1]
    output_dict[key]=value

def print_data(b,c):
    print('ID:',b,"Name:",c)

if __name__=='__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key,output_dict[key])
