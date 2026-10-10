"""Gera resumo de chamados por prioridade, respeitando registros antigos sem o campo."""
from collections import Counter
from chamados import carregar

def resumo_por_prioridade(chamados):
    contagem = Counter(c.get('prioridade', 'media') for c in chamados)
    return {p: contagem.get(p, 0) for p in ('alta', 'media', 'baixa')}

def main():
    chamados = carregar()
    totais = resumo_por_prioridade(chamados)
    print(f'Total de chamados: {len(chamados)}')
    for prioridade, quantidade in totais.items():
        print(f'{prioridade.capitalize():6}: {quantidade}')

if __name__ == '__main__':
    main()
