def valid_card(n):
    if n[0] != 4 or n[0] != 5 or n[0] != 6:
        print("Invalid")
        for i in range(len(n)):
            if (int(n[i]) >= 0 and int(n[i]) <= 9) == False:
                print("Invalid")
        if len(n) != 16:
            print("Invalid")
            if n[4] != "-" and n[9] != "-" and n[14] != "-":
                print("Invalid")

    else:
        print("Valid")


card_no = int(input())

for i in range(card_no):
    n = str(input())
    valid_card(n)
