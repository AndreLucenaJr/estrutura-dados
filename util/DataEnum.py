from enum import Enum


class Data(Enum):
    MIL = 1000, "mil_desordenado"
    DEZ_MIL = 10_000, "dez_mil_desordenado"
    CEM_MIL = 100_000, "cem_mil_desordenado"
    MILHAO = 1_000_000, "milhao_desordenado"
