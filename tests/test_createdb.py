from pathlib import Path
from createdb import capture_data

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
