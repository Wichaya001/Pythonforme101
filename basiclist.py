product = {'pencil' : {'price':50 ,'color':'red'},
           'Erasor':{'price':3,'color':'green'},
           'ruler':{'price':100,'color':'orange'}           
           }


while True:
    print('-------fill data product--------')
    p = input('name product')
    q = int(input('quility: '))
    print('--------')
    print(f'product:')
    if p in product:
        print(f'product: {p} price:{product[p]['price']} color:{product[p]['color']}')
        print(f'amout: {q} piece total {product[p]['price'] * q} Bath')
    else:
        print('No product in system454545')
