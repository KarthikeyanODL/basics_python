# 1. CREATE (Assigning a value to a variable)
item_name = "Laptop"
print(f"Created: {item_name}")

# 2. READ (Accessing/Displaying the variable)
print(f"Reading: The current item is {item_name}")

# 3. UPDATE (Reassigning a new value to the same variable)
item_name = "Gaming Laptop"
print(f"Updated: The item is now {item_name}")

# 4. DELETE (Removing the variable from memory)
# In Python, we use the 'del' keyword to delete a variable reference
del item_name

# If you try to print it now, it will throw a NameError because it no longer exists
print(item_name)
