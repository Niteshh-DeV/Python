import re

def is_anagram(str1,str2):
    str1 = re.sub(r'[^a-zA-Z0-9]','' ,str1).lower()
    print (str1)
    str2 = re.sub(r'[^a-zA-Z0-9]', '',str2).lower()
    print (str2)
    if sorted(str1)==sorted(str2):
        print("Anagram")
    else:
        print("Not Anagram")
        

print ("Input Strings")
str1=input()
str2=input()

is_anagram(str1,str2)