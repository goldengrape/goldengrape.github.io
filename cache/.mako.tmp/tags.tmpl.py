# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1579788614.3918421
_enable_loop = True
_template_filename = '/Volumes/macTF/Application/miniconda3/lib/python3.7/site-packages/nikola/data/themes/bootstrap4/templates/tags.tmpl'
_template_uri = 'tags.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        title = context.get('title', UNDEFINED)
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        title = context.get('title', UNDEFINED)
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if cat_items:
            if items:
                __M_writer('        <h2>')
                __M_writer(str(messages("Categories")))
                __M_writer('</h2>\n')
            for text, full_name, path, link, indent_levels, indent_change_before, indent_change_after in cat_hierarchy:
                for i in range(indent_change_before):
                    __M_writer('            <ul class="list-inline">\n')
                __M_writer('        <li class="list-inline-item"><a class="reference badge badge-secondary" href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(text)))
                __M_writer('</a>\n')
                if indent_change_after <= 0:
                    __M_writer('            </li>\n')
                for i in range(-indent_change_after):
                    __M_writer('            </ul>\n')
                    if i + 1 < len(indent_levels):
                        __M_writer('                </li>\n')
            if items:
                __M_writer('        <h2>')
                __M_writer(str(messages("Tags")))
                __M_writer('</h2>\n')
        if items:
            __M_writer('    <ul class="list-inline">\n')
            for text, link in items:
                if text not in hidden_tags:
                    __M_writer('            <li class="list-inline-item"><a class="reference badge badge-secondary" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(filters.html_escape(str(text)))
                    __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Volumes/macTF/Application/miniconda3/lib/python3.7/site-packages/nikola/data/themes/bootstrap4/templates/tags.tmpl", "uri": "tags.tmpl", "source_encoding": "utf-8", "line_map": {"27": 0, "42": 2, "47": 38, "53": 4, "67": 4, "68": 5, "69": 5, "70": 6, "71": 7, "72": 8, "73": 8, "74": 8, "75": 10, "76": 11, "77": 12, "78": 14, "79": 14, "80": 14, "81": 14, "82": 14, "83": 15, "84": 16, "85": 18, "86": 19, "87": 20, "88": 21, "89": 25, "90": 26, "91": 26, "92": 26, "93": 29, "94": 30, "95": 31, "96": 32, "97": 33, "98": 33, "99": 33, "100": 33, "101": 33, "102": 36, "108": 102}}
__M_END_METADATA
"""
