import yt_dlp
import os
from colorama import Fore, Style, init

init(autoreset=True)

def setup_folders():
    base_dir = "Downloads"
    video_dir = os.path.join(base_dir, "Videos")
    audio_dir = os.path.join(base_dir, "Audios")
    os.makedirs(video_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)
    return video_dir, audio_dir

def get_video_info(url):
    ydl_opts = {'quiet': True, 'no_warnings': True, 'noplaylist': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            return ydl.extract_info(url, download=False)
        except Exception:
            return None

def download_audio(url):
    _, audio_dir = setup_folders()
    print(f"\n{Fore.YELLOW}Downloading...{Style.RESET_ALL}")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{audio_dir}/%(title)s.%(ext)s',
        'ffmpeg_location': '.',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloaded_file = ydl.prepare_filename(info)

        print(f"{Fore.GREEN}Audio download finished.{Style.RESET_ALL}")
        
        while True:
            choice = input(f"\n{Fore.CYAN}Convert Audio? (e.g., mp3, wav, flac, m4a) or 'no' if you don't want to convert >> {Style.RESET_ALL}").lower().strip()
            
            if choice == 'no':
                break
            
            valid_audio_formats = ['mp3', 'wav', 'flac', 'm4a', 'ogg', 'aac']
            target_format = choice.replace('.', '')
            
            if target_format in valid_audio_formats:
                print(f"{Fore.YELLOW}Converting to {target_format.upper()}...{Style.RESET_ALL}")
                output_name = f"{os.path.splitext(downloaded_file)[0]}.{target_format}"
                
                if os.path.exists(output_name):
                    output_name = f"{os.path.splitext(downloaded_file)[0]}_alt.{target_format}"

                os.system(f'ffmpeg -i "{downloaded_file}" -ab 192k "{output_name}" -loglevel quiet')
                print(f"{Fore.GREEN}Created {target_format.upper()}.{Style.RESET_ALL}")
                
                while True:
                    print(f"\n{Fore.WHITE}Keep original source file?")
                    print(f"{Fore.WHITE}1. {Fore.GREEN}Yes, keep it")
                    print(f"{Fore.WHITE}2. {Fore.RED}No, delete it")
                    cleanup = input(f"{Fore.WHITE}>> {Style.RESET_ALL}").strip()
                    
                    if cleanup == '1':
                        break
                    elif cleanup == '2':
                        try:
                            os.remove(downloaded_file)
                            print(f"{Fore.YELLOW}Original source file deleted.{Style.RESET_ALL}")
                        except Exception as e:
                            print(f"{Fore.RED}Could not delete file: {e}")
                        break
                    else:
                        print(f"{Fore.RED}Select 1 or 2.{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Unsupported format. Try mp3, wav, flac, etc.{Style.RESET_ALL}")
                
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def download_video(url):
    video_dir, _ = setup_folders()
    print(f"\n{Fore.YELLOW}Downloading...{Style.RESET_ALL}")
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{video_dir}/%(title)s.%(ext)s',
        'merge_output_format': 'mkv', 
        'ffmpeg_location': '.',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloaded_file = ydl.prepare_filename(info)
            if 'merge_output_format' in ydl_opts:
                base, _ = os.path.splitext(downloaded_file)
                downloaded_file = f"{base}.mkv"

        print(f"{Fore.GREEN}Download finished.{Style.RESET_ALL}")
        
        while True:
            choice = input(f"\n{Fore.CYAN}Convert? (Enter format like mp4, wav, m4a, avi) or 'no' if you don't want to convert >> {Style.RESET_ALL}").lower().strip()
            
            if choice == 'n':
                break
            
            audio_only_formats = ['mp3', 'wav', 'flac', 'm4a', 'ogg', 'aac']
            video_formats = ['mp4', 'avi', 'mov', 'flv', 'mkv']
            all_valid = audio_only_formats + video_formats
            
            target_format = choice.replace('.', '')
            
            if target_format in all_valid:
                # Check if it's an audio format and warn the user
                if target_format in audio_only_formats:
                    warn = input(f"{Fore.RED}[!] This will convert the downloaded video into an {Fore.RED}{Style.BRIGHT}Audio{Style.NORMAL}{Fore.RED}. Are you sure? (y/n) >> {Style.RESET_ALL}").lower().strip()
                    if warn != 'y':
                        continue

                print(f"{Fore.YELLOW}Converting to {target_format.upper()}...{Style.RESET_ALL}")
                output_name = f"{os.path.splitext(downloaded_file)[0]}.{target_format}"
                
                if os.path.exists(output_name):
                    output_name = f"{os.path.splitext(downloaded_file)[0]}_converted.{target_format}"

                os.system(f'ffmpeg -i "{downloaded_file}" "{output_name}" -loglevel quiet')
                print(f"{Fore.GREEN}Created {target_format.upper()}.{Style.RESET_ALL}")
                
                while True:
                    print(f"\n{Fore.WHITE}Keep original MKV file?")
                    print(f"{Fore.WHITE}1. {Fore.GREEN}Yes, keep it")
                    print(f"{Fore.WHITE}2. {Fore.RED}No, delete it")
                    cleanup = input(f"{Fore.WHITE}>> {Style.RESET_ALL}").strip()
                    
                    if cleanup == '1':
                        break
                    elif cleanup == '2':
                        try:
                            os.remove(downloaded_file)
                            print(f"{Fore.YELLOW}Original file deleted.{Style.RESET_ALL}")
                        except Exception as e:
                            print(f"{Fore.RED}Could not delete file: {e}")
                        break
                    else:
                        print(f"{Fore.RED}Select 1 or 2.{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Unsupported or invalid format.{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")