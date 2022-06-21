from odoo import models, fields

class HmsPatient(models.Model):
    _name = "hms.patient"
    _description = "HMS patients"
    _rec_name = "first_name"

    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    cr_ration = fields.Float()
    history = fields.Html()
    blood_type = fields.Selection([
        ("A", "A"),
        ("B", "B"),
        ("A-", "A-"),
        ("A+", "A+")
    ])
    pcr = fields.Boolean()
    image = fields.Image()
    age = fields.Integar()
    address = fields.Text()

