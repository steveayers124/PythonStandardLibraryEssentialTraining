# String formatting methods and best practices
from string import Template

# TODO: Using Template strings
the_str = "The quick brown $animal $action over the lazy dog"
the_template = Template(the_str)
output_str = the_template.substitute(animal="fox", action="jumped")
print(output_str)
# Now use a ditionary object
args = {
    "animal":"cow",
    "action":"walked"
}
print(the_template.substitute(args))



# TODO: Using str.format()
foo = "foo"
bar = 123


# TODO: Using interpolation with f-strings in Python 3.6
product = "Widget"
price = 19.99
tax = 0.07
