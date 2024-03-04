from odoo import models,fields

class stockPickingBatchDock(models.Model):
    _name = "stock.picking.batch.dock"
    _description = "Dock"

    name = fields.Char("Dock",required=True)
