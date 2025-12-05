# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = input("Function: ")
    if function == "0":
        break
    elif function == "1":
        with open("diary.txt", "a") as file:
            file.write(input("Diary entry: ") + "\n")
            print("Diary saved\n")
    elif function == "2":
        with open("diary.txt") as file:
            print(file.read())
print("Bye now!")