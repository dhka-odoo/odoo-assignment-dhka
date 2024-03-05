from odoo import models,fields,api

class stockPickingBatch(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(compute="_compute_volume")

    # compute methods
    @api.depends("move_line_ids")
    def _compute_volume(self):
        for record in self:
            record.volume = sum(record.move_line_ids.product_id.mapped('volume'))
