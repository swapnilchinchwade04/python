import sys

# Print all arguments
print("Arguments list:", sys.argv)

# Access specific arguments
if len(sys.argv) > 1:
    print("First user argument:", sys.argv[1])