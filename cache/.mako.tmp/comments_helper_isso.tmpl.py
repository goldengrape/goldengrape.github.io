# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1575984845.375627
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl'
_template_uri = 'comments_helper_isso.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        isso_config = context.get('isso_config', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <div data-title="')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('" id="isso-thread"></div>\n        <script src="')
            __M_writer(str(comment_system_id))
            __M_writer('js/embed.min.js" data-isso="')
            __M_writer(str(comment_system_id))
            __M_writer('" data-isso-lang="')
            __M_writer(str(lang))
            __M_writer('"\n')
            if isso_config:
                for k, v in isso_config.items():
                    __M_writer('        data-isso-')
                    __M_writer(str(k))
                    __M_writer('="')
                    __M_writer(str(v))
                    __M_writer('"\n')
            __M_writer('        ></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <a href="')
            __M_writer(str(link))
            __M_writer('#isso-thread">Comments</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id and 'index' in pagekind:
            __M_writer('        <script src="')
            __M_writer(str(comment_system_id))
            __M_writer('js/count.min.js" data-isso="')
            __M_writer(str(comment_system_id))
            __M_writer('" data-isso-lang="')
            __M_writer(str(lang))
            __M_writer('"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/goldengrape/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl", "uri": "comments_helper_isso.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 13, "22": 19, "23": 26, "29": 2, "36": 2, "37": 3, "38": 4, "39": 4, "40": 4, "41": 5, "42": 5, "43": 5, "44": 5, "45": 5, "46": 5, "47": 6, "48": 7, "49": 8, "50": 8, "51": 8, "52": 8, "53": 8, "54": 11, "60": 15, "65": 15, "66": 16, "67": 17, "68": 17, "69": 17, "75": 22, "82": 22, "83": 23, "84": 24, "85": 24, "86": 24, "87": 24, "88": 24, "89": 24, "90": 24, "96": 90}}
__M_END_METADATA
"""
