
print('Price of product')
product = {'pencil' : {'price':50 ,'color':'red'},
           'Erasor':{'price':3,'color':'green'},
           'ruler':{'price':100,'color':'orange'},           
           'paper':{'price':99,'color':'black'}           
           }

print('welcome our program')
for t,p in product.items():
    print('product {} price: {} Bath'.format(t,p['price']) )

while True:
   
    print('---input data product---')
    p = input('name product: ')
    q = int(input('quility: '))
    print('--------')
    print(f'product:')
    if p in product:
        print(f'product: {p} price:{product[p]['price']} color:{product[p]['color']}')
        print(f'amout: {q} piece total {product[p]['price'] * q} Bath')
    else:
        print('No product in system4')


