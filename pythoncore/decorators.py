def decorator(func):

    def wrapper():
        
        print("Transaction Initiated :")
        func()
        print("transaction : proccessed")
        return wrapper

@decorator
def transac():
    print("Executing proccesses for transaction ")

# 1. Define the decorator
def announce(func):
    
    # 2. Define the "wrapper" (the bread of the sandwich)
    def wrapper():
        print("🍞 --- Starting the function ---")
        
        func()  # (The meat of the sandwich) This is where the original function runs!
        
        print("🍞 --- Finished the function ---")
        
    # 3. Return the wrapper
    return wrapper

# --- How to use it ---

@announce
def say_hello():
    print("🥩 Hello! I am running right now.")

# Run the function
say_hello()