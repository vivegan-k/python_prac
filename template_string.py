from string import Template

temp = Template('Hi I am ${name} working at ${company}')

out = temp.substitute(name='vivek', company='Nutanix')

data = {'name': 'vivek', 'company':'Nutanix'}

out1 = temp.substitute(data)

print out
print out1