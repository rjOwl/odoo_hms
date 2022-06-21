from odoo import models, fields

class HmsDoctor(models.Model):
    _name = "hms.doctor"
    _description = "HMS Doctor"
    # _rec_name = "first_name"

    first_name = fields.Char(required=True)
    last_name = fields.Char()
    image = fields.Image()

