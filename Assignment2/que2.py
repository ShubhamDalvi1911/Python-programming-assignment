""" What is the difference between :
    a = 10
    b = 10
    and
    a = [10]
    b = [10]
    Explain using id()."""

# First Case:
a = 10
b = 10
print("id of a :", id(a))
print("id of b :", id(b))
print(id(a) == id(b))
# In this case both a and b points to the same memory loaction beacause immutable objects may share the same memory location if they have the same value.

# Second Case:
a = [10]
b = [10]
print("id of a :", id(a))
print("id of b : ", id(b))
print(id(a) == id(b))
# In this case both a and b points to different memory loaction because list are mutable and mutable objects have different memory locations even if they have the same value.
