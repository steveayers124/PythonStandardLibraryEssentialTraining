from string import Template
the_template = Template("The quick brown $animal $action over the lazy dog")
print(the_template.substitute(animal="fox", action="jumped"))
