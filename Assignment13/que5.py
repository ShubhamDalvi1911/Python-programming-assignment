# Write a program which accepts marks and display grade
'''Condition Example:
    >= 75  --> Distinction
    >= 60  --> First Class
    >= 50  --> Second Class
    < 75  --> Fail'''
def Grade(Marks):
    if Marks >= 75:
        return "Distiction"
    elif Marks >= 60:
        return "First Class"
    elif Marks >= 50:
        return "Second Class"
    else:
        return "Fail"

def main():
    No = int(input("Enter the marks : "))
    result = Grade(No)
    print(result)
   
if __name__ == "__main__":
    main()