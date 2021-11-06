
def fibonacci(n):
    '''
    this function take n from user and it will return the febonacci series
    '''

    if n == 0:
        return 0

    elif n==1 :
        return 1

    else :
        return (fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    '''
    you insert the n value and the function return the nth value and whole series of lucas series
    '''
    if n == 0:
        return 2

    elif n==1 :
        return 1
    else :
        return lucas(n-1) + lucas(n-2)


   
def sum_series(n,firstEle=0,secondEle=1):
    '''
    you insert the nth value and the firstEle and secondEle is optional and it should return the nth value and whole of sum_series series
    '''
    if n == 0:
        return firstEle

    elif n==1 :
        return secondEle
    else :
        return (sum_series(n-1) + sum_series(n-2))


