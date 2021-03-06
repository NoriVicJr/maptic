# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = T('Sistema de Mapeamento das TICs nas Escolas')

#http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Bruno Barbosa'
response.meta.description = 'Sistema de Mapeamento das TICs nas Escolas'
response.meta.keywords = 'web2py, python, framework, TIC, NTE, Samambaia'
response.meta.generator = 'Web2py Enterprise Framework'
response.meta.copyright = 'Copyright 2011'


##########################################
## Criando seus menus
##########################################

if 'auth' in globals():
    # Verifica se algum usuario esta logado
    if not auth.is_logged_in():
        response.menu = [
            (T('Home'), False, URL(request.application,'default','index'), []),
            (T('Sobre'), False, URL(request.application,'default','sobre'), []),
            ]
    else:    # Caso estiver logado exibe os menus de acordo com sua permissao
        if auth.has_membership('Administrador'):
            response.menu = [
                (T('Home'), False, URL('default','index'), []),
                (T('Wiki'), False, URL('wiki','index'), []),
                (T('Relatórios'), False, URL('relatorios', 'index'), []),
                (T('Escolas'), False, URL('admin', 'escolas', args=['lista']), []),
                (T('Usuarios'), False, URL('admin', 'usuarios', args=['lista']), []),
                #(T('Autorizados'), False, URL('usuarios', 'autorizados'), [])
                ]
        if auth.has_membership('Tecnico'):
            response.menu = [
                (T('Home'), False, URL(request.application,'atividades','index'), []),
                (T('Escolas'), False, URL('escolas', 'lista'), []),
                (T('Relatórios'), False, URL('relatorios', 'lista'), [])
                ]
        if auth.has_membership('Escola'):
            response.menu = [
                (T('Home'), False, URL(request.application,'escola','index'), []),
                (T('Help'), False, URL(request.application,'wiki','index'), [])
                ]
