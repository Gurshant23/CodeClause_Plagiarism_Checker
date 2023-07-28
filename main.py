
from difflib import SequenceMatcher


original = input("Enter the original line : ")
tocheckfor = input("Enter the line that you have written : ")


match = SequenceMatcher(None, original, tocheckfor)


result = match.ratio() * 100


print(int(result), "%")
