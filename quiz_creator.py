import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

# Display the banner
def display_banner():
    banner = pyfiglet.figlet_format("Quiz Creator", font="slant")
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + banner)

def main():
    display_banner()
    print(Fore.MAGENTA + "Welcome to the Quiz Creator!")
    print(Fore.LIGHTMAGENTA_EX + "Created by: Jonalyn Antoc from BSCpE 1-1")
    print(Fore.MAGENTA + "Type 'exit' anytime to stop.\n")
    
    question_count = 0
    
    while True:
        # Get question input from the user
        question_text = input(Fore.BLUE + "Enter your question: ").strip()
        if question_text.lower() == 'exit':
            break

if __name__ == "__main__":
    main()