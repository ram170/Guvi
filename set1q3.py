s=input()
if(s=='a' or s=='e' or s=='i' or s=='o' or s=='u' or s=='A' or s=='E' or s=='I' or s=='O' or s=='U'):
    print("Vowel")
elif(ord(s)>=97 and ord(s)<=122):
    print("Consonant")
elif(ord(s)>=65 and ord(s)<=90):    
    print("Consonant")
else:
    print("invalid")
    
    
