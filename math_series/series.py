
# def febonacci(n):
#     '''
#     this function take n from user and it will return the febonacci series
#     '''
def fiboseries(n):
    # series = [0]* (n-1)
    if n == 0:
            # series.append(n)
        return 0

    elif n==1 :
            # series.append(n)
        return 1
    else :
            # series.append((febonacci(n-1) + febonacci(n-2)))
        return (fiboseries(n-1) + fiboseries(n-2))
    # nthvalue = fiboseries(n)
    # print(f'nthvalue = {nthvalue}')
    # for i in range(n):
    #     # series.append(febonacci(i))

    #     print(f'fibonacci({i}) == {fiboseries(i)}')

# x= input('insert number :   ')
# print(febonacci(int(x)))


# def lucas(n):
    '''
    you insert the n value and the function return the nth value and whole series of lucas series
    '''
def lucasSeries(n):
    if n == 0:
        return 2

    elif n==1 :
        return 1
    else :
        return lucasSeries(n-1) + lucasSeries(n-2)
#     nthvalue = lucasSeries(n)
#     print(f'nthvalue = {nthvalue}')
#     for i in range(n):
#         print(f'lucas({i}) == {lucasSeries(i)}')
# # y= input('insert number :   ')
# # print(lucas(int(y)))

# def sum_series(n,firstEle=2,secondEle=3):
    '''
    you insert the nth value and the firstEle and secondEle is optional and it should return the nth value and whole of sum series
    '''
def sum(n,firstEle=2,secondEle=3):
    if n == 0:
        return firstEle

    elif n==1 :
        return secondEle
    else :
        return (sum(n-1) + sum(n-2))
    
    # nthvalue = sum(n)
    # print(f'nthvalue = {nthvalue}')
    # for i in range(n):
    #     print(f'sum series ({i}) == {sum(i)}')
# y= input('insert number :   ')
# print(sum_series(int(y)))

