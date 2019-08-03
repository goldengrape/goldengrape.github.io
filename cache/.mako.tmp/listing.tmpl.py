# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1564814309.696875
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/listing.tmpl'
_template_uri = 'listing.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='ui_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        ui = _mako_get_namespace(context, 'ui')
        files = context.get('files', UNDEFINED)
        source_link = context.get('source_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        code = context.get('code', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        ui = _mako_get_namespace(context, 'ui')
        files = context.get('files', UNDEFINED)
        source_link = context.get('source_link', UNDEFINED)
        def content():
            return render_content(context)
        code = context.get('code', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(ui.breadcrumbs(crumbs)))
        __M_writer('\n')
        if folders or files:
            __M_writer('<ul>\n')
            for name in folders:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('" class="listing-folder">')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            for name in files:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('.html" class="listing-file">')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            __M_writer('</ul>\n')
        if code:
            __M_writer('    <h1>')
            __M_writer(str(title))
            __M_writer('\n')
            if source_link:
                __M_writer('            <small><a href="')
                __M_writer(str(source_link))
                __M_writer('">(')
                __M_writer(str(messages("Source")))
                __M_writer(')</a></small>\n')
            __M_writer('        </h1>\n    ')
            __M_writer(str(code))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/goldengrape/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/listing.tmpl", "uri": "listing.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "44": 2, "45": 3, "50": 24, "56": 4, "70": 4, "71": 5, "72": 5, "73": 6, "74": 7, "75": 8, "76": 9, "77": 9, "78": 9, "79": 9, "80": 9, "81": 11, "82": 12, "83": 12, "84": 12, "85": 12, "86": 12, "87": 14, "88": 16, "89": 17, "90": 17, "91": 17, "92": 18, "93": 19, "94": 19, "95": 19, "96": 19, "97": 19, "98": 21, "99": 22, "100": 22, "106": 100}}
__M_END_METADATA
"""
