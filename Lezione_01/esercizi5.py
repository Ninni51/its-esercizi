import time
'''
def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    z = []
    if len(x) == len(y):
        for i in range(len(x)):
            z.append(x[i]+y[i])
        print(z)
    else:
        print("Errore: numero di elementi diverso nelle liste.")

somma_elementi([2,2,2], [1,1,1])
somma_elementi([2,6,8], [10,23,11])
somma_elementi([2,2,2, 2], [1,1,1])

def even_odd_pattern(numbers:list[int]) -> list[int]:
    even = []
    odd = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even.append(numbers[i])
        else:
            odd.append(numbers[i])
    numbers = []
    numbers.extend(even)
    numbers.extend(odd)

def prime_factors(n: int) -> list[int]:
    den = 2
    prime = []
    while n != 0 and n != 1:
        if n%den == 0:
            prime.append(den)
            n = n//den
            den = 2
        else:
            den+=1
    return prime
            
print(prime_factors(99999999999999999999))
'''
def find_disappeared_numbers(nums: list[int]) -> list[int]:
    missing = []
    n = len(nums)
    nums.sort()
    j = 0
    for i in range(1, n+1):
        while j < n and nums[j] < i:
            j += 1  
        if j >= n or nums[j] > i:
            missing.append(i)  
    return missing
            
print(find_disappeared_numbers([1, 8, 9, 150]))