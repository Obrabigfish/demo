#!/usr/bin/python3
print("Hello")
name = input("What is your name")
name_length = len(name)
print(name_length)
if name_length > 5:
    print(f"Your name has {name_length} chafracters")
else:
    print(f"{name_length} Few characters")
