# Array with 10 elements
arr = [45, 12, 67, 23, 89, 34, 10, 56, 78, 21]

print("Original Array:", arr)

print("\n1. Ascending Order")
print("2. Descending Order")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    sorted_arr = sorted(arr)
    print("Array in Ascending Order:")
    print(sorted_arr)

elif choice == 2:
    sorted_arr = sorted(arr, reverse=True)
    print("Array in Descending Order:")
    print(sorted_arr)

else:
    print("Invalid choice!")