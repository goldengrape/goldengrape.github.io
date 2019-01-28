# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548660868.500753
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/list.tmpl'
_template_uri = 'list.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('archive_nav', context._clean_inheritance_tokens(), templateuri='archive_navigation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'archive_nav')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
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
        _import_ns = {}
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<article class="listpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n    </header>\n    ')
        __M_writer(str(archive_nav.archive_navigation()))
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.translation_link()))
        __M_writer('\n')
        if items:
            __M_writer('    <ul class="postlist">\n')
            for text, link, count in items:
                __M_writer('        <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(text)))
                __M_writer('</a>\n')
                if count:
                    __M_writer('            (')
                    __M_writer(str(count))
                    __M_writer(')\n')
            __M_writer('    </ul>\n')
        else:
            __M_writer('    <p>')
            __M_writer(str(messages("Nothing found.")))
            __M_writer('</p>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/goldengrape/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/list.tmpl", "uri": "list.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "32": 0, "47": 2, "48": 3, "49": 4, "54": 26, "60": 6, "74": 6, "75": 9, "76": 9, "77": 11, "78": 11, "79": 12, "80": 12, "81": 13, "82": 14, "83": 15, "84": 16, "85": 16, "86": 16, "87": 16, "88": 16, "89": 17, "90": 18, "91": 18, "92": 18, "93": 21, "94": 22, "95": 23, "96": 23, "97": 23, "98": 25, "104": 98}}
__M_END_METADATA
"""
