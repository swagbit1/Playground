def main():
    time = input("Time: ")
    hrs = convert(time)

    if hrs >= 7 and hrs <= 8:
        print("breakfast time")
    elif hrs >= 12 and hrs <= 13:
        print("lunch time")
    elif hrs >= 18 and hrs <= 19:
        print("dinner time")

    


def convert(time):
    hr, min = time.strip().split(":")

    return (float (hr)) + (float (min))/60


if __name__ == "__main__":
    main()