def nfruits(dictionary, string):
    """
    Python is an MIT student who loves fruits.
    He carries different types of fruits (represented by capital letters) daily from his house to the MIT campus to eat on the way.
    But the way he eats fruits is unique.
    After each fruit he eats (except the last one which he eats just on reaching the campus),
    he takes a 30 second break in which he buys 1 fruit of each type other than the one he just had.
    determine the maximum quantity out of the different types of fruits that is present with Python when he has reached the campus?
    """
    i = 0
    string = sorted(string)

    for idx, char in enumerate(string):
        # Update the fruit Python ate
        dictionary[char] -= 1
        # update others he bought, skip this on the last step
        if idx < len(string) - 1:
            for key in dictionary:
                if key != char:
                    dictionary[key] += 1
    # returning the maximum number of fruit    
    return dictionary[max(dictionary, key = dictionary.get)]