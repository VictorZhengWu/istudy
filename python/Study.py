################################################################
## 模板
name = input('Please input your name: ')
age = input('Please input your age: ')
job = input('Please input your job: ')

template = '''Hello, my name is %s, 
i am %s this year, 
my job is %s''' %(name, age, job)

print(template)


################################################################
## bit_length
num = 10
print(num.bit_length())