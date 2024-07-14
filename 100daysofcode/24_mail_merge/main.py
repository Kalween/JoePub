with open("my_file.txt", mode='r') as file:
    content = file.read()
    print(content)

# with open("my_file.txt", mode="w") as file:
#     file.write("\nTest new test")