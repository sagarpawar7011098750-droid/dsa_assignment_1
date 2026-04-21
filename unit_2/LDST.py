class DynamicArray:
    def __init__(self, initial_capacity=2):
        # Initialize internal capacity and size
        self.capacity = initial_capacity
        self.size = 0
        # Simulating a raw array using a fixed-size Python list
        self.array = self._create_array(self.capacity)

    def _create_array(self, capacity):
        """Creates a fixed-size array with None values."""
        return [None] * capacity

    def append(self, x):
        """Appends an element, doubling capacity if full."""
        if self.size == self.capacity:
            self._resize()
        
        # Insert the new element
        self.array[self.size] = x
        self.size += 1

    def _resize(self):
        """Creates a new array with double capacity and copies elements over."""
        old_capacity = self.capacity
        self.capacity *= 2
        print(f"[*] Array Full! Resizing capacity from {old_capacity} to {self.capacity}...")
        
        new_array = self._create_array(self.capacity)
        # Copy elements to the new array
        for i in range(self.size):
            new_array[i] = self.array[i]
            
        self.array = new_array

    def pop(self):
        """Removes and returns the last element."""
        if self.size == 0:
            print("Error: Array underflow (cannot pop from empty array)")
            return None
        
        # Get the last element
        val = self.array[self.size - 1]
        # Remove it logically by decreasing size and clearing the slot
        self.array[self.size - 1] = None 
        self.size -= 1
        return val

    def print_array(self):
        """Displays the current active elements, size, and capacity."""
        # Only show up to self.size to hide the empty allocated slots
        active_elements = [str(self.array[i]) for i in range(self.size)]
        print(f"Array: [{', '.join(active_elements)}] | Size: {self.size} | Capacity: {self.capacity}")



# TEST CASES
if __name__ == "__main__":
    print("--- Testing Dynamic Array ---")
    da = DynamicArray(initial_capacity=2)
    
    print("1. Appending 12 items to trigger resizing:")
    for i in range(1, 13):
        da.append(i * 10)
        da.print_array()
        
    print("\n2. Popping 3 items:")
    for _ in range(3):
        popped_val = da.pop()
        print(f"Popped: {popped_val}")
    da.print_array()
    print("-" * 30 + "\n")