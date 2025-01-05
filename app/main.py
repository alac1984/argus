"""

    DOC: main.py

    Esse script possui a lógica de execução do sistema.

"""


def main() -> None:
    """

        DOC: main.main()

        Ao executar a função main(), o sistema deve:

        ---- Na fase de Extração de Dados:

        1) Checar a existência de novos Arquivos;

        2) Caso identifique esses arquivos, persistir suas informações;

        3) Interpretar (pelo nome do arquivo) o Concurso e a Publicação a qual
        o arquivo representa;

        4) Usar o Extrator para extrair os Documentos presentes na Publicação e
        persisti-los nos lugares corretos;

        ---- Na fase de triagem dos dados

        5) Loopar pelas listas de cada Documento em busca de novas Entradas;

        6) Caso hajam novas Entradas do tipo Inscrição, persisti-las;

        7) Caso hajam novas Entradas do tipo Aprovação, persisti-las e persistir
        tambem a Ordem de Aprovação;

        8) Caso hajam novas Entradas do tipo Convocação loopar por elas e:
            8.1. Checar se as Pessoas presentes na Convocação são Candidatos
            com Inscrição;
                8.1.1. Se não forem, gravar como Erro de Inscrição;
            8.2. Checar se os Candidatos presentes na Convocação e Inscrição são
            Candidatos com Aprovação;
                8.2.1. Se não forem, gravar como Erro de Aprovação;
            8.3. Checar se os Candidatos presentes na Convocação, com Inscrição e
            Aprovação estão sendo convocados na Ordem esperada;
                8.3.1. Se não forem, gravar como Erro de Convocação;

        9) Caso não hajam Exceções que impeçam a Execução do programa, gravar
        os logs de execução e persistir os dados da Execução.

    """
