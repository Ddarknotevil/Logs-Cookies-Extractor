import os
import concurrent.futures
import platform
import threading
import shutil
from colorama import Fore, Back, Style, init
import logging
import colorama
import subprocess
import sys

# Set up logging 
logging.basicConfig(filename='requirements-state.log', level=logging.INFO)

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of requirements
required_packages = ['requests', 'colorama']

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
print_lock = threading.Lock()

def discord_cookie_extractor():
    processed_cookies = set() 

    site = input("\033[93mEnter the site for which you want to extract cookies: \033[0m")

    # extract cookies and eat them <3
    def extract_data(file_path, original_folder, site, output_pattern):
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    cookies = file.readlines()
                    for cookie in cookies:
                        if site in cookie:
                            cookie = cookie.strip()
                            if cookie and cookie not in processed_cookies:
                                processed_cookies.add(cookie)  
                                if output_pattern == "1":
                                    with open('Full_output.txt', 'a', encoding='utf-8') as output_file_without_dir:
                                        output_file_without_dir.write(f'{cookie}\n')
                                elif output_pattern == "2":
                                    if not os.path.exists('Multi_Output'):
                                        os.makedirs('Multi_Output')
                                    with open(f'Multi_Output/cookie_{len(processed_cookies)}.txt', 'w', encoding='utf-8') as output_file_individual:
                                        output_file_individual.write(f'{cookie}\n')
                                print("\033[92m Please Wait \033[0m", end="", flush=True)  
                                print(colorama.Fore.MAGENTA + '''
________________________________█████_____█████
______________________________███____██_██_____███
_____________________________██________██__________██
____________________________██__________█____________██
________██████____________██_______With Love_________██
_____███████████________██__________By______________██
____█████████████_______██_Crcked.io/Ddarknotevil██
___███████████████______██______________________██
___████████████████______██___________________██
___████████████████_______██_________________██
____███████████████_______███_______________██
_______███████████_______██__██_____________██
___________███████______████___██__________██
____██████__██████████████_____██____    _██
__██████████████████████________██_██_███ ██
_████████████████████_____________████████
██_█████_████████████_______________
█__█_██__████████████
_____█__████████████               
_______█████████████                           Drink Coffee & Eat cookies..
_______██████████████                                       
_______███████████████                                                         
________███████████████                                        
_______███████__████████                                        
______███████_____███████                                   
____█████████________██████

    ''' + colorama.Style.RESET_ALL)
            except UnicodeDecodeError:
                pass

    def traverse_dir(dir_path, num_threads, site, output_pattern):
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            for foldername, subfolders, filenames in os.walk(dir_path):
                if 'Cookies' in subfolders:
                    cookies_folder = os.path.join(foldername, 'Cookies')
                    for filename in os.listdir(cookies_folder):
                        if filename.endswith('.txt'):  # Check if the file is a .txt file
                            file_path = os.path.join(cookies_folder, filename)
                            executor.submit(extract_data, file_path, foldername, site, output_pattern)

    start_dir = os.getcwd()

    num_threads = int(input("\033[93mEnter the number of threads you want to use: \033[0m"))
    output_pattern = input("\033[93mChoose an output pattern: 1 for all cookies in one output, 2 for each cookie in a separate file: \033[0m")

    traverse_dir(start_dir, num_threads, site, output_pattern)

def main():
    while True:
        clear_console()
        init()
        columns, rows = shutil.get_terminal_size()
        print(Fore.MAGENTA + '\n' * (rows // 2 - 6))
        print(' ' * (columns // 2 - 20) + '+' + '-' * 40 + '+')
        print(' ' * (columns // 2 - 20) + "| Please enter a number:                  |")
        print(' ' * (columns // 2 - 20) + "|                                        |")
        print(' ' * (columns // 2 - 20) + "| \033[1m\033[92m 1 Extract Cookies\033[0m ")
        print(' ' * (columns // 2 - 20) + "| \033[1m\033[91m 2. Exit\033[0m                               ")
        print(' ' * (columns // 2 - 20) + '+' + '-' * 40 + '+' + Style.RESET_ALL)    
        choice = input("Enter your choice: ")
        if choice == "1":
            discord_cookie_extractor()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
