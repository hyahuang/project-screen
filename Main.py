# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 18:04:09 2020

@author: Sean
"""
import ParseCsv
import csv

if __name__ == '__main__':
    parser = ParseCsv.ParseCsv()
    while (True):
        try:
            filename=input("Input filename or \"exit\":")
            if(filename=="exit" ):
                break; 
            while(True):
               csvfile = open (filename,newline='')
               try:
                   csvf = csv.DictReader(csvfile)
                   command=input("Input command(etc. -name <pattern>, -email <pattern>, -gpa <gpa>[+-]) or \"exit\":")
                   if(command=="exit" ):
                       break;
                   parser.parse(command,csvf)
               except:
                   print('Please input correct command')
        except:
            print('Please input correct filename')
    

            