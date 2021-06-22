import random
import mysql.connector

dbav = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Atv"
)
if dbav.is_connected():
    db_info = dbav.get_server_info()
    print("Connectado.")

class Valores():
    def _init_(self, var, nums):
        self.var = int(var)
        self.nums = dict(nums)

 class dimens():
    def _init_(self, dimen, numse):
        self.dimen = int(dimen)
        self.numse = dict(numse)

def suv(valores, num):
    print(f'numero do Somatório = {peso}')
    global numDb
    numDb = num

    b = 0
    var_adc = 0
    for e in valores:
        var_adc += e['var'] * e['nums'][num]
    return round(var_adc + b, 2)

def sur(valores, num):
    print(f'valor da dimencao = {peso}')
    global numDb
    numDb = num

    c = 0
    dimen_adc = 0
    for e in valores:
        dimen_adc += e['dimen'] * e['numse'][num]
    return round(dimen_adc + c, 1)


def Esp(var_obitido, var_ideal):
    return round(((var_obitido - var_ideal) ** 2), 2)


def criar_nums(qtd_nums):
    nums = {}
    for n_num in range(qtd_nums):
        nums[f'w{n_num}'] = round(random.random(), 2)
    return nums

def criar_numse(qtd_numse):
    numse = {}
    for n_num in range(qtd_numse):
        numse[f'w{n_num}'] = round(random.random(), 1)
    return numse


def cria_lista_valores(qtd_valores, qtd_nums_por_valores,qtd_numse_por_valores):
    valores = []
    for n_valores in range(qtd_valores):
        vars()[f'e{str(n_valores)}'] = {
            "nome": f'Valores {str(n_valores)}',
            "var": round(random.random(), 2),
            "dimen": round(random.random(), 1),
            "nums": criar_nums(qtd_nums_por_valores),
            "numse": criar_numse(qtd_numse_por_valores)
        }valores.append(vars()[f'e{str(n_valores)}'])
    return valores


def pull_num_randomico(valores):
    return f'w{str(random.randint(0, len(valores["nums"]) - 1))}'

def pull_num_randomico(dimen):
    return f'w{str(random.randint(0, len(int(dimen)) - 2))}'

def pull_nums_randomico(var):
    return f'w{str(random.randint(0, int(var) - 1))}'

def pull_numse_randomico(numse):
    return f'w{str(random.randint(0, int(numse) - 2))}'


def print_lista_valores(valores):
    for obj in valores:
        print(f'{obj["nome"]}: var = {obj["var"]}, nums = {obj["nums"]} ')
    print('\n')

    def print_lista_snivel(valores):
    for obj in valores:
        print(f'{obj["nome"]}: dimen = {obj["dimen"]}, nums = {obj["nums"]}, var = {obj["var"]} numse = {obj["numse"]}')
    print('\n')

def print_lista_valores_total(valores):
    for obj in valores:
        print(obj)
    print("\n")


def run():
    qtd_valores = 20
    qtd_nums = 20
    qtd_numse = 20


    print(f'Valores: {qtd_valores}\nNums por valor: {qtd_nums}\n')

    valores = cria_lista_valores(qtd_valores, qtd_nums, qtd_numse)

    print_lista_valores(valores)

    adcs = suv(valores, pull_num_randomico(qtd_nums))
    adcr = sur(valores, pull_num_randomico(qtd_numse))

    print(f'Valores para somar')
    esps = esp(adcr, 2)
    esps = esp(adcs, 1)

    print(f'Espaços entre valores')

    mycursor = dbav.cursor()

    sql = "INSERT INTO valores (nums, VarAtivacao, Varesp, numse) VALUES (%s, %s, %s,%s)"
    val = [(numDb, adcs, esp, adcr)]
    mycursor.executemany(sql, val)
    dbav.commit()
    print("Dados Salvos")
    run()
