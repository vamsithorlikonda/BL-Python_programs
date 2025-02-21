import random

def generate_random_coupon(n):
    return random.randint(1, n)

def collect_all_coupons(n):
    collected_coupons = set()
    total_random_numbers = 0

    while len(collected_coupons) < n:
        coupon = generate_random_coupon(n)
        collected_coupons.add(coupon)
        total_random_numbers += 1

    return total_random_numbers

# input
n = int(input("Enter the number of distinct coupons: "))

collect_all_coupons(n)

# Displaying the output
print(f"Total random numbers generated to collect all {n} distinct coupons: {collect_all_coupons(n)}")
