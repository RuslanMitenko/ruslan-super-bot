from .actions import ActInterface
from .models import db, History

db.connect()
db.create_tables([History])

if __name__ == '__main__':
    action = ActInterface()
