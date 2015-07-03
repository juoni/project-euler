# problem 6: find difference between sum of squares of first n ints, and square of sum of first n ints

import math

# sum of numbers from 1 to n is trivially n*(n+1)/2
def natural_sum(n):
	return n*(n+1)/2.0

# misc: let n^2 be the square of a number, and let (n+1)^2 be the square of a number succeeding n. (n+1)^2=n^2+2n+1, meaning that every square of a number is greater than its previous square by an odd number, computed with the number before it.
# sum of squares from 1 to n

# proof that sum of squares = n*(n+1)*(2*n+1)/6.0 is given by the fact that summation(1, n, (i+1)^3-(i^3)) simplifies, with its telescoping sum, to (n+1)^3-1. The original summation also equals summation(1, n, 3i^2 + 3i + 1). Setting that equal to the simplified form, and solving for i^2 yields the equation. Simple algebra.
def sum_of_squares(n):
	return n*(n+1)*(2*n+1)/6.0


print natural_sum(10) ** 2 - sum_of_squares(10)
print natural_sum(100) ** 2 - sum_of_squares(100)
