# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1579703944.541547
_enable_loop = True
_template_filename = '/Volumes/macTF/Application/miniconda3/lib/python3.7/site-packages/nikola/data/themes/base/templates/tag.tmpl'
_template_uri = 'tag.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        subcategories = _import_ns.get('subcategories', context.get('subcategories', UNDEFINED))
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(tag, kind, rss_override=False)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def content():
            return render_content(context)
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        subcategories = _import_ns.get('subcategories', context.get('subcategories', UNDEFINED))
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<article class="tagpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('            <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        if subcategories:
            __M_writer('        ')
            __M_writer(str(messages('Subcategories:')))
            __M_writer('\n        <ul>\n')
            for name, link in subcategories:
                __M_writer('            <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('        <div class="metadata">\n            ')
        __M_writer(str(feeds_translations.feed_link(tag, kind=kind)))
        __M_writer('\n        </div>\n        ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n    </header>\n')
        if posts:
            __M_writer('        <ul class="postlist">\n')
            for post in posts:
                __M_writer('            <li><time class="listdate" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time> <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('<a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Volumes/macTF/Application/miniconda3/lib/python3.7/site-packages/nikola/data/themes/base/templates/tag.tmpl", "uri": "tag.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "49": 2, "50": 3, "55": 7, "60": 37, "66": 5, "77": 5, "78": 6, "79": 6, "85": 9, "102": 9, "103": 12, "104": 12, "105": 13, "106": 14, "107": 14, "108": 14, "109": 16, "110": 17, "111": 17, "112": 17, "113": 19, "114": 20, "115": 20, "116": 20, "117": 20, "118": 20, "119": 22, "120": 24, "121": 25, "122": 25, "123": 27, "124": 27, "125": 29, "126": 30, "127": 31, "128": 32, "129": 32, "130": 32, "131": 32, "132": 32, "133": 32, "134": 32, "135": 32, "136": 32, "137": 32, "138": 32, "139": 34, "140": 36, "146": 140}}
__M_END_METADATA
"""
