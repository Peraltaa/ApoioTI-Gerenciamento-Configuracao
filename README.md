# ApoioTI - Controle de Chamados de Informática

Projeto original da aula prática de Gerenciamento de Configuração de Software (U4 A1). Aplicação Python de linha de comando para cadastrar e consultar chamados de suporte técnico, classificar prioridades e produzir relatórios.

## Como executar
Requer Python 3.10+ e não depende de bibliotecas externas.

```bash
python chamados.py abrir "Biblioteca" "Impressora sem conexão" --prioridade alta
python chamados.py abrir "Sala de aula 2" "Mouse com defeito" --prioridade baixa
python chamados.py listar
python relatorio.py
python -m unittest discover -s tests -v
```

## Artefatos controlados
- `chamados.py`: cadastro, listagem e persistência de chamados.
- `relatorio.py`: resumo das quantidades por prioridade.
- `tests/test_chamados.py`: cinco testes automatizados.
- `README.md`: instruções, objetivos e histórico funcional.
- `.gitignore`: impede versionamento de dados operacionais e cache.

## Solicitação de mudança simulada
A versão inicial permitia cadastrar e listar chamados. A área de operações pediu inclusão de prioridade alta, média ou baixa e de relatórios; também precisava manter compatibilidade com registros anteriores, sem campo de prioridade. Estes recursos estão no código publicado.

## Gestão de configuração
O histórico deste repositório GitHub registra os commits de publicação dos artefatos e sua rastreabilidade. O estudo original também documentou, em laboratório local, duas versões evolutivas, clonagem, alterações, commit, push e auditoria independente. As duas histórias são distintas: histórico local de desenvolvimento e histórico da publicação GitHub.

## Privacidade
Projeto didático: dados fictícios. Arquivo `dados/chamados.json` não deve ser enviado ao GitHub.
