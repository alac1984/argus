"""

    DOC: cli/__init__.py

    Lista de comandos:

    - exibir (grupo)
    Grupo de comandos que mostram dados do sistema

        - exibir concurso  id <id> | --nome <nome> | --sem-extrator | --all
        Exibe um, alguns ou todos os concursos inseridos

        - exibir arquivo  id <id> | --nome <nome> | --all
        Exibe um, alguns ou todos os arquivos inseridos

        - exibir extrator --id <id> | --concurso <id ou nome> | --documento <id ou nome> | --all
        Exibe um, alguns ou todos os extratores inseridos

        - exibir erro-inscricao --id <id> | --concurso <id ou nome> | --all
        Exibe um, alguns ou todos os Erros de Inscrição gerados

        - exibir erro-aprovacao --id <id> | --concurso <id ou nome> | --all
        Exibe um, alguns ou todos os Erros de Aprovação gerados

        - exibir erro-convocacao --id <id> | --concurso <id ou nome> | --all
        Exibe um, alguns ou todos os Erros de Convocacao gerados

    - inserir (grupo)
    Grupo de comandos que inserem dados no sistema

        - inserir dados --arquivo <path>
        Insere um JSON com dados para persistência

        - inserir arquivo --concurso <id ou nome> | --caminho <path>
        Insere Arquivo no sistema (copia para pasta específica)

    - processar (grupo)
    Grupo de comandos que processam dados de uma Publicação

        - processar arquivo --id <id> | --concurso <id ou nome> | --todos-pendentes
        Processa um, alguns ou todos os arquivos pendentes em busca de Publicações

        - processar publicacao --id <id> | --concurso <id ou nome> | --todos-pendentes
        Processa uma, algumas ou todas as publicações pendentes em busca de Documentos

        - processar lista-inscricao --id <id> | --concurso <id ou nome> | --todos-pendentes
        Processa uma, algumas ou todas as Listas de Inscrição pendentes em busca de Inscrições

        - processar lista-aprovacao --id <id> | --concurso <id ou nome> | --todos-pendentes
        Processa uma, algumas ou todas as Listas de Aprovacao pendentes em busca de Aprovações

        - processar lista-convocacao --id <id> | --concurso <id ou nome> | --todos-pendentes
        Processa uma, algumas ou todas as Listas de Convocação pendentes em busca de Convocações

        - processar inscricao --id <id> | --nome <nome> | --todos-pendentes
        Processa uma, algumas ou todas as Inscrições pendentes

        - processar aprovacao --id <id> | --nome <nome> | --todos-pendentes
        Processa uma, algumas ou todas as Aprovações pendentes

        - processar convocacao --id <id> | --nome <nome> | --todos-pendentes
        Processa uma, algumas ou todas as Convocações pendentes

"""
