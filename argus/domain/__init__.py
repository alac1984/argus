"""

    DOC: domain/__init__.py

    Os seguintes elementos fazem parte do domínio:

    - ARQUIVO: é um Arquivo no sistema operacional, salvo em uma determinada
    pasta do sistema, e que pode ser um Publicação que contém Documentos;
    - CARGO: é a ocupação para a qual um Candidato fez sua Inscrição em um Concurso;
    - CONCURSO: é um processo seletivo, cujos Arquivos podem ser Publicações e estas
    podem conter Documentos, que podem possuir Entradas;
    - DOCUMENTO: é uma entrada relevante encontrada em um Publicação:
        - LISTA DE INSCRIÇÃO: uma lista de Candidatos com Inscrição num Concurso;
        - LISTA DE APROVAÇÃO: uma lista de Candidatos com Aprovação num Concurso;
        - LISTA DE CONVOCAÇÃO: uma lista de Candidatos com Convocação num Concurso;
    - ESCOLA: é a unidade de ensino para a qual o Candidato recebeu sua Convocação;
    - ERRO: é um tipo de erro encontrado no Concurso.
        - ERRO DE CONVOCAÇÃO: ocorre quando a Ordem de Convocação de um Candidato é
        diferente da Ordem de Aprovação do mesmo em um determinado Concurso;
        - ERRO DE INSCRIÇÃO: ocorre quando um Candidato com Convocação não possui
        Inscrição para aquele Concurso;
        - ERRO DE APROVAÇÃO: ocorre quando um Candidato com Convocação não possui
        Aprovação para aquele Concurso;
    - EXECUÇÃO: é uma Execução do programa, que grava os Erros e os logs de execução;
    - EXTRATOR: é uma estrutura que possui todas os regex necessários para extrair
    informações de um Documento relativo a um Concurso e gerar Entradas para o mesmo;
    - ENTRADA: é uma inserção de dados de um Candidato em um Concurso.
        - INSCRIÇÃO: é a Inscrição de um Candidato em um Concurso;
        - APROVAÇÃO: é a Aprovação de um Candidato em um Concurso;
        - CONVOCAÇÃO: é a Convocação de um Candidato em um Concurso;
    - ORDENAMENTO: é a representação da ordem do Candidato numa Fase:
        - ORDEM DE APROVAÇÃO: a posição de um Candidato que teve Aprovação em um
        determinado Concurso;
        - ORDEM DE CHAMADA: é a posição na qual um Candidato teve sua Convocação em um
        determinado Concurso;
    - PESSOA: um indivíduo que é encontrado em um Documento.
        - CANDIDATO: uma Pessoa que pode ser encontrado em uma Lista de Inscritos,
        em uma Lista de Aprovados ou em uma Lista de Convocados;
    - PUBLICAÇÃO: é o nome de um documento externo ao sistema, e que pode possuir
    Documentos de interesse do sistema.
        - DOE: Diaŕio Oficial do Estado, pode conter uma Lista de Convocação;
        - ANEXO: (i.e.: Anexo ao Edital) pode conter Listas de Inscrição ou Lista de
        Aprovação.

"""
