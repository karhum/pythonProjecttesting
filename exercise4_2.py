# palindrome: tacocat

txt = input("Give some text:\n")
print(txt[::-1])
if not txt:
    print("Your text is empty.")
elif txt == txt[::-1]:
    print("Palindrome: YES")
else:
    print("Palindrome: NO")
