# Algorithmic Efficiency & Recursion Toolkit (AERT)


# Part A: Stack ADT
class StackADT:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Part B: Factorial
def factorial(n):
    if n < 0:
        return "Error: Input must be non-negative"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Part B: Fibonacci (Naive & Memoized)
naive_calls = 0
memo_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memo(n, memo=None):
    global memo_calls
    memo_calls += 1
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# Part C: Tower of Hanoi 
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)


# Part D: Recursive Binary Search
def binary_search(arr, key, low, high, trace_stack=None):
    if low > high or len(arr) == 0:
        return -1
    
    mid = (low + high) // 2
    
    if trace_stack is not None:
        trace_stack.push(mid)
        
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1, trace_stack)
    else:
        return binary_search(arr, key, mid + 1, high, trace_stack)
    

# Main Execution (Test Cases)
if __name__ == "__main__":
    print("=== AERT TOOLKIT EXECUTION ===\n")

    # Testing Part B: Factorial 
    print("--- Part B: Factorial Tests ---")
    for val in [0, 1, 5, 10]:
        print(f"factorial({val}) = {factorial(val)}")

    #  Testing Part B: Fibonacci
    print("\n--- Part B: Fibonacci Tests ---")
    for val in [5, 10, 20, 30]:
        naive_calls = 0
        memo_calls = 0
        
        ans_naive = fib_naive(val)
        ans_memo = fib_memo(val)
        
        print(f"Fibonacci({val}) = {ans_naive}")
        print(f"  -> Naive calls: {naive_calls}")
        print(f"  -> Memoized calls: {memo_calls}")

    # Testing Part C: Tower of Hanoi
    print("\n--- Part C: Tower of Hanoi (N=3) ---")
    hanoi(3, 'A', 'B', 'C')

    # Testing Part D: Binary Search
    print("\n--- Part D: Binary Search Tests ---")
    search_stack = StackADT() 
    
    # Test 1: Populated Array
    arr = [1, 3, 5, 7, 9, 11, 13]
    keys_to_search = [7, 1, 13, 2]
    print(f"Array: {arr}")
    for key in keys_to_search:
        search_stack.items = [] # Clear stack
        result = binary_search(arr, key, 0, len(arr) - 1, search_stack)
        print(f"Searching for {key}: Index {result} | Visited Mid-Indices (Stack): {search_stack.items}")

    # Test 2: Empty Array
    empty_arr = []
    search_stack.items = [] # Clear stack
    empty_result = binary_search(empty_arr, 5, 0, -1, search_stack)
    print(f"Searching for 5 in empty array []: Index {empty_result}")
    
    print("\n EXECUTION COMPLETE ")