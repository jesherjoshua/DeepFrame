from faker import Faker



def gen_fake_loc(intensity=0):
    fake=Faker()
    lat,lng=fake.latlng()
    with open('./logs/intensity/logs.txt','a') as fh:
        fh.write(f'{lat},{lng},{intensity}\n')

