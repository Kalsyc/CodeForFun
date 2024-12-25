"""
You're hosting an event at a food festival and want to showcase the best possible pairing of two dishes from the festival that complement each other's flavor profile.

Each dish has a flavor profile represented by an integer. A negative integer means a dish is sweet, while a positive integer means a dish is savory. The absolute value of that integer represents the intensity of that flavor. For example, a flavor profile of -3 is slightly sweet, one of -10 is extremely sweet, one of 2 is mildly savory, and one of 8 is significantly savory.

You're given an array of these dishes and a target combined flavor profile. Write a function that returns the best possible pairing of two dishes (the pairing with a total flavor profile that's closest to the target one). Note that this pairing must include one sweet and one savory dish. You're also concerned about the dish being too savory, so your pairing should never be more savory than the target flavor profile.

All dishes will have a positive or negative flavor profile; there are no dishes with a 0 value. For simplicity, you can assume that there will be at most one best solution. If there isn't a valid solution, your function should return [0, 0]. The returned array should be sorted, meaning the sweet dish should always come first.
"""

def sweetAndSavory(dishes, target):
    sweet_dishes = sorted([dish for dish in dishes if dish < 0], key=abs)
    savory_dishes = sorted([dish for dish in dishes if dish > 0])
    
    best_pair = [0, 0]
    best_diff = float("inf")
    sweet_pointer, savory_pointer = 0, 0
    
    while sweet_pointer < len(sweet_dishes) and savory_pointer < len(savory_dishes):
        curr_value = sweet_dishes[sweet_pointer] + savory_dishes[savory_pointer]
        if curr_value <= target:
            curr_diff = target - curr_value
            if curr_diff < best_diff:
                best_diff = curr_diff
                best_pair = [sweet_dishes[sweet_pointer], savory_dishes[savory_pointer]]
            savory_pointer += 1
        else:
            sweet_pointer += 1
    return best_pair

"""
Time Complexity: O(nlog(n) + mlog(m)) where n is the number of sweet dishes and m is the number of savory dishes
Space Complexity: O(n + m) where n is the number of sweet dishes and m is the number of savory dishes

The time complexity is O(nlog(n) + mlog(m)) because we sort the sweet and savory dishes before iterating through them. The space complexity is O(n + m) because we store the sorted sweet and savory dishes in separate arrays.

The idea is to sort the sweet and savory dishes and then iterate through them using two pointers. We keep track of the best pair of dishes that is closest to the target sum. 
We update the best pair if the current pair has a smaller difference with the target sum. We move the pointers based on the sum of the current pair and the target sum.
"""