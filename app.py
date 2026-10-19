from colorama import Fore, Style, just_fix_windows_console

# Ajuda a mostrar as cores corretamente no Windows.
just_fix_windows_console()

niveis_reservatorio = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]


def cor_do_nivel(nivel):
    """Retorna a cor correspondente ao nível informado."""
    cores = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
        4: Fore.CYAN,
        5: Fore.BLUE
    }
    return cores.get(nivel, Fore.WHITE)


def mostrar_situacao(nivel):
    """Exibe a situação do reservatório usando a cor do nível."""
    if nivel < 1 or nivel > len(niveis_reservatorio):
        print(Fore.WHITE + "Nível inválido." + Style.RESET_ALL)
        return

    mensagem = niveis_reservatorio[nivel - 1]
    cor = cor_do_nivel(nivel)
    print(cor + mensagem + Style.RESET_ALL)


print("MONITORAMENTO DO RESERVATÓRIO")
print("=" * 35)

# Simulação dos cinco níveis possíveis.
for nivel_atual in range(1, len(niveis_reservatorio) + 1):
    mostrar_situacao(nivel_atual)
