# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class RopaRentaAnual(models.Model):
    _name = 'nominas.ropa.renta'
    _description = 'Declaración de la renta anual de empleado'

    employee_id = fields.Many2one(
        'res.partner',
        string='Empleado',
        required=True,
        domain=[('is_company', '=', False)],
    )

    year = fields.Integer(string='Año', required=True)

    nomina_ids = fields.Many2many(
        'nominas.ropa.nomina',
        'nominas_ropa_renta_nomina_rel',
        'renta_id',
        'nomina_id',
        string='Nóminas incluidas',
    )

    total_gross = fields.Float(
        string='Sueldo bruto total',
        compute='_compute_totals',
        store=True,
    )

    total_irpf = fields.Float(
        string='IRPF total pagado',
        compute='_compute_totals',
        store=True,
    )

    @api.depends('nomina_ids.gross_for_irpf', 'nomina_ids.irpf_amount')
    def _compute_totals(self):
        for record in self:
            record.total_gross = sum(record.nomina_ids.mapped('gross_for_irpf'))
            record.total_irpf = sum(record.nomina_ids.mapped('irpf_amount'))

    @api.constrains('nomina_ids', 'year', 'employee_id')
    def _check_nominas(self):
        for record in self:
            if len(record.nomina_ids) > 14:
                raise ValidationError("Una declaración de la renta no puede tener más de 14 nóminas.")

            for nomina in record.nomina_ids:
                if nomina.employee_id != record.employee_id:
                    raise ValidationError("Todas las nóminas deben ser del mismo empleado.")
                if nomina.date and nomina.date.year != record.year:
                    raise ValidationError("Todas las nóminas deben pertenecer al mismo año natural indicado.")
