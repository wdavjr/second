word = "bottles"

for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")

    print(beer_num, word, "of beer.")

    print(beer_num, word, "Take one down.")

    print(beer_num, word, "Pass it around.")

    if beer_num == 1:

        print("No more bottles of beer on the wall.")

    else:

        new_num = beer_num - 1

        if new_num == 1:

            word = "bottle"

        print(new_num, word, "of beer on the wall.")

print()
