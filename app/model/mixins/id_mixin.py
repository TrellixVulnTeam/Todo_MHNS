import uuid
from app.database import db


class IdMixin(object):
    id = db.Column(db.String(36), default=lambda: uuid.uuid4(), primary_key=True)
