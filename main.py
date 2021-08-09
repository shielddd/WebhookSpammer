import time, sys, time, os

try:
    import requests
    from colorama import Fore, init
except (ModuleNotFoundError):
    os.system('pip install requests colorama')

from colorama import Fore, init
init(convert=True)

print(f'{Fore.MAGENTA}Webhook{Fore.RESET}\n1. Spam Webhook\n2. Delete Webhook')
print(f'{Fore.MAGENTA}Choice ->: {Fore.RESET}', end='')
choice = int(input(''))

if choice not in [1, 2]:
    print(f'---\n{Fore.MAGENTA}Webhook{Fore.RESET} -> {Fore.RED}Error{Fore.RESET} : Invalid Choice')
    time.sleep(1)

if choice == 1:
    print(f"---\n{Fore.MAGENTA}Webhook URL{Fore.RESET}")
    webhook = str(input(" > "))
    print(f"{Fore.MAGENTA}Message{Fore.RESET}")
    message = str(input(" > "))
    while True:
        _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
        if _data.status_code == 204:
            print('Sent a new message!')

if choice == 2:
  print(f"---\n{Fore.MAGENTA}Webhook URL{Fore.RESET}")
  webhook = str(input(" > "))
  requests.delete(webhook)
