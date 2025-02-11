fish = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john "
"dory", "red cod"]

# Task A
for name in fish:
    print(name[0])

# Task B
print("\n")
for name in fish:
    print(name[:3])

# Task C
print("\n")
longest_name = ""
for name in fish:
    if len(name) > len(longest_name):
        longest_name = name
print(longest_name)

# Task D
print("\n")
for name in fish:
    if " " in name:
        print(name)

# Task E
print("\n")
for name in fish:
    if "cod" in name:
        print(name)
