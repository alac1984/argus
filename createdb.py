import re
import pypdf
from pathlib import Path
from enum import Enum
from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class LineType(Enum):
    HEADER = 1
    SUBJECT = 2
    CANDIDATE = 3
    ANEXO = 4
    SECRETARIA = 5


class Line(BaseModel):
    type: LineType
    content: tuple | None = None
    code: int | None = None

# TODO: create Candidate model (SQLModel)


class CandidateCreate(BaseModel):
    # TODO: create CandidateCreate model
    ...


def process_line(line: str) -> Line | None:
    header_regex = re.compile(r"\b(NOME|INSCRIÇÃO|Língua|Portuguesa|Conhecimentos|Educacionais|EspecíficosNOTA\sOBJETIVA)\b")
    subject_regex = re.compile(r"(4\d{2})\s-\sPROFESSOR")
    candidate_regex = re.compile(
        r"([\w\s\(\)\.,çãáéóêô]+?)\s+(\d{10})\s+(\d+\.\d{2})\s+(\d+\.\d{2})\s+(\d+\.\d{2})\s+(\d+\.\d{2})"
    )
    anexo_regex = re.compile(r"ANEXO ÚNICO - ")
    secretaria_regex = re.compile(r"(SECRETARIA DA EDUCAÇÃO DO ESTADO DO CEARÁ|SEDUC)")

    match = candidate_regex.match(line)
    if match:
        return Line(type=LineType.CANDIDATE, content=tuple(match.groups()))

    match = subject_regex.match(line)
    if match:
        return Line(type=LineType.SUBJECT, code=int(match.group(1)))

    match = header_regex.match(line)
    if match:
        return Line(type=LineType.HEADER)

    match = anexo_regex.match(line)
    if match:
        return Line(type=LineType.ANEXO)

    match = secretaria_regex.match(line)
    if match:
        return Line(type=LineType.SECRETARIA)

    return None

def capture_data(path: Path) -> list[tuple]:
    """
    Captura os dados dos professores, linha a linha, considerando
    o tipo (type) de concurso que ele realizou
    """
    table_data = []

    # Abrir o PDF
    with open(path, 'rb') as file:
        # Lê o PDF com o PyPDF2
        reader = pypdf.PdfReader(file)

        # Loopando pelas paǵinas
        for page_num, page in enumerate(reader.pages):
            # Extrai o texto da página
            text = page.extract_text()
            # Dividindo em linhas
            lines = text.splitlines()
            # Inicializa a variável que salvará o último código
            last_code = None
            # Loopando pelas linhas
            for line in lines:
                result = process_line(line)

                if line.type == LineType.CANDIDATE:
                    # TODO: implement the CandidateCreate logic here

                # TODO: implement the logic for other LineTypes

    return table_data


def create_instances(data: list[tuple], instances: list) -> list[SQLModel]:
    # TODO: create create_instances
    ...


def insert_all(instances: list[SQLModel]) -> None:
    # TODO: create insert_all
    ...


if __name__ == "__main__":
    # Captura os dados do PDF
    data = capture_data()

    # Cria as instâncias
    instances = []
    create_instances(data, instances)

    # Insere no banco
    insert_all(instances)

    # Print the result
    print(result)
