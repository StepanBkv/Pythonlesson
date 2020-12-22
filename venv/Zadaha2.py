all_numbers = set(range(0, int(input()) + 1))

while (data := input()) != "HELP" :
    if data == "YES":
        all_numbers &= in_numbers
    elif data == "NO":
        all_numbers -= in_numbers
    else:
        in_numbers = set(map(int, data.split()))
    print(all_numbers)
print(*sorted(all_numbers))