import os

print('What is the text you want to replace?')
oldText = input()
print('What is the new text you want to replace?')
newText = input()

print('You are replacing \"' + oldText + '\" text with \"' + newText + '\"')

[os.rename(f, f.replace(oldText, newText)) for f in os.listdir('.') if not f.startswith('.')]

print('Your changes are now complete!')

input("Press enter to exit")