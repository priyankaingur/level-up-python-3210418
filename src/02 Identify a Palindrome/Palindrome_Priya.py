def is_Palindrome(txt):
    rev = txt.lower()[::-1].replace(" ", "")
    fwd = txt.lower().replace(" ", "")
    return fwd == rev


print(is_Palindrome("Malayalam"))
print(is_Palindrome("Go hang a salami Im a lasagna hog"))
