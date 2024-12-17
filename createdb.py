import re
import PyPDF2
from pathlib import Path
from sqlmodel import SQLModel, Field


def capture_data(path: Path) -> list[tuple]:
    # TODO: create capture_data
    ...


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
