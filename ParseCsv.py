# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 17:45:05 2020

@author: Sean
"""
import pandas as pd
import re

class ParseCsv():
    def __init__(self):
        self.regexN = r"^-[ ]*name[ ]*<"
        self.regexE = r"^-[ ]*email[ ]*<"
        self.regexG = r"^-[ ]*gpa[ ]*<"
    def parse(self,command,csvf):
        if(re.search(self.regexN,command)!=None):
            self.parseName(csvf,command)
        elif(re.search(self.regexE,command)!=None):
            self.parseEmail(csvf,command)
        elif(re.search(self.regexG,command)!=None):
            self.parseGPA(csvf,command)
        else: 
            print('Please input correct command')
            return
    def parseName(self,csvf,command):
        match = re.search(self.regexN,command) ##delete inforamtion other than pattern
        reg = command.replace(match.group(0),"")
        reg = reg.replace(">","")
        for row in csvf:
            if(re.search(reg,row['firstname'],flags=re.IGNORECASE)!=None or re.search(reg,row['lastname'],flags=re.IGNORECASE)!=None):
                print(row['firstname'],row['lastname'],row['email'],row['gpa'])
    def parseEmail(self,csvf,command):
        match = re.search(self.regexE,command)
        reg = command.replace(match.group(0),"")
        reg = reg.replace(">","")
        for row in csvf:
            if(re.search(reg,row['email'])!=None):
                print(row['firstname'],row['lastname'],row['email'],row['gpa'])
    def parseGPA(self,csvf,command):
        match = re.search(self.regexG,command)
        threshold = command.replace(match.group(0),"")
        threshold = threshold.replace(">","")
        if(threshold.find('-')==-1):
            threshold = threshold.replace("+","")
            for row in csvf:
                if(float(row['gpa'])>=float(threshold)):
                    print(row['firstname'],row['lastname'],row['email'],row['gpa'])
        else:
            threshold = threshold.replace("-","")
            for row in csvf:
                if(float(row['gpa'])<=float(threshold)):
                    print(row['firstname'],row['lastname'],row['email'],row['gpa'])
            