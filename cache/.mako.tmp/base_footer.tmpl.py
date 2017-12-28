# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1514481462.374063
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/base_footer.tmpl'
_template_uri = 'base_footer.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_footer']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        template_hooks = context.get('template_hooks', UNDEFINED)
        content_footer = context.get('content_footer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if content_footer:
            __M_writer('        <footer id="footer">\n            <p>')
            __M_writer(str(content_footer))
            __M_writer('</p>\n            ')
            __M_writer(str(template_hooks['page_footer']()))
            __M_writer('\n        </footer>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/goldengrape/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/base_footer.tmpl", "uri": "base_footer.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 10, "28": 3, "34": 3, "35": 4, "36": 5, "37": 6, "38": 6, "39": 7, "40": 7, "46": 40}}
__M_END_METADATA
"""
