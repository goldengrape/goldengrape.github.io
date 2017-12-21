# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513862317.335451
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/bootstrap3/templates/listing.tmpl'
_template_uri = 'listing.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def content():
            return render_content(context._locals(__M_locals))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def content():
            return render_content(context)
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        if folders or files:
            __M_writer('<ul class="list-unstyled">\n')
            for name in folders:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('"><i class="glyphicon glyphicon-folder-open"></i> ')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            for name in files:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('.html"><i class="glyphicon glyphicon-file"></i> ')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            __M_writer('</ul>\n')
        if code:
            __M_writer('    ')
            __M_writer(str(code))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context)
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if source_link:
            __M_writer('    <li>\n    <a href="')
            __M_writer(str(source_link))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 5, "23": 3, "77": 5, "78": 6, "79": 6, "80": 7, "81": 8, "82": 9, "83": 10, "84": 10, "85": 10, "86": 10, "87": 10, "88": 12, "89": 13, "90": 13, "91": 13, "92": 13, "29": 0, "94": 15, "95": 17, "96": 18, "97": 18, "98": 18, "104": 22, "93": 13, "47": 2, "48": 3, "114": 22, "115": 23, "116": 24, "53": 20, "118": 25, "119": 25, "120": 25, "58": 28, "126": 120, "117": 25}, "source_encoding": "utf-8", "uri": "listing.tmpl", "filename": "/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/bootstrap3/templates/listing.tmpl"}
__M_END_METADATA
"""
