import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

# Display the banner
def display_banner():
    banner = pyfiglet.figlet_format("Quiz Creator", font="slant")
    print(Style.BRIGHT + Fore.BLUE + banner)

def main():
    display_banner()

if __name__ == "__main__":
    main()