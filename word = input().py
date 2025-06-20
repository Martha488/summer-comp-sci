word= input("enter your word: ")
copy= ""
for char in word:
        copy= (char + copy)
print(copy)
if word == copy:
    print("palindrome!")
else:
      print("not a palindrome")