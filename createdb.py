import re
import pypdf
from pathlib import Path
from sqlmodel import SQLModel, Field


def capture_data(path: Path) -> list[tuple]:
    # TODO: create capture_data
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
            # Loopando pelas linhas
            for line in lines:
                # Ignorando os cabeçalhos
                if "NOME" in line and "INSCRIÇÃO" in line:
                    continue

                # Pattern para pegar os dados
                pattern = re.compile(
                    r"([\w\s\(\)\.,çãáéóêô]+?)\s+(\d{10})\s+(\d+\.\d{2})\s+(\d+\.\d{2})\s+(\d+\.\d{2})\s+(\d+\.\d{2})"
                )
                # Dar match na linha
                match = pattern.match(line)

                if match:
                    table_data.append(tuple(match.groups()))

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
