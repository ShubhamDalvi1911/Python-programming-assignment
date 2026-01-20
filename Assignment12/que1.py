# Write a program which accepts one character and checks whether it is vowel or consonant.
def IsVowel(Ch):
    # if Ch == 'a' or Ch == 'e' or Ch == 'i' or Ch == 'o' or Ch == 'u' or Ch == 'A' or Ch == 'E' or Ch == 'I' or Ch == 'O' or Ch == 'U':
    #     return True
    # else:
    #     return False
    
    tup = ('a','e','i','o','u','A','I','E','O','U')
    for i in tup:
        if Ch == i:
            return True
        else: 
            return False

def main():
    Ch = input("Enter a character to check whether is vowel or not : ")
    result = IsVowel(Ch)
    if result == True:
        print("Vowel")
    else:
        print("Not Vowel")

if __name__ == "__main__":
    main()