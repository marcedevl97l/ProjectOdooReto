{
    'name': 'Reto Practicante Programador',
    'sumary': 'Este modulo nos permitira gestionar los datos y credenciales de una escuela'
    'version': '1.0',
    'author': "Marcelo Sebastian Reyes Montenegro"
    'category': 'Tools'
    #Dependencias, base significa que no depende de otro modulo
    'depends': ['base'],
    'data': [
        'views/school_student_views',
        'views/school_subject_views',
        'views/school_teacher_views',
        'views/menu_item_views.xml',
    ],
    'installable': True,
    'auto-install': 'False'
}