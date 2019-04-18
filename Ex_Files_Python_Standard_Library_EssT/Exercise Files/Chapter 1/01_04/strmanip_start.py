# Working with string manipulation functions

test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of December"
test2 = ["The", "easter", "egg", "is", "for", "Miranda"]

# TODO: upper and lower convert between cases
print(test_string1.upper())
print(test_string1.lower())

# TODO: Use the split and join functions
print(test_string1.split(" "))
print(" ".join(["The", "easter", "egg", "is", "for", "Miranda"]))
letters = ["a","b","c"]
print(", ".join(letters))
# https://support.klipfolio.com/hc/en-us/.../210940137-Working-with-UTC-date-Format
# Salesforce CreatedDate format:
# UTC format --> "yyyy-MM-dd'T'HH:mm:ss.SSSZ"
print("Norwax, Inc|5826 S. Westgate Rd|Penton|CO|84632".split("|"))
print("|".join(["09817234987234","34.97","2","2019-04-16'T'09:57:01.528Z","1"]))

# TODO: use justification functions to align strings
# ljust, center, rjust
names = ["Amy", "John", "George", "Michael", "Penelope"]
print("\n".join(names))
longestLength = max(len(name) for name in names)
for name in names:
    print(name.ljust(longestLength+2,"-") + ":")
for name in names:
    print(name.center(longestLength+2,"-") + ":")
for name in names:
    print(name.rjust(longestLength+2,"-") + ":")


# TODO: Use a translation table to replace characters
sample_str = "The quick brown fox jumped over the lazy dog"
trans_table = str.maketrans("abegilostz", "4636110572")
print(sample_str)
print(sample_str.translate(trans_table))