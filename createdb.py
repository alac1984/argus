import re
import PyPDF2
from sqlmodel import SQLModel, Field


def capture_data() -> list[tuple]:
    ...


def create_instances(data: list[tuple], instances: list) -> list[SQLModel]:
    ...


def insert_all(instances: list[SQLModel]) -> None:
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
