import emoji

user = input("Input: ")

if '_' in user:
    print(emoji.emojize(user))
else:
    print(emoji.emojize(user, language='alias'))