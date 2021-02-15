from funcao import funcao_para_testar, funcao_nova


def teste_basico():
    assert funcao_para_testar(3, 5) == 15


def teste_numeros_negativos():
    assert funcao_para_testar(-3, 9) == -27

def teste_funcao_nova_media():
    assert funcao_nova(1, 2, 3) == 2

