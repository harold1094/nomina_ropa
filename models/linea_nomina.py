# -*- coding: utf-8 -*-
from odoo import models, fields

class RopaNominaLinea(models.Model):
    _name = 'nominas.ropa.linea'
    _description = 'Bonificación o deducción de nómina'

    nomina_id = fields.Many2one(
        'nominas.ropa.nomina',
        string='Nómina',
        required=True,
        ondelete='cascade',
    )

    line_type = fields.Selection(
        [
            ('bonus', 'Bonificación'),
            ('deduction', 'Deducción'),
        ],
        string='Tipo',
        required=True,
        default='bonus',
    )

    amount = fields.Float(string='Importe bruto', required=True)
    concept = fields.Char(string='Concepto', required=True)
