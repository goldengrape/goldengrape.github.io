# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1514481462.367861
_enable_loop = True
_template_filename = 'themes/lanyon/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_header', 'html_site_title', 'html_navigation_links', 'html_translation_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def html_translation_header():
            return render_html_translation_header(context)
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_site_title():
            return render_html_site_title(context)
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <header id="header" role="banner">\n        ')
        __M_writer(str(html_site_title()))
        __M_writer('\n        ')
        __M_writer(str(html_translation_header()))
        __M_writer('\n        ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n')
        if search_form:
            __M_writer('            <div class="searchform" role="search">\n                ')
            __M_writer(str(search_form))
            __M_writer('\n            </div>\n')
        __M_writer('    </header>\n    ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <h3 id="brand" class="masthead-title">\n      <a href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('" title="')
        __M_writer(str(blog_title))
        __M_writer('" rel="home">')
        __M_writer(str(blog_title))
        __M_writer('</a>\n    </h3>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <nav id="menu" role="navigation" class="sidebar-nav">\n')
        for url, text in navigation_links[lang]:
            __M_writer('        <a class="sidebar-nav-item" href="')
            __M_writer(str(url))
            __M_writer('">')
            __M_writer(str(text))
            __M_writer('</a>\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <div id="toptranslations">\n            <h2>')
            __M_writer(str(messages("Languages:")))
            __M_writer('</h2>\n            ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/lanyon/templates/base_header.tmpl", "uri": "base_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 16, "35": 22, "36": 32, "37": 42, "43": 4, "57": 4, "58": 6, "59": 6, "60": 7, "61": 7, "62": 8, "63": 8, "64": 9, "65": 10, "66": 11, "67": 11, "68": 14, "69": 15, "70": 15, "76": 18, "86": 18, "87": 20, "88": 20, "89": 20, "90": 20, "91": 20, "92": 20, "98": 24, "107": 24, "108": 26, "109": 27, "110": 27, "111": 27, "112": 27, "113": 27, "114": 29, "115": 29, "116": 29, "117": 30, "118": 30, "124": 35, "134": 35, "135": 36, "136": 37, "137": 38, "138": 38, "139": 39, "140": 39, "146": 140}}
__M_END_METADATA
"""
