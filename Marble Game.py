print("There are some marbles on the table and we take 1 or 2 each turn.")
print("Who takes the last wins.")
n = int(input("How many marbles should we start with? "))
if n % 3 == 0:
    # Play second
    print("I play second. You start.")
else:
    # Play first
    print("I play first.")
    m = n % 3
    n = n - m
    print(f"I take {m}.")
while n > 0:
    print(f"There is {n} marbles left.")
    m = int(input("It's your turn. How many you take? "))
    if m < 1 or m > 2:
        print(f"I got you. I said take 1 or 2, not {m}.")
        m = int(input("Choose again "))
    n -= m

    m = n % 3
    n = n - m
    print(f"I take {m}.")

print("I won. Easy")    