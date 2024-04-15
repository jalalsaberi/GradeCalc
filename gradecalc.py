def convert_grade():
    iran_grade = float(input("Enter an Iranian 20-point grade: \n"))
    if iran_grade < 0 or iran_grade > 20:
        print("Iranian grade must be between 0 and 20\n")
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
      print(f"Iranian Grade: {iran_grade}\nGPA: {round(gpa, 3)}\nPercentage: {round(percent, 2)}\nLetter Grade: {letter_grade}")
      
convert_grade()