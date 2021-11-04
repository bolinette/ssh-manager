from bolinette import core, types
from bolinette.decorators import model


@model('key')
class Key(core.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True)
    uid = types.defs.Column(types.db.String, entity_key=True, nullable=False)
    name = types.defs.Column(types.db.String, nullable=False)
