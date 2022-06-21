from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, date
import re


class HmsPatient(models.Model):
    _name = "hms.patient"
    _description = "HMS patients"
    _rec_name = "first_name"

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    cr_ratio = fields.Float()
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
    department_capacity = fields.Integer(related="department_id.capacity")
    logs_ids = fields.Many2one("hms.patient.log ")
    state = fields.Selection([("un", "Undetermined"),
                              ("g", "Good"),
                              ("f", "Fair"),
                              ("s", "Serious")], default="un")
    doctors_ids = fields.Many2many("hms.doctor")
    _sql_constraints = [
        ('unique_email', 'unique(email)', "Email already exists."),
    ]

    email = fields.Char()


    def _onchange_age(self):
        if self.age and self.age < 30:
            self.pcr = True
            return {
                'warning': {
                    "Title": "Warning!",
                    "message": "PCR has been set to checked!"
                }
            }

    def set_good(self):
        self.state = "g"
        self.add_log("Good")

    def set_serious(self):
        self.state = "g"
        self.add_log("Serious")

    def set_undetermined(self):
        self.state = "u"
        self.add_log("Undetermined")

    def set_fair(self):
        self.state = "f"
        self.add_log("Fair")

    def add_log(self, state):
        self.env["hms.patient.log"].create({
            "description": f"State changed to {state}",
            "patient_id": self.id
        })

    @api.constrains('email')
    def _validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if not match:
                raise ValidationError('Not a valid E-mail ID')


class PatientLog(models.Model):
    _name = "hms.patient.log"
    description = fields.Text()
    patient_id = fields.Many2one("hms.patient")
