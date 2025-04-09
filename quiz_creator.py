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
        
        # Get the possible answer from the user
        answer_a = input("Choice A: ")
        answer_b = input("Choice B: ")
        answer_c = input("Choice C: ")
        answer_d = input("Choice D: ")
        
        # Get the correct answer input from the user
        correct_choice = input("Correct answer a/b/c/d: ").lower()
        if correct_choice not in ['a', 'b', 'c', 'd']:
            print(Fore.RED + "Invalid answer choice, Please choose a valid option.\n")
            continue
        
        # Save the question and answer to a txt file
        with open("quiz.txt", "a", encoding="utf-8") as quiz_file:
            quiz_file.write(f"Question: {question_text}\n")
            quiz_file.write(f"a) {answer_a}\n")
            quiz_file.write(f"b) {answer_b}\n")
            quiz_file.write(f"c) {answer_c}\n")
            quiz_file.write(f"d) {answer_d}\n")
            quiz_file.write(f"Answer: {correct_choice}\n")
            quiz_file.write("---\n")
            
        # Show a swummary of the question previously added
        print(Fore.GREEN + "\n Question saved!")
        print(Fore.YELLOW + f"Question: {question_text}")
        print(f"a) {answer_a}")
        print(f"b) {answer_b}")
        print(f"c) {answer_c}")
        print(f"d) {answer_d}")
        print(Fore.GREEN + f"Correct Answer: {correct_choice}\n")
        
        question_count += 1
        print(Fore.GREEN + f"Question #{question_count} saved!\n")
        
        # Ask if the user wants to add another question
        while True:
            add_another = input("Add another question? (yes/no): ").strip().lower()
            if add_another in ["yes","no"]:
                break
            elif not add_another: # Handle the errors if ever there is
                print(Fore.RED + "Please type 'yes' or 'no' only.")
            else:
                print(Fore.RED + "Please type 'yes' or 'no' only.")
        
        if add_another == "no":
            break
    
    print(Fore.LIGHTMAGENTA_EX + f"\n{question_count} question(s) saved to 'quiz.txt'. ")
    print(Fore.MAGENTA + "Thank you!")
    
if __name__ == "__main__":
    main()