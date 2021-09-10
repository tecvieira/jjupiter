import pandas


tabela = pandas.read_excel('vendas2021.xlsx')
print(tabela)
faturamentoTotal = tabela['VENDAS'].sum()
print(f'O faturamento total é R$ {faturamentoTotal:.2f}')

faturamentoLoja = tabela[['LOJAS', 'VENDAS']].groupby('LOJAS').sum()
print(faturamentoLoja)

faturProduto = tabela[['LOJAS','PRODUTO','VENDAS']].groupby(['LOJAS', 'PRODUTO']).sum()
print(faturProduto)