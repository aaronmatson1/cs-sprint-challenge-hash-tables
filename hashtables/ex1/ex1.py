def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Your solution should run in linear time.
    # I've recieved a package with a weight limit and a list of weights.
    # create a function `get_indices_of_item_weights` that finds two items whose SUM OF WEIGHTS EQUALS THE WEIGHT LIMIT `limit`.
    # **The higher valued index should be placed in the `zeroth` index and the smaller index should be placed in the `first` index.**_
    # If such a pair doesn’t exist for the given inputs, your function should return `None`. [X]


    cache = {}

    #Edge case

    if length <= 1:
        print("Error! Too short.")
        return None

    for i in range(length):
        current = weights[i]

        if current in cache:
            previous = cache[current]
            return(i, previous)
        cache[limit - weights[i]] = i
    return None
