def convert(face):
    face = face.replace(":)", "🙂")
    face = face.replace(":(","🙁")
    return face

def main():
    user = input("Input: ")
    print(convert(user))

main()