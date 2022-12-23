#LIBRARIES
from colorama import *
import random
from time import sleep, time
import sys
import os
import re
import emoji
import string
import zipfile
import requests
import threading
import easygui
import shutil
import datetime
import pyautogui
import keyboard

##############################################

def menu():
  from colorama import Fore, Back, Style, init
  import random
  import time

  init(autoreset=True)
  print(Fore.CYAN + '      | $$$|    /$|$$$$$$$$|            |$$$$$$$$$ |   $$|     /$|            |$$$$$$$$$ | ')
  time.sleep(0.1)
  print(Fore.CYAN + '      | $$$|    $$|                   /$$$$$$$$ |      $$|     |$|          /$$$$$$$$ | ')
  time.sleep(0.1)
  print(Fore.CYAN + '      | $$$|    $$|                 /$$$$$$ /          $$|     |$|        /$$$$$$ / ')
  time.sleep(0.1)
  print(Fore.CYAN + '      | $$$|    $$|_____           |$$$$ |             $$|     |$|       |$$$$ | ')
  time.sleep(0.1)
  print(Fore.CYAN + '      | $$$|    $$|$$$$$|           \$$$$$ \           $$|     |$|        \$$$$$ \ ')
  time.sleep(0.1)
  print(Fore.CYAN + '      | $$$|    $$|$$$$$|             \$$$$$ \         $$|     |$|          \$$$$$ \ ')
  time.sleep(0.1)
  print(Fore.CYAN + '      | $$$|    $$|                    |$$$$  |        $$|     |$|           |$$$$  | ')
  time.sleep(0.1)
  print(Fore.CYAN + ' |$|__| $$$|    $$|                   /$$$$$ /         $$|     |$|          /$$$$$ / ')
  time.sleep(0.1)
  print(Fore.CYAN + ' |$$$$$$$$/     $$|________     _____/$$$$$ /          $$|     /$|    _____/$$$$$ / ')
  time.sleep(0.1)
  print(Fore.CYAN + ' |_______/      \$|$$$$$$$$|    $$$$$$$$$$ /           \________/     $$$$$$$$$$ / ')

  w = Fore.WHITE
  b = Fore.BLACK
  g = Fore.LIGHTGREEN_EX
  y = Fore.LIGHTYELLOW_EX
  m = Fore.LIGHTMAGENTA_EX
  c = Fore.LIGHTCYAN_EX
  lr = Fore.LIGHTRED_EX
  lb = Fore.LIGHTBLUE_EX


  time.sleep(1.2)
  print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
{m}[{w}1{Fore.RESET}{m}]{Fore.RESET} Discord Nitro   {b}|{Fore.RESET}{m}[{w}9{Fore.RESET}{m}]{Fore.RESET}  Webhook Spammer      
{m}[{w}2{Fore.RESET}{m}]{Fore.RESET} Nitro Checker   {b}|{Fore.RESET}{m}[{w}10{Fore.RESET}{m}]{Fore.RESET} Channel Spammer       
{m}[{w}3{Fore.RESET}{m}]{Fore.RESET} Token Checker   {b}|{Fore.RESET}{m}[{w}11{Fore.RESET}{m}]{Fore.RESET} DM Spammer       
{m}[{w}4{Fore.RESET}{m}]{Fore.RESET} Token Onliner   {b}|{Fore.RESET}{m}[{w}12{Fore.RESET}{m}]{Fore.RESET} Friend Spammer
{m}[{w}5{Fore.RESET}{m}]{Fore.RESET} Token Grabber   {b}|{Fore.RESET}{m}[{w}13{Fore.RESET}{m}]{Fore.RESET} Reaction Spammer       
{m}[{w}6{Fore.RESET}{m}]{Fore.RESET} Ask Question    {b}|{Fore.RESET}{m}[{w}14{Fore.RESET}{m}]{Fore.RESET} About{Fore.RESET}
{m}[{w}7{Fore.RESET}{m}]{Fore.RESET} Say Chat        {b}|{Fore.RESET}{m}[{w}15{Fore.RESET}{m}]{Fore.RESET} Version{Fore.RESET}
{m}[{w}8{Fore.RESET}{m}]{Fore.RESET} Server Nuker    {b}|{Fore.RESET}{m}[{w}16{Fore.RESET}{m}]{Fore.RESET}{lr} EXIT{Fore.RESET}''')
  
  print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
  choice = input('Elige una opción: ')

  #DISCORD NITRO

  if choice == '1':
    from base64 import urlsafe_b64decode
    from http.client import REQUEST_ENTITY_TOO_LARGE
    from optparse import check_builtin
    import random
    import string
    from urllib import request

    def gen():
      import random

      upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      lower_letter = 'abcdefghijklmnopqrstuvwxyz'
      digits = '0123456789'

      numbtogen = input('Cuántos códigos quieres generar: ')
      upper, lower, nums, = True, True, True,
      all = ""

      if upper:
          all += upper_letter
      if lower:
          all += lower_letter
      if nums:
          all += digits
        
      lenght = 16
      amount = numbtogen

      for x in range(int(numbtogen)):
          nitro = ''.join(random.sample(all, lenght))
          print('discord.gift/'+nitro)

      gen()
    
  #Nitro Checker  
  if choice == '2':
    print(f'{m} En desarrollo')
    time.sleep(1)
    return menu()

  #Token Checker
  if choice == '3':
    print(f'{m} En desarrollo')
    time.sleep(1)
    return menu()

  #Token Onliner
  if choice == '4':
    print(f'{m} En desarrollo')
    time.sleep(1)
    return menu()

  #Token Grabber
  if choice == '5':
    print(f'{m} En desarrollo')
    time.sleep(1)
    return menu()

  #Ask Question
  if choice == '6':
   return menu()

  #Say Chat
  if choice == '7':
    return menu()

  #Server Nuke
  if choice == '8':
    print(f'{m} En desarrollo')
    time.sleep(1)
    return menu()

  #Webhook Spammer
  if choice == '9':
    print(f'{m} En desarrollo')
    time.sleep(1)
    return menu()

  #Channel Spammer
  if choice == '10':
    print(f'{m} En desarrollo')
    time.sleep(1)
    return menu()

  #DM Spammer
  if choice == '11':
    print(f'{m} En desarrollo')
    time.sleep(1)
    return menu()

  #Friend Spammer
  if choice == '12':
    print(f'{m} En desarrollo')
    time.sleep(1)
    return menu()

  #Reaction Spammer
  if choice == '13':
    print(f'{m} En desarrollo')
    time.sleep(1)
    return menu()

  #About
  if choice == '14':
    print('Hola, gracias por usar la tool Jesus-C.\nTodo aquel que utilize esta tool, se hace responsable de las posibles consecuencias si es que se hace un mal uso de esta.')
    print('Presiona ENTER para volver al panel')
    while True:
      if keyboard.is_pressed('enter'):
        return menu()
    

  #Version
  if choice == '15':
    print(f'{g} 1.0')
  
  #Exit
  if choice == '16':
    Sgr = str(input('Estás seguro de que quieres salir? S/N:'))
    if Sgr == 'S':
      sys.exit()
    else:
      return menu()





menu()