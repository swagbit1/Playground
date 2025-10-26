user = input("File: ").lower()

if user.endswith(".gif"):
    print(f"image/gif")
elif user.endswith(".jpg"):
    print(f"image/jpg")
elif user.endswith(".jpeg"):
    print(f"image/jpeg")
elif user.endswith(".png"):
    print(f"image/png")
elif user.endswith(".pdf"):
    print(f"image/pdf")
elif user.endswith(".txt"):
    print(f"image/txt")
elif user.endswith(".zip"):
    print(f"image/zip")
else:
    print("application/octet-stream")
    