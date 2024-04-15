from colorama import Fore, Style, init

init()

def convert_grade():
    iran_grade = float(input(f"{Fore.YELLOW}Enter an Iranian 20-point grade:{Style.RESET_ALL} "))
    if iran_grade < 0 or iran_grade > 20:
        print(f"{Fore.RED}Iranian grade must be between 0 and 20{Style.RESET_ALL}\n")
        convert_grade()
    else:
      gpa = (iran_grade / 20) * 4
      percent = (iran_grade / 20) * 100
      letter_grade = ""
      if iran_grade >= 17:
          letter_grade = "A"
      elif iran_grade >= 15:
          letter_grade = "B"
      elif iran_grade >= 12:
          letter_grade = "C"
      elif iran_grade >= 10:
          letter_grade = "D"
      else:
          letter_grade = "F"
      print(f"\n{Fore.YELLOW}Iranian Grade: {Fore.CYAN}{iran_grade}\n{Fore.YELLOW}GPA: {Fore.CYAN}{round(gpa, 3)}\n{Fore.YELLOW}Percentage: {Fore.CYAN}{round(percent, 2)}\n{Fore.YELLOW}Letter Grade: {Fore.CYAN}{letter_grade}{Style.RESET_ALL}")
      
convert_grade()
