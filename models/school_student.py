from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = 'school.student'

    name = fields.Char(string='Nombres', required=True)
    lastname = fields.Char(string='Apellidos', required=True)
    photo = fields.Binary(string='Foto')
    birth_date = fields.Date()
    age = fields.Integer(compute='_compute_age', store=True)
    date_of_birth = fields.Selection([('h', 'Hombre'), ('m','Mujer'), ('o', 'Otro')], string='genero')

    final_exam_grade = fields.Float()
    subject_ids = fields.Many2many('school.subject', string='Subjects')

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = fields.Date.today()
                delta = today - record.birth_date
                record.age = int(delta.days / 365.25)
            else:
                record.age = 0
