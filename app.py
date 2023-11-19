from faker import Faker

fake = Faker('pt_BR')
for _ in range(10):
    print(40*'-')
    print(f'Nome: {fake.name()}')
    print(f'Data Nascimento: {fake.date()}')
    print(f'Endereço: {fake.address()}')
    print(f'CPF: {fake.cpf()}')
    print(f'RG: {fake.rg()}')