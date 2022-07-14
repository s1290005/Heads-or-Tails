import random

print("Who are you?")
print("> ")
name = input()
print("Hello, " + name + "!")

print("Tossing a coin...")

head = 0
tail = 0
for i in range(3):
    print("Round " + str(i+1) + ": ")
    coin = random.randint(0, 1)
    if coin == 0:
        print("Heads")
        head += 1
    if coin == 1:
        print("Tails")
        tail += 1
