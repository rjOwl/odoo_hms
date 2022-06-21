from odoo import models, fields

class HmsPatient(models.Model):
    _name = "hms.patient"
    _description = "HMS patients"
    _rec_name = "first_name"

    first_name = fields.Char(required=True)
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
    age = fields.Integer()
    address = fields.Text()
    department_id = fields.Many2one("hms.department")

