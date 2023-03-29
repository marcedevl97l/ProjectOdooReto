from odoo import models, fields

class SchoolSubject(models.Model):
    _name = 'school.subject'

    subject_name = fields.Char("Name or description")
    credits = fields.Integer()
    max_students = fields.Integer()
    active = fields.Boolean(default=True)
    student_ids = fields.Many2many('school.student', string='Students')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')

