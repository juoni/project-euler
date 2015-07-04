import math
from timeit import default_timer as timer

def time(callback, arg):
	t = timer()
	result = callback(arg)
	elapsed_time = timer() - t
	print "Call took:", elapsed_time

# naive predicate for palindrome checking
# O(n) time, where n is number of digits in input
def is_palindrome(n):
	lst = []
	while (n > 0):
		i = n % 10
		n /= 10
		lst.append(i)
	i = 0
	j = len(lst) - 1
	while (j > i):
		if (lst[i] != lst[j]):
			return False
		i += 1
		j -=1
	return True

# VERY naive check for largest palindrome of product of 2 DIGITS-digit numbers
# counting down from i and j with a difference of 1 between them will not work
# because does not compute cases where i > j or vice versa... Instead I would
# have to check every i against every j. can find the max by searching for every
# case... Calling with DIGITS+1 is 100 times slower than the last. so growth is
# indeed exponential, and terribly so at O(10^2n), CONFIRMED with tests (n is
# digits). optimizations: do not need to do i=98,j=99 when i=99,j=98 already
# done; optimize by j=i condition - however still exponential
# as shown with summation formula. early stop by checking if m > i*999 since
# everything after we compute is less than that
def largest_palindrome_naive(digits):
	upper_bound = (10 ** digits - 1) # '**' power operation associates right to left
	lower_bound = (10 ** (digits-1) - 1)
	i = j = upper_bound
	a = b = 0
	m = 0
	while (i <= upper_bound and i > lower_bound):
		if (m > i*999):
			break
		while (j >= i):
			x = i*j
			if (is_palindrome(x)):
				if (x>m):
					m = x
					a = i
					b = j
			j-=1
		j = upper_bound
		i -= 1
	print "Largest palindrome of product of two", digits, "digit numbers is", m, "with factors ", a, b

#finding max more efficiently. Can we traverse in such a way so that product is ordered from largest to smallest in worst-case O(n) time, without traversing a smaller one first?
def sorted_product():
	lst = []
	for i in range(1, 10):
		for j in range(1, 10):
			lst.append(i*j)
	lst = sorted(set(lst))
	lst2 = []
	lst3 = []
	for i in lst:
		for j in reversed(range(1, 10)):
			if (i % j == 0):
				s = str(j) + str((i/j))
				lst2.append(s)
				a = 9-j
				b = 9-(i/j)
				break
	print lst, len(lst)
	print lst2, len(lst2)


# another approach: generate all palindromes starting from upper bound, get all factors, and create two factors

assert(is_palindrome(3223) == True)
assert(is_palindrome(9328239) == True)
time(largest_palindrome_naive, 2)
time(largest_palindrome_naive, 3)
time(largest_palindrome_naive, 4)
time(largest_palindrome_naive, 5)
time(largest_palindrome_naive, 6)
time(largest_palindrome_naive, 7)
time(largest_palindrome_naive, 8)

# how many palindromes given n digits?
def num_palindromes(n):
	i = n/2- 1
	if (n%2 ==0):
		return 10**(i) * 9
	else:
		return (10**(i+1)) * 9

assert(num_palindromes(1) == 9)
assert(num_palindromes(2) == 9)
assert(num_palindromes(3) == 90)
assert(num_palindromes(4) == 90)
assert(num_palindromes(5) == 900)
