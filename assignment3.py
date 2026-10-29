def replace_value(values, index, new_value):
    values[index] = new_value
    return None
 
 
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1
 
 
def summarize(values):
    return min(values), max(values), sum(values)
 
 
days = int(input("Enter the number of days: "))
 
original = []
for day in range(days):
    minutes = int(input("Enter exercise time in minutes: "))
    original.append(minutes)
 
updated = original[:]
 
index = int(input("Enter the index to correct: "))
new_time = int(input("Enter the new exercise time: "))
replace_value(updated, index, new_time)
 
target = int(input("Enter the exercise time to search for: "))
 
first_index = find_first(updated, target)
count = updated.count(target)
 
minimum, maximum, total = summarize(updated)
 
sorted_list = sorted(updated)
 
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum exercise time: {minimum} minutes")
print(f"Maximum exercise time: {maximum} minutes")
print(f"Total exercise time: {total} minutes")
if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")
print(f"Matching values: {count}")
 
