"""s = "hello"
rev = ''
for ch in s:
    rev = ch + rev
print(rev)

for number in range(1, 6):
  print(number)
# "olleh"

numbers = [1, 5, 9 , 3,]
total = 0
for num in numbers:
    total += num
print(total)

value = input("Enter a number or letter:")

while not (value.isdigit() or value.isalpha()):
    value = input("Invalid input. Please enter a number or letter:")
print("Thank you! You entered:", value)

shopping_list = ["apples", "bananas", "carrots", "dates"]
item_found = False
while not item_found:
    item = input("Enter an item to search for in the shopping list or enter 'q' to quit: ").strip()
    if item.lower() == 'q':
        print("Exiting the search.")
        break
    if item in shopping_list:
        print(f"{item} is in the shopping list.")
        item_found = True
    else:
        print(f"{item} is not in the shopping list. Try again.")


outer_count = 5

while outer_count > 0:
  # Outer loop controls the number of times the inner loop runs
  inner_count = 1
  while inner_count <= outer_count:
    # Inner loop repeats for each outer loop iteration
    print(inner_count, end=" ")
    inner_count += 1
  print()  # Move to a new line after each outer loop iteration
  outer_count -= 1"""

for i in range(1, 11):
  # Outer loop iterates through rows (multiplication factors)
  for j in range(1, 11):
    # Inner loop iterates through columns (other factors)
    product = i * j
    print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
  print()  # Move to a new line after each row