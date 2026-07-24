def print_song_line(bottle_number):
    print()
    print(f"{bottle_number} bottle{'' if bottle_number == 1 else 's'} of beer on the wall.")
    print(f"{bottle_number} bottle{'' if bottle_number == 1 else 's'} of beer.")
    print(f"Grab one down, pass it around.")
    bottle_number = bottle_number - 1
    print(f"{bottle_number} bottle{'' if bottle_number == 1 else 's'} of beer on the wall.")

    return bottle_number

bottle_number = 99

while bottle_number > 0:
    bottle_number = print_song_line(bottle_number)



