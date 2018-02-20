# -*- coding: utf-8 -*-
from jinja2 import Template


def get_auth_page(auth=False):
    html = open('templates/login_page.html').read()
    template = Template(html)
    return template.render(auth=auth)


def get_register_page():
    html = open('templates/register_page.html').read()
    template = Template(html)
    return template.render()
