"""Registro simples de chamados de suporte de informática, sem dependências externas."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ARQUIVO = Path(__file__).parent / 'dados' / 'chamados.json'
PRIORIDADES = ('baixa', 'media', 'alta')

def carregar(caminho=ARQUIVO):
    caminho = Path(caminho)
    if not caminho.exists():
        return []
    with caminho.open(encoding='utf-8') as arquivo:
        return json.load(arquivo)

def salvar(chamados, caminho=ARQUIVO):
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open('w', encoding='utf-8') as arquivo:
        json.dump(chamados, arquivo, ensure_ascii=False, indent=2)

def abrir_chamado(solicitante, descricao, caminho=ARQUIVO, prioridade='media'):
    if not solicitante.strip() or not descricao.strip():
        raise ValueError('Solicitante e descrição não podem estar vazios.')
    if prioridade not in PRIORIDADES:
        raise ValueError('Prioridade inválida: use baixa, media ou alta.')
    chamados = carregar(caminho)
    novo = {
        'id': max((c['id'] for c in chamados), default=0) + 1,
        'solicitante': solicitante.strip(),
        'descricao': descricao.strip(),
        'status': 'aberto',
        'prioridade': prioridade,
        'criado_em': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    }
    chamados.append(novo)
    salvar(chamados, caminho)
    return novo

def main():
    parser = argparse.ArgumentParser(description='ApoioTI - gestão simples de chamados')
    sub = parser.add_subparsers(dest='comando', required=True)
    novo = sub.add_parser('abrir', help='Cadastrar novo chamado')
    novo.add_argument('solicitante')
    novo.add_argument('descricao')
    novo.add_argument('--prioridade', choices=PRIORIDADES, default='media')
    sub.add_parser('listar', help='Listar todos os chamados')
    args = parser.parse_args()
    if args.comando == 'abrir':
        chamado = abrir_chamado(args.solicitante, args.descricao, prioridade=args.prioridade)
        print(f"Chamado #{chamado['id']} cadastrado com sucesso.")
    elif args.comando == 'listar':
        for c in carregar():
            print(f"#{c['id']} | {c.get('prioridade', 'media')} | {c['status']} | {c['solicitante']} | {c['descricao']}")

if __name__ == '__main__':
    main()
