from marshmallow import Schema, fields, post_load
from model.argentineBank_model import ArgentineBank


class ArgentineBankSchema(Schema):
    """ArgentineBank Schema"""

    bank_name = fields.String(attribute="bank_name")
    time = fields.String(attribute="time")
    compra = fields.Float(attribute="compra")
    venta = fields.Float(attribute="venta")
    valor_con_impuestos = fields.Float(attribute="valor_con_impuestos")


    @post_load
    def create_argentine_bank(self, data, **kwargs):
        return ArgentineBank(**data)
