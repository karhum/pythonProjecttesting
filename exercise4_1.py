# palindrome: tacocat

txt = input("Give some text:\n")
print(f"txt[:-]")
if not txt:
    print("Your text is empty.")
if txt == txt[:-]:
    print("Palindrome: YES")
else:
    print("Palindrome: NO")
  