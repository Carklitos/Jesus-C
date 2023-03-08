from utilities.settings.libraries import *
from utilities.settings.funtions import *

def DmDeleter(token, channels):
    for channel in channels:
        try:
            requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'],
            headers=getheaders(token))
            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] DM Borrado: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"\nERROR | {e}")