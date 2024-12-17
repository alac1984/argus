from pathlib import Path
from createdb import capture_data

def test_capture_data():
    path = Path('tests/testdata.pdf')
    data = capture_data(path)

    assert len(data) == 76 + 76 + 25 + 48
    assert len(data[0]) == 6
    assert len(data[122]) == 6
    assert data[0][0] == 'Wellington Rodrigues De Sousa'
    assert data[0][1] == '1040013396'
    assert data[0][2] == 2.0
    assert data[0][3] == 8.0
    assert data[0][4] == 13.0
    assert data[0][5] == 23.0
    assert data[1][0] == 'Wellington Sabino Garcia'
    assert data[1][1] == '1040010924'
    assert data[1][2] == 3.0
    assert data[1][3] == 11.0
    assert data[1][4] == 13.0
    assert data[1][5] == 27.0
    assert data[17][0] == 'Wilker Ferreira Silva'
    assert data[17][1] == '1040028902'
    assert data[17][2] == 1.0
    assert data[17][3] == 9.0
    assert data[17][4] == 13.0
    assert data[17][5] == 23.0
    assert data[48][0] == 'Abel Ferreira Dos Santos'
    assert data[48][1] == '1050017771'
    assert data[48][2] == 3.0
    assert data[48][3] == 8.0
    assert data[48][4] == 12.0
    assert data[48][5] == 23.0
    assert data[73][0] == 'Adriana Helia Rodrigues Ximenes'
    assert data[73][1] == '1050027492'
    assert data[73][2] == 4.0
    assert data[73][3] == 10.0
    assert data[73][4] == 13.0
    assert data[73][5] == 27.0


# TODO: test_create_instances
# TODO: test_insert_all
