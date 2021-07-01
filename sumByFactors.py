'''
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

It can happen that a sum is 0 if some numbers are negative!
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
'''
def primesUpTo(limit):
    limit = abs(max(limit, key=abs))
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def sum_for_list(lst):
    print(lst)
    primeDict = {}
    primeNums = primesUpTo(lst)
    for n in lst:
        for p in primeNums:
            if n % p == 0: # if p is a factor of n.
                if p in primeDict.keys():
                    primeDict[p] += n
                else:
                    primeDict[p] = n
    
    return sorted([[k, v] for k, v in primeDict.items()])
    
print(
    sum_for_list([12, 15]) == [[2, 12], [3, 27], [5, 15]],
    sum_for_list([15, 21, 24, 30, -45]) == [[2, 54], [3, 45], [5, 0], [7, 21]],
    sum_for_list([107, 158, 204, 100, 118, 123, 126, 110, 116, 100]),
    sum_for_list([362048, -971016, -643895, -769176, -238682, 411533, -734897, -437951, -686038, -60942, 969764, -792004, -279366]) == [[2, -2465412], [3, -2080500], [5, -643895], [7, -704837], [101, -279366], [107, -437951], [131, -238682], [197, 411533], [389, -792004], [461, -279366], [509, -792004], [911, -238682], [1187, -769176], [1451, -60942], [2089, 411533], [4093, -437951], [5657, 362048], [18397, -643895], [40459, -971016], [242441, 969764], [343019, -686038], [734897, -734897]]
)