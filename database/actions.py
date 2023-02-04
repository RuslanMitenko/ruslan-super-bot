from typing import Dict, List, TypeVar
from .models import db, ModelBase
from peewee import ModelBase, ModelSelect

T = TypeVar('T')


def _store_date(db: db, model: T, *data: List[Dict]) -> None:
    with db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(db: db, model: T, *colums: ModelBase) -> ModelSelect:
    with db.atomic():
        response = model.select(*colums)

    return response


class ActInterface():
    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrieve():
        return _retrieve_all_data


if __name__ == '__main__':
    _store_date()
    _retrieve_all_data()
    ActInterface()
