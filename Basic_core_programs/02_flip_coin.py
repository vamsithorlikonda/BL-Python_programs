import random

def flip_coin(num_flips):
    if num_flips <= 0:
        return print("Please enter a positive integer.")

    heads_count = 0
    tails_count = 0

    for i in range(num_flips):
        if random.random() < 0.5:
            heads_count += 1
        else:
            tails_count += 1

    total_flips = heads_count + tails_count
    heads_percentage = (heads_count / total_flips) * 100
    tails_percentage = (tails_count / total_flips) * 100

    print(f"Total Flips: {total_flips}")
    print(f"Heads: {heads_count} ({heads_percentage:.2f}%)")
    print(f"Tails: {tails_count} ({tails_percentage:.2f}%)")

num_flips = int(input("Enter the number of times to flip the coin: "))
flip_coin(num_flips)