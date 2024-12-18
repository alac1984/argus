from pathlib import Path
from createdb import Line, LineType, capture_data, process_line


def test_process_line_case_header():
    line = 'NOME INSCRIÇÃO Língua ', 'Portuguesa', 'Conhecimentos ', 'Educacionais', 'Conhecimentos ', 'EspecíficosNOTA OBJETIVA'

    result = process_line(line)

    assert result.type = LineType.HEADER

def test_process_line_case_type():
    line1 = '401 - PROFESSOR   ANOS INICIAIS (1º AO 5º ANO) - TODAS AS ÁREAS DA EDUCAÇÃO BÁSICA '
    line2 = '410 - PROFESSOR ENSINO FUNDAMENTAL (ANOS FINAIS) OU MÉDIO - LÍNGUA PORTUGUESA '

    result1 = process_line(line1)
    result2 = process_line(line2)

    assert result1.type = LineType.SUBJECT
    assert result2.type = LineType.SUBJECT
    assert result1.code = 401
    assert result2.code = 410

def test_process_line_case_candidate():
    line = 'Abgail Marrocos Silva 0340050033 2.00 6.00 10.00 18.00'

    result = process_line(line)

    assert result.type = LineType.CANDIDATE
    assert result.content = 'Abgail Marrocos Silva 0340050033 2.00 6.00 10.00 18.00'

def test_process_line_case_anexo():
    line = 'ANEXO ÚNICO - EDITAL DE RESULTADO DA PROVA OBJETIVA – PRELIMINAR'

    result = process_line(line)

    assert result.type = LineType.ANEXO

def test_process_line_case_secretaria():
    line1 = 'SECRETARIA DA EDUCAÇÃO DO ESTADO DO CEARÁ'
    line1 = 'SEDUC'

    result1 = process_line(line1)
    result2 = process_line(line2)

    assert result1.type = LineType.ANEXO
    assert result2.type = LineType.ANEXO

def test_capture_data():
    path = Path('tests/testdata.pdf')
    data = capture_data(path)

    assert data is not None
    assert hasattr(data, '__iter__')
    assert len(data) == 224
    assert len(data[0]) == 6
    assert len(data[122]) == 6
    assert data[0][0] == 'Wellington Rodrigues De Sousa'
    assert data[0][1] == '1040013396'
    assert data[0][2] == '2.00'
    assert data[0][3] == '8.00'
    assert data[0][4] == '13.00'
    assert data[0][5] == '23.00'
    assert data[1][0] == 'Wellington Sabino Garcia'
    assert data[1][1] == '1040010924'
    assert data[1][2] == '3.00'
    assert data[1][3] == '11.00'
    assert data[1][4] == '13.00'
    assert data[1][5] == '27.00'
    assert data[16][0] == 'Wilker Ferreira Silva'
    assert data[16][1] == '1040028902'
    assert data[16][2] == '1.00'
    assert data[16][3] == '9.00'
    assert data[16][4] == '13.00'
    assert data[16][5] == '23.00'
    assert data[47][0] == 'Abel Ferreira Dos Santos'
    assert data[47][1] == '1050017771'
    assert data[47][2] == '3.00'
    assert data[47][3] == '8.00'
    assert data[47][4] == '12.00'
    assert data[47][5] == '23.00'
    assert data[72][0] == 'Adriana Helia Rodrigues Ximenes'
    assert data[72][1] == '1050027492'
    assert data[72][2] == '4.00'
    assert data[72][3] == '10.00'
    assert data[72][4] == '13.00'
    assert data[72][5] == '27.00'


# TODO: test_create_instances
# TODO: test_insert_all
