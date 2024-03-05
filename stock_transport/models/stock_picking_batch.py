from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from odoo.tools.float_utils import float_round

class stockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock = fields.Many2one('stock.picking.batch.dock',string="Dock")
    vehicle = fields.Many2one('fleet.vehicle.model',string="Vehicle")
    vehicle_category = fields.Many2one('fleet.vehicle.model.category',string="Vehicle category",store=True)
    weight_bar = fields.Float(compute="_compute_weight",string="Weight",default=0,store=True)
    volume_bar = fields.Float(compute="_compute_volume",string="Volume",default=0,store=True)
    transfers = fields.Float(compute="_compute_transfers",store=True)
    lines = fields.Float(compute="_compute_lines",store=True)
    date_start = fields.Date('Start Date',default=fields.Date.today())
    date_stop = fields.Date('Stop Date',default=fields.Date.today()+relativedelta(days=7))
    color = fields.Integer('color',default=1,store=False)

    # Compute methods
    @api.depends("move_line_ids","vehicle_category")
    def _compute_weight(self):
        for record in self:
            if record.vehicle_category.max_weight != 0:
                record.weight_bar = sum(record.move_line_ids.product_id.mapped('weight'))*100/record.vehicle_category.max_weight
            else:
                record.weight_bar = 0

    @api.depends("move_line_ids","vehicle_category")
    def _compute_volume(self):
        for record in self:
            if record.vehicle_category.max_volume != 0:
                record.volume_bar = sum(record.move_line_ids.product_id.mapped('volume'))*100/record.vehicle_category.max_volume
            else:
                record.volume_bar = 0

    @api.depends("transfers","picking_ids")
    def _compute_transfers(self):
        for record in self:
            record.transfers = len(record.picking_ids)

    @api.depends("lines","move_line_ids")
    def _compute_lines(self):
        for record in self:
            record.lines = len(record.move_line_ids)

    def _compute_display_name(self):
        for record in self:
            display_weight = float_round(sum(record.move_line_ids.product_id.mapped('weight')),precision_digits=2)
            display_volume = float_round(sum(record.move_line_ids.product_id.mapped('volume')),precision_digits=2)
            record.display_name = f"{record.name} ({display_weight} Kg, {display_volume} m³)"
