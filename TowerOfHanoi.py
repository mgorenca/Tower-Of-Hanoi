
def move_disks(n, source, destination, temp):
if n == 1:
# Base case: Move a single disk from source to destination
print(f"{source} → {destination}")
else:
# Recursive steps for moving n-1 disks
move_disks(n - 1, source, temp, destination) # Step a
print(f"{source} → {destination}") # Step b
move_disks(n - 1, temp, destination, source) # Step c

def main():
number_of_disks = 3 # Change this value for a different number of disks
move_disks(number_of_disks, 1, 3, 2)

if __name__ == "__main__":
main()