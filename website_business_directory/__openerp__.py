{
    'name': "Website Business Directory",
    'version': "0.8.2",
    'author': "Sythil Tech",
    'category': "Tools",
    'support': "steven@sythiltech.com.au",
    'summary': "A directory of local companies",
    'license':'LGPL-3',
    'data': [
        'views/res_partner_views.xml',
        'views/website_business_directory_templates.xml',
        'views/res_partner_directory_department_views.xml',
        'views/website_directory_category_views.xml',
        'views/website_directory_settings_views.xml',
        'views/website_directory_field_views.xml',
        'views/menus.xml',
        'data/website.menu.csv',
        'data/res.groups.csv',
        'data/website_directory_settings.xml',
        'data/website.directory.field.type.csv',
        'security/ir.model.access.csv',
        'security/ir.rule.xml',
    ],
    'demo': [],
    'depends': ['mail','website'],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}