import math

def binary_search_explanation(data_list, target):
    """
    This function demonstrates O(log n) - Logarithmic Time Complexity.
    
    Logarithmic time means that the time (number of steps) increases 
    proportionally to the logarithm of the input size (n). 
    In practical terms: every time you double the size of the input, 
    you only add ONE additional step to the process.
    """

    low = 0
    high = len(data_list) - 1
    steps = 0

    print(f"Searching for {target} in a list of size {len(data_list)}....")

    while low <= high:
        steps += 1
        # In each step we find the middle of the current range
        mid = (low + high) // 2
        guess = data_list[mid]

        print(f"Step {steps}: Checkd index {mid} (Value: {guess})")

        if guess == target:
            print(f"-> Sucess! Found {target} in {steps} steps")

            return steps
        
        # LOGARITHMIC MAGIC HAPPENS HERE
        # We don't just move one item at a time (which would be O(n))
        # We discord HALF of the remaining search area in every single step

        if guess > target:
            # Target is in lower half, discard the upper half
            high = mid + 1
        else: 
            # Target is in the uper half, discard the lower half
            low = mid + 1

    print(f"-> {target} not found after {steps} steps.")

    return steps





def run_demonstration():
    # 1. Setup an input of size 1,000 (n = 1000)
    # Since log2(1000) is approx 10, it should take ~10 steps max
    size_n = 1000
    test_data = list(range(size_n))

    print("-" * 30)
    print(f"SCENARIO 1: n = {size_n}")
    print("-" * 30)
    steps_small = binary_search_explanation(test_data, 999)

    # 2. Setup an input of size 1,000,000 (n = 1,000,000)
    # Even though the size increased by 1,000x, the steps will barely increase
    # log2(1,000,000) is approx 20
    size_huge = 1_000_000
    test_data_huge = list(range(size_huge))

    print("-" * 30)
    print(f"SCENARIO 2: n = {size_huge} (1,000x target!)")
    print("-" * 30)
    steps_large = binary_search_explanation(test_data_huge,999999)

    print("-" * 30)
    print("THE LOGARITHMIC CONCLUSION")
    print(f"Input size increased by: {size_huge // size_n} x")
    print(f"Steps only increased by : {steps_large - steps_small} additional steps.")
    print("Thi is why O( log n) is extremely efficient for large datasets")
    print("-" *30)



if __name__ == "__main__":
    run_demonstration()



"""
WHY IS THIS LOGARITHMIC?
------------------------
Imagine you have 128 items.
Step 1: 128 -> 64  left
Step 2: 64  -> 32  left
Step 3: 32  -> 16  left
Step 4: 16  -> 8   left
Step 5: 8   -> 4   left
Step 6: 4   -> 2   left
Step 7: 2   -> 1   left (Found!)

Mathematically: 2^7 = 128. 
Therefore, log2(128) = 7.
The number of steps is the exponent you need to raise 2 to in order to get n.
"""