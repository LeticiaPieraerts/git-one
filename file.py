from pathlib import Path

# Notebook
this_dir = Path(".")
print(this_dir)

this_dir = this_dir.resolve()
print(this_dir)

root = this_dir.parent
print(root)

# Py file
this_file = Path(__file__)
print(this_file)

root = this_file.parent.parent
print(root)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
