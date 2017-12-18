# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513620228.004085
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/index_helper.tmpl'
_template_uri = 'index_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['mathjax_script', 'html_pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_katex = context.get('use_katex', UNDEFINED)
        any = context.get('any', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if any(post.is_mathjax for post in posts):
            if use_katex:
                __M_writer('            <script src="//cdnjs.cloudflare.com/ajax/libs/KaTeX/0.3.0/katex.min.js"></script>\n            <script src="//cdnjs.cloudflare.com/ajax/libs/KaTeX/0.3.0/contrib/auto-render.min.js"></script>\n            <script>\n                renderMathInElement(document.body);\n            </script>\n')
            else:
                __M_writer('            <script type="text/javascript" src="//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>\n            <script type="text/x-mathjax-config">\n            MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n            </script>\n')
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


"""
__M_BEGIN_METADATA
{"filename": "/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/index_helper.tmpl", "uri": "index_helper.tmpl", "line_map": {"64": 13, "65": 13, "66": 13, "67": 16, "73": 67, "16": 0, "21": 19, "22": 36, "28": 21, "34": 21, "35": 22, "36": 23, "37": 24, "38": 29, "39": 30, "45": 2, "52": 2, "53": 3, "54": 4, "55": 6, "56": 7, "57": 8, "58": 8, "59": 8, "60": 8, "61": 11, "62": 12, "63": 13}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
