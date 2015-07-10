from timeit import default_timer as timer

def time(callback, arg):
  t = timer()
  result = callback(arg)
  elapsed_time = timer() - t
  print "Call took:", elapsed_time

# computes number of possible paths in an nxn grid from upperleft corner
# to lowerright corner. observe that nodes are in row major order.
# naive solution: grows exponentially; this solution doesn't even finish in time
def naive_sol(n):
  MAX_NODE = (n+1)**2 - 1 # lowerright corner node of grid
  RIGHT = 1
  DOWN = 2
  def can_move_right(node):
    return ((node+1) % (n+1) != 0) # == means at right side of grid
  def can_move_down(node):
    return ((node < (MAX_NODE-n)));
  def move_down(cur_node):
    return cur_node + (n+1)
  def move_right(cur_node):
    return cur_node + 1
  # we don't need to track direction because we only have 2 directions. by
  # virtue of testing whether we can move right or down alone we can determine
  # if we are building a new path or continuing the same one
  def count_paths(cur_node):
    def count_paths_inner(cur_node):
      num_paths = 0
      if (cur_node == MAX_NODE):
        return 0
    #  if they only have one direction to go then number of path remains same
    #  (because we continue building on the same path)
      if (can_move_right(cur_node) and can_move_down(cur_node)):
        num_paths += 1
      if (can_move_right(cur_node)):
        num_paths += count_paths_inner(move_right(cur_node))
      if (can_move_down(cur_node)):
        num_paths += count_paths_inner(move_down(cur_node))
      return num_paths
    return 1 + count_paths_inner(cur_node) # add 1 for single node grid

  cur_node = 0
  print "Number of paths for", n, "x", n, "grid:", count_paths(cur_node)

# Observe that each path has the same number of steps: 2n. This is because we
# are only allowed to go right and down, and never back. In other words, we are
# only allowed to increment the initial coordinates (i=0, j=0), until we reach
# the max node (n, n). As a result we have an equal number of right and down
# steps in each path. Hence the number of different paths is the number of ways
# we can distribute N right steps into 2N total steps, which makes out to be
# combination(2N, N).
def better_sol(n):
  return combination(2*n, n)

# naive combination
def combination(n, k):
  return permutation(n, k) / factorial(k)
# naive permutation
def permutation(n, k):
  return factorial(n) / factorial(n-k)
# naive factorial
def factorial(x):
  if (x == 0 or x == 1):
    return 1
  return x * (factorial(x-1))

print better_sol(20)



