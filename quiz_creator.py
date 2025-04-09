import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

# Display the banner
def display_banner():
    banner = pyfiglet.figlet_format("Quiz Creator", font="slant")
    print(Style.BRIGHT + Fore.BLUE + banner)

def main():
    display_banner()
    print(Fore.MAGENTA + "Welcome to the Quiz Creator! Type 'exit' anytime to stop.\n")

if __name__ == "__main__":
    main()