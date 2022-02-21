from datetime import date

import StudentClass as s

def main():

    studentone = s.Student(123,"Bob","1/1/2000","F")

    studentone.set_age()
    studentone.set_registration("sr")

    print(studentone.get_age())
    print("Your registration date is:",studentone.get_registration())



main()