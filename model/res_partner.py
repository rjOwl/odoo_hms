from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    related_patient_id = fields.Many2one("hms.patient")

    @api.constrains("related_patient_id")
    def _validate_email(self):
        if self.related_patient_id.email and self.related_patient_id.email != self.email:
            raise ValidationError("Patient has a Different Email")

    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise ValidationError("Can't delete customer with related Patient")
        return super().unlink()
