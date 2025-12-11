# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class RopaNomina(models.Model):
    _name = 'nominas.ropa.nomina'
    _description = 'Nómina de empleado tienda de ropa'

    employee_id = fields.Many2one(
        'res.partner',
        string='Empleado',
        required=True,
        domain=[('is_company', '=', False)],
    )

    base_salary = fields.Float(string='Sueldo base', required=True)
    line_ids = fields.One2many(
        'nominas.ropa.linea',
        'nomina_id',
        string='Bonificaciones y deducciones'
    )

    irpf_percent = fields.Float(string='IRPF (%)', required=True, default=15.0)
    irpf_amount = fields.Float(
        string='IRPF pagado (€)',
        compute='_compute_amounts',
        store=True,
    )

    gross_for_irpf = fields.Float(
        string='Sueldo bruto para IRPF',
        compute='_compute_amounts',
        store=True,
    )
    total_bonuses = fields.Float(
        string='Total bonificaciones',
        compute='_compute_amounts',
        store=True,
    )
    total_deductions = fields.Float(
        string='Total deducciones',
        compute='_compute_amounts',
        store=True,
    )

    date = fields.Date(
        string='Fecha',
        default=fields.Date.context_today,
        required=True,
    )

    transfer_document = fields.Binary(
        string='Justificante de transferencia'
    )
    transfer_filename = fields.Char(string='Nombre justificante')

    state = fields.Selection(
        [
            ('draft', 'Redactada'),
            ('confirmed', 'Confirmada'),
            ('paid', 'Pagada'),
        ],
        string='Estado',
        default='draft',
    )

    @api.depends('base_salary', 'line_ids.amount', 'line_ids.line_type', 'irpf_percent')
    def _compute_amounts(self):
        for record in self:
            bonuses = sum(record.line_ids.filtered(lambda l: l.line_type == 'bonus').mapped('amount'))
            deductions = sum(record.line_ids.filtered(lambda l: l.line_type == 'deduction').mapped('amount'))
            record.total_bonuses = bonuses
            record.total_deductions = deductions

            record.gross_for_irpf = (record.base_salary or 0.0) + bonuses

            if record.irpf_percent and record.irpf_percent > 0:
                record.irpf_amount = record.gross_for_irpf * record.irpf_percent / 100.0
            else:
                record.irpf_amount = 0.0

    @api.constrains('base_salary', 'irpf_percent', 'line_ids')
    def _check_values(self):
        for record in self:
            if record.base_salary < 0:
                raise ValidationError("El sueldo base no puede ser negativo.")
            if record.irpf_percent < 0 or record.irpf_percent > 100:
                raise ValidationError("El porcentaje de IRPF debe estar entre 0 y 100.")
            for line in record.line_ids:
                if line.amount < 0:
                    raise ValidationError("Las bonificaciones y deducciones no pueden tener importe negativo.")

    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'

    def action_set_draft(self):
        for record in self:
            record.state = 'draft'

    def action_mark_paid(self):
        for record in self:
            record.state = 'paid'
