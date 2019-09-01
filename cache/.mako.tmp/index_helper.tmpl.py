# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1567318812.918654
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/index_helper.tmpl'
_template_uri = 'index_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_pager', 'mathjax_script']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if prevlink or nextlink:
            __M_writer('        <nav class="postindexpager">\n        <ul class="pager">\n')
            if prevlink:
                __M_writer('            <li class="previous">\n                <a href="')
                __M_writer(str(prevlink))
                __M_writer('" rel="prev">')
                __M_writer(str(messages("Newer posts")))
                __M_writer('</a>\n            </li>\n')
            if nextlink:
                __M_writer('            <li class="next">\n                <a href="')
                __M_writer(str(nextlink))
                __M_writer('" rel="next">')
                __M_writer(str(messages("Older posts")))
                __M_writer('</a>\n            </li>\n')
            __M_writer('        </ul>\n        </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/goldengrape/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/index_helper.tmpl", "uri": "index_helper.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "31": 2, "32": 20, "33": 25, "39": 3, "46": 3, "47": 4, "48": 5, "49": 7, "50": 8, "51": 9, "52": 9, "53": 9, "54": 9, "55": 12, "56": 13, "57": 14, "58": 14, "59": 14, "60": 14, "61": 17, "67": 23, "72": 23, "73": 24, "74": 24, "80": 74}}
__M_END_METADATA
"""
