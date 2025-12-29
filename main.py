import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)
GREY = Fore.LIGHTBLACK_EX

try:
    import ytdownloader as downloader
except ImportError:
    print(f"\n{Fore.RED}[!] Error: ytdownloader.py missing.")
    sys.exit(1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    print(Fore.CYAN + r"""
⣿⠛⠛⠛⠛⠻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠛⢛⣿⠋⢀⡾⠃⠀⠀⠀⠀⢀⣤⣤⠤⠤⣤⣤⣀⣀⣀⣠⠶⡶⣤⣀⣠⠾⡷⣦⣀⣤⣤⡤⠤⠦⢤⣤⣄⡀⠀⢠⡶⢶⡄⠀⠀
⢠⡟⠁⣴⣿⢤⡄⣴⢶⠶⡆⠈⢷⡀⠀⠀⠀⠀⢀⣭⣫⠵⠥⠽⣄⣝⠵⢍⣘⣄⠳⣤⣀⠀⠀⢀⡤⠊⣽⠁⠀⠸⣇⠀⢿⠀⠀
⠸⢷⣴⣤⡤⠾⠇⣽⠋⠼⣷⠀⠈⢷⡄⢀⣤⡶⠋⠀⣀⡄⠤⠀⡲⡆⠀⠀⠈⠙⡄⠘⢮⢳⡴⠯⣀⢠⡏⠀⠀⠀⢻⠀⢸⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠛⠋⠉⢀⣴⠟⠉⢯⡞⡠⢲⠉⣼⠀⠀⡰⠁⡇⢀⢷⠀⣄⢵⠀⠈⡟⢄⠀⠀⠙⢷⣤⣤⣤⡿⢢⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠑⠊⠁⡼⣌⢠⢿⢸⢸⡀⢰⠁⡸⡇⡸⣸⢰⢈⠘⡄⠀⢸⠀⢣⡀⠀⠈⢮⢢⣏⣤⡾⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣯⣴⠞⡠⣼⠁⡘⣾⠏⣿⢇⣳⣸⣞⣀⢱⣧⣋⣞⡜⢳⡇⠀⢸⠀⢆⢧⠀⠰⣄⢏⢧⣾⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⡏⢰⠁⡻⠀⡟⡏⠉⠀⣀⠀⠀⠀⠀⣀⠁⠀⠉⠛⢽⠇⠀⣼⡆⠈⡆⠃⠀⡏⠻⣾⣽⣇⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⡇⠀⡇⡄⣿⠷⠿⠿⠛⠀⠀⠀⠀⠛⠻⠿⠿⠿⡜⢀⡴⡟⢸⣸⡼⠀⠀⡇⠀⡞⡆⢻⠙⢦⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡶⢀⣼⣿⣬⣽⠧⠬⠇⠀⠀⠀⠀⠀⠀⢞⣯⣭⢺⣔⣪⣾⣤⠺⡇⢳⠀⢠⣧⡾⠛⠛⠻⠶⠞⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⢿⠟⠉⡀⠈⢦⡀⠀⠀⣠⠖⠒⠒⢤⡀⠀⢀⡼⠿⢇⡣⢬⣶⠷⢿⣤⡾⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⠾⠷⠖⠛⠛⠲⠶⠿⠤⣤⠤⠤⢷⣶⠋⠀⠀⠀⣱⠞⠁⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠓⠒⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """ + Style.RESET_ALL)
    print(f"{Fore.MAGENTA}{Style.BRIGHT}    created by saguny".center(120))
    print(f"{Fore.WHITE}{'─' * 45}".center(120))

def run():
    status_msg = ""
    while True:
        clear_screen()
        show_header()
        
        if status_msg:
            print(f"{status_msg}")
            status_msg = "" # Reset after showing

        url = input(f"\n{Fore.CYAN}[ LINK ] {Fore.WHITE}Paste here >> {Style.RESET_ALL}").strip()
        if not url: continue

        print(f"{Fore.YELLOW}Looking at URL...{Style.RESET_ALL}", end="\r")
        info = downloader.get_video_info(url)
        
        if not info:
            status_msg = f"{Fore.RED}Link invalid. Please try again.{Style.RESET_ALL}"
            continue

        # Sub-loop for selection
        while True:
            clear_screen()
            show_header()
            print(f"{Fore.GREEN}Target: {Style.BRIGHT}{info.get('title', 'Unknown')[:60]}{Style.RESET_ALL}")
            
            if status_msg:
                print(f"{status_msg}")
                status_msg = ""

            print(f"\n{Fore.WHITE}1. {Fore.GREEN}[ Audio ] {GREY}(MP3){Style.RESET_ALL}")
            print(f"{Fore.WHITE}2. {Fore.BLUE}[ Video ] {GREY}(MKV/MP4){Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.WHITE}Selection ( 1 or 2 ) >> {Style.RESET_ALL}").strip()

            if choice == '1':
                downloader.download_audio(url)
                break
            elif choice == '2':
                downloader.download_video(url)
                break
            else:
                status_msg = f"{Fore.RED}Invalid choice. Type 1 or 2.{Style.RESET_ALL}"

        # Sub-loop for exit
        while True:
            print(f"\n{Fore.MAGENTA}1. Download more  |  2. Exit{Style.RESET_ALL}")
            final_choice = input(f"{Fore.WHITE}>> {Style.RESET_ALL}").strip()
            if final_choice == '1':
                return
            elif final_choice == '2':
                print(f"\n{Fore.MAGENTA}See you!{Style.RESET_ALL}")
                time.sleep(1)
                sys.exit()
            else:
                # Clear previous lines to rewrite "Invalid choice"
                print(f"{Fore.RED}Please type 1 or 2.{Style.RESET_ALL}")

if __name__ == "__main__":
    while True:
        try:
            run()
        except KeyboardInterrupt:
            break