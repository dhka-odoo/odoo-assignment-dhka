from odoo import models,fields,api

class stockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock = fields.Many2one('stock.picking.batch.dock',string="Dock")
    vehicle = fields.Many2one('fleet.vehicle.model',string="Vehicle")
    vehicle_category = fields.Many2one('fleet.vehicle.model.category',string="Vehicle category",store=True)
    weight_bar = fields.Float(compute="_compute_weight",string="Weight",default=0,store=True)
    volume_bar = fields.Float(compute="_compute_volume",string="Volume",default=0,store=True)
    transfers = fields.Float(compute="_compute_transfers",store=True)
    lines = fields.Float(compute="_compute_lines",store=True)

    @api.depends("move_line_ids","vehicle_category")
    def _compute_weight(self):
        for record in self:
            if record.vehicle_category:
                record.weight_bar = sum(record.move_line_ids.product_id.mapped('weight'))*100/record.vehicle_category.max_weight
            else:
                record.weight_bar = 0

    @api.depends("move_line_ids","vehicle_category")
    def _compute_volume(self):
        for record in self:
            if record.vehicle_category:
                record.volume_bar = sum(record.move_line_ids.product_id.mapped('volume'))*100/record.vehicle_category.max_volume
            else:
                record.volume_bar = 0

    @api.depends("transfers","picking_ids")
    def _compute_transfers(self):
        for record in self:
            record.transfers = len(record.picking_ids)

    @api.depends("lines","move_line_ids")
    def _compute_transfers(self):
        for record in self:
            record.lines = len(record.move_line_ids)
