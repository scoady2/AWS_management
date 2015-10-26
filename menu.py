#!/usr/bin/python3

def start_menu():
  print('\n|==============================================|')
  print('|                  AWS Manager                 |')
  print('|==============================================|')
  print('| Welcome to AWS Manager. A program to help    |')
  print('| you manage your AWS instances.               |')
  print('|                                              |')
  print('|______________________________________________|\n')

def main_menu():
  print('\n|==============================================|')
  print('|                  Main Menu                   |')
  print('|==============================================|')
  print('| 1) Create new instance                       |')
  print('| 2) Manage your current instances             |')
  print('| 0) Exit                                      |')
  print('|______________________________________________|\n')

def new_instance():
  print('\n|==============================================|')
  print('|               Instance Manager               |')
  print('|==============================================|')
  print('| Please note, python will be installed on     |')
  print('| your instance by default. There will be a    |')
  print('| delay while SSH starts up and python is      |')
  print('| installed.                                   |')
  print('|==============================================|')
  print('| 1) Launch new instance                       |')
  print('| 2) Manage your current instances             |')
  print('| 0) Return                                    |')
  print('|______________________________________________|\n')

def instance_manager():
  print('\n|==============================================|')
  print('|              Instance Manager                |')
  print('|==============================================|')
  print('| 1) Start instance                            |')
  print('| 2) Stop instance                             |')
  print('| 3) Terminate instance                        |')
  print('| 4) Install python                            |')
  print('| 5) Install nginx                             |')
  print('| 6) Copy check_webserver script to instance   |')
  print('| 7) Run nginx checking script                 |')
  print('| 0) Return                                    |')
  print('|______________________________________________|\n')