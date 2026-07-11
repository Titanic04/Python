import string 
import random

a=input("enter your messege : ")
words=a.split()
encoded_words=[]
def encoding():
        for word in words:
             
            if len(word)<3:
                encoded_words.append(word[::-1])                  # if len(a)==2:
                                                          #     print(a[1]+a[0])
                                                          # elif len(a)==1:
                                                          #     print(a[0])
                                                          # elif len(a)==0:
                                                          #     print()

            else:
                prefix=''.join(random.choices(string.ascii_lowercase,k=3))
                suffix=''.join(random.choices(string.ascii_lowercase,k=3))
                encoded_words.append(prefix+word[1:]+word[0]+suffix)
encoding()
print(' '.join(encoded_words))