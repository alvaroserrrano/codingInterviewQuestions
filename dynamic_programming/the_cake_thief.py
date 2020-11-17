"""

u are a renowned thief who has recently switched from stealing precious metals to stealing cakes because of the insane profit margins. You end up hitting the jackpot, breaking into the world’s largest privately owned stock of cakes—the vault of the Queen of England.

While Queen Elizabeth has a limited number of types of cake , she has an unlimited supply of each type .

Each type of cake has a weight and a value, stored in a tuple with two indices:

An integer representing the weight of the cake in kilograms
An integer representing the monetary value of the cake in British shillings
For example:

# Weighs 7 kilograms and has a value of 160 shillings
(7, 160)

# Weighs 3 kilograms and has a value of 90 shillings
(3, 90)
You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.

Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity , and returns the maximum monetary value the duffel bag can hold.

For example:

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

# Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
max_duffel_bag_value(cake_tuples, capacity)
Weights and values may be any non-negative integer. Yes, it’s weird to think about cakes that weigh nothing or duffel bags that can’t hold anything. But we’re not just super mastermind criminals—we’re also meticulous about keeping our algorithms flexible and comprehensive.
"""
def get_max_value(cake_tuples, max_capacity):
    #index is the capacity and value is the value at that capacity
    max_vals_at_capacity = [0] * (capacity + 1)
    for capacity in range(max_capacity + 1):
        current_max = 0
        for weight, value in cake_tuples:
            #edge cases
            if(weight == 0 and value > 0):
                return float('inf')
            if(weight == 0 and value == 0):
                return 0
            #valid cake to include in the bag
            if(weight <= capacity):
                max_val_using_cake = value + max_vals_at_capacity[capacity-weight]
                current_max = max(current_max, max_val_using_cake)
        max_vals_at_capacity[capacity] = current_max
    return max_vals_at_capacity[max_capacity]
