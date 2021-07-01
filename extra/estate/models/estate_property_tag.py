from odoo import fields, models, api


class EstatePropertyType(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _order = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    # Basic
    name = fields.Char("Name", required=True)
    color = fields.Integer("Color Index")

