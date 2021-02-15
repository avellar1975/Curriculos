from funcao import funcao_para_testar


def teste_basico():
    assert funcao_para_testar(3, 5) == 15


def teste_numeros_negativos():
    assert funcao_para_testar(-3, 9) == -27
