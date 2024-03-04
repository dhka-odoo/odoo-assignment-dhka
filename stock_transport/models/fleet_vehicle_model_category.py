from odoo import models,fields

class estateProperty(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float('Max Weight (Kg)')
    max_volume = fields.Float('Max Volume (m³)')

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.max_weight} Kg, {record.max_volume} m³)"
