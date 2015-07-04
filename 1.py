import math

# sum of multiples of k below n
def sum_of_multiples_of_k(k, n):
  u = math.ceil(n/(float(k))) - 1
  s = (u*(u+1))/2 * k
  return s

# this problem is trivial with the summation formula (factoring out k from
# multiples of k yields natural numbers in sequence, which leaves summation
# formula to be applied). after summing up the multiples, we must then
# subtract the multiples of 15, as 3 and 5 are factors of 15, so all multiples
# of 15 will be added twice, meaning we must get rid of the duplicate sums.
def sol():
  return sum_of_multiples_of_k(3, 1000) + sum_of_multiples_of_k(5, 1000) - sum_of_multiples_of_k(15, 1000)

print sol()

# proof of summation formula
# let S(n) be sum from k to n. S(n) = k+(k+1)...+n = n+(n-1)...+(n-k)+(n-k-1)
# adding those two forms of S(n), we get 2*S(n) = k
