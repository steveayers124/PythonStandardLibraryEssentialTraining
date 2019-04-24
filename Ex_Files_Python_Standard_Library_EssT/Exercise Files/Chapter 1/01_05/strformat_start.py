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
# the format string is very powerful. This tutorial doesn't dive
#  deeply into usage of the format string. But do so on your own
foo = "foo"
bar = 123
print("Output: {}, {}".format(foo, bar))
print("Output: {1}, {0}".format(foo, bar))
date = "2019-04-23"
meal = "lunch"
print("Today's date is {0}. On {0}, you should go to {1}.\nYou should go to {1} on {0}.".format(date, meal))
print("Output: {var1}, {var2}".format(var1=foo,var2=bar))




# TODO: Using interpolation with f-strings in Python 3.6
product = "Widget"
price = 19.99
tax = 0.07
