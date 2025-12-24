name="Hello world #"
count1=0
count2=0
count3=0

for letter in name:
    if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
        count1+=1
    else:
        count2+=1
    if letter=="!" or letter=="?" or letter=="." or letter=="#":
        count3+=1

if name==name[::-1]:
       print(name,"is a palindrome")
else:
       print(name,"is not a palindrome")

freq={}
for ch in name:
    freq[ch]=freq.get(ch,0)+1

print('vovels ',count1)
print('consonants ',count2)
print('special charecter ',count3)
print(name[::-1])
print(freq)



