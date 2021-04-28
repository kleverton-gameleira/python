print('*'*20)
print('*'*20,'verificando a categoria','*'*20)

data_nasc = int(input('informe a data de nascimento do atleta: '))
idade = 2021 - data_nasc

if idade < 18:
    if idade <= 10:
        print('Este atleta pertece a categoria infantil')
    elif idade <= 15:
        print('Este atleta pertece a categoria sub-15')
    elif idade <= 17:
        print('Este atleta pertence a categoria juvenil')
elif idade <= 20:
    print('Este atleta pertence a categoria sub-20')
else:
    print('Este atleta pertence a categoria profissional')