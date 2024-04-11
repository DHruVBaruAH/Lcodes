
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def print_menu():
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Exit")

def main():
    while True:
        print("\nWelcome to Sorting Program")
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            arr = input("Enter the array to be sorted (space-separated numbers): ").split()
            arr = [int(x) for x in arr]
            bubble_sort(arr)
            print("Sorted array using Bubble Sort:", arr)

        elif choice == '2':
            arr = input("Enter the array to be sorted (space-separated numbers): ").split()
            arr = [int(x) for x in arr]
            selection_sort(arr)
            print("Sorted array using Selection Sort:", arr)

        elif choice == '3':
            arr = input("Enter the array to be sorted (space-separated numbers): ").split()
            arr = [int(x) for x in arr]
            insertion_sort(arr)
            print("Sorted array using Insertion Sort:", arr)

        elif choice == '4':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    main()
