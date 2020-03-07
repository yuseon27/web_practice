from faker import Faker
# To Create Massive Fake Data randomly

ko_fake = Faker('ko_KR')
my_fake = Faker()

# Using Faker's method, decide which fake data to fetch
Faker.seed(1) # seed number is data's number

print(my_fake.name())
print(my_fake.address())
print(my_fake.text())
print(my_fake.state())
print(my_fake.sentence())
print(my_fake.random_number())

'''
views.py DB - for loop
blog = Blog()
blog.title = ''
blog.body = ''

blog.save()
blog.delete()
'''
