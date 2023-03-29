from odoo import models, fields

class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    
    name = fields.Char(string="Teacher Name", required=True)
    profile = fields.Text(string="Profile")
    subject_ids = fields.One2many('school.subject', 'teacher_id', string="Subjects")
