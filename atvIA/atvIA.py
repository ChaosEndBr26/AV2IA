#Feito por :
#BRENO PIMENTEL DE OLIVEIRA - 201751190481
#MATHEUS SÁ BARRETO MACIEL - 201951196988

import random
import mysql.connector

numDb = ""

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Atv"
)
if mydb.is_connected():
    db_info = mydb.get_server_info()
    print("Connected.")

class Valores():
    def _init_(self, var, nums):
        self.var = int(var)
        self.nums = dict(nums)


def suv(valores, num):
    print(f'numero do Somatório = {peso}')
    global numDb
    numDb = num

    b = 0
    var_adc = 0
    for e in valores:
        var_adc += e['var'] * e['nums'][num]
    return round(var_adc + b, 2)


def Esp(var_obitido, var_ideal):
    return round(((var_obitido - var_ideal) ** 2), 2)


def criar_nums(qtd_nums):
    nums = {}
    for n_num in range(qtd_nums):
        nums[f'w{n_num}'] = round(random.random(), 2)
    return nums


def cria_lista_valores(qtd_valores, qtd_nums_por_valores):
    valores = []
    for n_valores in range(qtd_valores):
        vars()[f'e{str(n_valores)}'] = {
            "nome": f'Valores {str(n_valores)}',
            "var": round(random.random(), 2),
            "nums": criar_nums(qtd_nums_por_valores)
        }
        valores.append(vars()[f'e{str(n_valores)}'])
    return valores


def pull_num_randomico(valores):
    return f'w{str(random.randint(0, len(valores["nums"]) - 1))}'


def pull_nums_randomico(var):
    return f'w{str(random.randint(0, int(var) - 1))}'


def print_lista_valores(valores):
    for obj in valores:
        print(f'{obj["nome"]}: var = {obj["var"]}, nums = {obj["nums"]} ')
    print('\n')


def print_lista_valores_total(valores):
    for obj in valores:
        print(obj)
    print("\n")


def run():
    qtd_valores = 20
    qtd_nums = 20

    print(f'Valores: {qtd_valores}\nNums por valor: {qtd_nums}\n')

    valores = cria_lista_valores(qtd_valores, qtd_nums)

    print_lista_valores(valores)

    adcs = suv(valores, pull_num_randomico(qtd_nums))

    print(f'Valores para somar')

    esps = esp(adcs, 1)

    print(f'Espaços entre valores')

    mycursor = mydb.cursor()

    sql = "INSERT INTO valores (nums, VarAtivacao, Varesp) VALUES (%s, %s, %s)"
    val = [(numDb, adcs, esp)]
    mycursor.executemany(sql, val)
    mydb.commit()
    print("Dados Salvos")

if __name__ == 'ATV IA':
    run()

