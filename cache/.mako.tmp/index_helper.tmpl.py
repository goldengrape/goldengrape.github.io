# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1582039816.007195
_enable_loop = True
_template_filename = '/Volumes/macTF/Application/miniconda3/lib/python3.7/site-packages/nikola/data/themes/bootstrap4/templates/index_helper.tmpl'
_template_uri = 'index_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        nextlink = context.get('nextlink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if prevlink or nextlink:
            __M_writer('        <ul class="pager postindexpager clearfix">\n')
            if prevlink:
                __M_writer('            <li class="previous"><a href="')
                __M_writer(str(prevlink))
                __M_writer('" rel="prev">')
                __M_writer(str(messages("Newer posts")))
                __M_writer('</a></li>\n')
            if nextlink:
                __M_writer('            <li class="next"><a href="')
                __M_writer(str(nextlink))
                __M_writer('" rel="next">')
                __M_writer(str(messages("Older posts")))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Volumes/macTF/Application/miniconda3/lib/python3.7/site-packages/nikola/data/themes/bootstrap4/templates/index_helper.tmpl", "uri": "index_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 13, "27": 2, "34": 2, "35": 3, "36": 4, "37": 5, "38": 6, "39": 6, "40": 6, "41": 6, "42": 6, "43": 8, "44": 9, "45": 9, "46": 9, "47": 9, "48": 9, "49": 11, "55": 49}}
__M_END_METADATA
"""
