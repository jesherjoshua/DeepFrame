from faker import Faker

def checker(lat, lng):
    if lng<-63 and lng>-174.1 and lat<77.5 and lat>18:
        return True
    elif lng<-34 and lng>-81 and lat<11 and lat>-55:
        return True
    else:
        return False
landmasses={
    'north america':[(-112.1,-92.9),(75.48,14.52)]
}
def gen_fake_loc(val=0,mode='intensity'):
    fake=Faker()
    lat,lng=fake.latlng()
    while checker(lat,lng):
        lat,lng=fake.latlng()
    with open(f'./logs/{mode}/logs.txt','a') as fh:
        fh.write(f'{lat},{lng},{val}\n')

