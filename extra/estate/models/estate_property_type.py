
# -*- coding: utf-8 -*-

from odoo import fields, models


class EstatePropertyType(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "sequence, name"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("Name", required=True)
    sequence = fields.Integer("Sequence", default=10)

    # Relational (for inline view)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")




