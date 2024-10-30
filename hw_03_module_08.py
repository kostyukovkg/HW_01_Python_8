import numpy as np

def guess_function(number:int=1) -> int:
    """Takes a given number and tries to guess it with a given algorithm

    Args:
        number (int, optional): hidden number. Defaults to 1.

    Returns:
        int: number of tries
    """
    # first random prediction 
    predict = np.random.randint(1, 100)

    # number of tries
    count = 0
    # we save unsuccessful attempts to restate the borders later
    # first stated highest and lowest borders
    predict_h = 101
    predict_l = 1
    while True:
        # counter
        count+=1
        # if first prediction is more than a number, 
        # remember the prediction as a high bound and make a new guess given new borders
        if predict > number:
            predict_h = predict
            predict = np.random.randint(predict_l, predict_h)
        # if first prediction is less than a number, 
        # remember the prediction as a low bound and make a new guess given new borders
        elif predict < number:
            predict_l = predict
            predict = np.random.randint(predict_l, predict_h)
        else:
            print (f'Your number is {number}, number of tries: {count}')
            break
    return count

def guess_function_2(number:int=1) -> int:
    """Takes a given number and tries to guess it with a given algorithm

    Args:
        number (int, optional): hidden number. Defaults to 1.

    Returns:
        int: number of tries
    """
    # first prediction 
    predict = 50 
    # number of tries
    count = 0
    # we save unsuccessful attempts to restate the borders later
    # first stated highest and lowest borders
    predict_h = 101
    predict_l = 1
    while True:
        # counter
        count+=1
        # if first prediction is more than a number, 
        # remember the prediction as a high bound and make a new guess given new borders
        if predict > number:
            predict_h = predict
            predict = int((predict_h + predict_l) / 2)
        # if first prediction is less than a number, 
        # remember the prediction as a low bound and make a new guess given new borders
        elif predict < number:
            predict_l = predict
            predict = int((predict_h + predict_l)/2)
        else:
            print (f'Your number is {number}, number of tries: {count}')
            break
    return count

def guess_game(guess_function) -> int:
    """Generates a random array of integers and calculates average number of tries to guess

    Args:
        guess_function (_type_): function to guess the hidden number

    Returns:
        int: average number of tries to guess
    """
    
    # make a list to fill with random 1000 numbers
    count_ls = []
    # fix the seed
    np.random.seed(1) 
    # random array statement
    random_array = np.random.randint(1, 100, 1000)
    
    # add a number of tries required to guess a given 'number'
    for number in random_array:
        count_ls.append(guess_function(number))
    
    # calculate average number of tries
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


guess_game(guess_function_2)