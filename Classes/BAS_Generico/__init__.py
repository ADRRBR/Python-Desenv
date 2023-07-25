import sys

import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

import pyodbc
import pandas as pd
from enum import Enum

from datetime import datetime as dtm

# Tipos de Retorno para Execução dos Métodos da Classes
class StatusExecucao(Enum):
    SemRequisicao = 0
    Encontrado = 1
    NaoEncontrado = 2
    Sucesso = 3
    Erro = 4
    Confirmado = 5
    Cancelado = 6

class DigitacaoValores(Enum):
    Cancelado = -999999
    Invalido = -444444

def DigMoeda(Mensagem):
    try:
        valor = float(input(Mensagem))
    except (ValueError, TypeError) as erro:
        valor = DigitacaoValores.Invalido
    except KeyboardInterrupt as erro:
        valor = DigitacaoValores.Cancelado

    return valor

def DigNumero(Mensagem):
    try:
        valor = int(input(Mensagem))
    except (ValueError, TypeError) as erro:
        valor = DigitacaoValores.Invalido
    except KeyboardInterrupt as erro:
        valor = DigitacaoValores.Cancelado

    return valor