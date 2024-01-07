# Task 1
# start by intilizing the necessary variables such as n to store the length of price array , span as an array of zeros to store the stock span, and set the span of first day to 1 

# Task 2: Transverse through the prices
# Iterate through the prices array from the second to the last day

# Task 3: Initialise Span and Index
# For each day, initialise a variable ’span’ to 1 to represent the current span and an index ‘j’ to set ‘I-1’  to start back traversal.

# Task 4: Backward Traversal
# Traverse backward from current day until a greater price is found or the start of the series is reached

# Task 5: Calculate Span
# Within the backward traverse loop, add the span of previous day to the current span if the current day span is greater than or equal to the previous day’s price.Update the index  ‘j’ to ‘j-span[j]’.

# Task 6: Stored Calculated Span
# Once the backward traversal is complete, store the calculated span for the current day in the spans array at index ‘i’

# Task 7: Repeat
# Repeat steps 3-6 for the remaining days in the prices array.
    
def calculateSpan(prices):
    n = len(prices)  # Length of the prices array
    span = [0] * n  # Initialize span array with zeros
    span[0] = 1  # Span for the first day is always 1

    # Iterate through the prices array starting from the second day
    for i in range(1, n):
        span[i] = 1  # Initialize span for the current day as 1
        j = i - 1  # Set j to the previous day

        # Backward traversal to find the span
        while j >= 0 and prices[j] <= prices[i]:
            span[i] += span[j]  # Add the span of the previous day
            j -= span[j]  # Update j to jump back by the span of day j

        # Task 6: Store the calculated span for the current day
        # This is done implicitly as we are updating span[i] in the loop

    return span

# Example usage
prices = [100, 80, 60, 70, 60, 75, 85]
print("The stock spans are:", calculateSpan(prices))
