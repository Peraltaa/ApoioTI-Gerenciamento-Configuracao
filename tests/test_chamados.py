"""Testes automatizados das funcionalidades originais e da evolução solicitada."""
import tempfile
import unittest
from pathlib import Path

from chamados import abrir_chamado, carregar
from relatorio import resumo_por_prioridade

class TestChamados(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.caminho = Path(self.tmp.name) / 'chamados.json'

    def tearDown(self):
        self.tmp.cleanup()

    def test_registra_e_recupera_chamado(self):
        registro = abrir_chamado('Laboratório 3', 'Sem rede', self.caminho, 'alta')
        self.assertEqual(registro['id'], 1)
        self.assertEqual(carregar(self.caminho)[0]['prioridade'], 'alta')

    def test_prioridade_invalida_rejeitada(self):
        with self.assertRaises(ValueError):
            abrir_chamado('Secretaria', 'Impressora', self.caminho, 'urgente')

    def test_identificadores_sequenciais(self):
        abrir_chamado('Sala 1', 'Mouse', self.caminho)
        segundo = abrir_chamado('Sala 2', 'Teclado', self.caminho)
        self.assertEqual(segundo['id'], 2)

    def test_relatorio_contabiliza_prioridades(self):
        dados = [{'prioridade': 'alta'}, {'prioridade': 'baixa'}, {'prioridade': 'alta'}]
        self.assertEqual(resumo_por_prioridade(dados), {'alta': 2, 'media': 0, 'baixa': 1})

    def test_registro_antigo_tem_prioridade_padrao_no_relatorio(self):
        self.assertEqual(resumo_por_prioridade([{'id': 1}])['media'], 1)

if __name__ == '__main__':
    unittest.main()
