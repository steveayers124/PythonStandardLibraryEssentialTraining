# use predefined string constants
import string


# TODO: predefined string constants can be used in common scenarios
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)

print(string.printable)
print(string.whitespace)
print("Okay, that was whitespace. Next, __all__")
print(string.__all__)
print("Okay, that was __all__. Next, __file__")
print(string.__file__)
print("Okay, that was __file__. Next, ascii_lowercase")
print(string.ascii_lowercase)
print(string.octdigits)

print("\n\n\n")


# # TODO: Use the constants to filter information out
# test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of December"
# test_string2 = "Supercalifragilistic"
# test_string3 = "90210"

# # A list comprehension consists of brackets containing an expression 
# # followed by a for clause, then zero or more for or if clauses. 
# # The result will be a new list resulting from evaluating the 
# # expression in the context of the for and if clauses which follow it.
# #  https://docs.python.org/3/tutorial/datastructures.html
# result = "".join([c for c in test_string1 if c in string.ascii_letters])
# print(result)
# result = test_string3.join([c for c in test_string1 if c in string.ascii_letters])
# print(result)
# result = "Z".join([c for c in test_string1 if c in string.ascii_letters])
# print(result)
# result = "".join(["a" for a in test_string1 if a in string.ascii_letters])
# print(result)
# result = "".join(["`" for a in test_string1 if a in string.ascii_letters])
# print(result)
# result = "".join(["`" for a in test_string1 if a in "abc"])
# print(result)
# result = "".join([c for c in test_string1 if c in string.ascii_letters])
# print(result)

# print("\n\n\n")


# # TODO: String testing methods

# print(test_string1.isalnum())
# print(test_string2.isalpha())

# print(all([c.isalpha() for c in test_string1]))
# print(all([c.isalpha() for c in test_string2]))
# print(all([c.isalpha() for c in test_string3]))

# print(all([c.isalnum() for c in test_string1]))
# print(all([c.isalnum() for c in test_string2]))
# print(all([c.isalnum() for c in test_string3]))

# print(all([c.isnumeric() for c in test_string1]))
# print(all([c.isnumeric() for c in test_string2]))
# print(all([c.isnumeric() for c in test_string3]))

# print("\n\n\n")


# # TODO: more playing around
# print("".join([c for c in test_string1 if c in string.ascii_letters]))
# print("".join([c for c in test_string2 if c in string.ascii_letters]))
# print("".join([c for c in test_string3 if c in string.ascii_letters]))

# print("".join([c for c in test_string1 if c in string.digits]))
# print("".join([c for c in test_string2 if c in string.digits]))
# print("".join([c for c in test_string3 if c in string.digits]))

# print("".join([c for c in test_string1 if c in string.hexdigits]))
# print("".join([c for c in test_string2 if c in string.hexdigits]))
# print("".join([c for c in test_string3 if c in string.hexdigits]))

# print("\n\n\n")

# print(any([c.isalpha() for c in test_string1]))
# print(any([c.isalpha() for c in test_string2]))
# print(any([c.isalpha() for c in test_string3]))

# print(any([c.isalnum() for c in test_string1]))
# print(any([c.isalnum() for c in test_string2]))
# print(any([c.isalnum() for c in test_string3]))

# print(any([c.isnumeric() for c in test_string1]))
# print(any([c.isnumeric() for c in test_string2]))
# print(any([c.isnumeric() for c in test_string3]))
