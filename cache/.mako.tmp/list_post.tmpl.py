# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1577434741.6648462
_enable_loop = True
_template_filename = '/Volumes/macTF/Application/miniconda3/lib/python3.7/site-packages/nikola/data/themes/base/templates/list_post.tmpl'
_template_uri = 'list_post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


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
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
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
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(kind=kind, rss_override=False)))
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
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        def content():
            return render_content(context)
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<article class="listpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n    </header>\n    ')
        __M_writer(str(archive_nav.archive_navigation()))
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n')
        if posts:
            __M_writer('    <ul class="postlist">\n')
            for post in posts:
                __M_writer('        <li><time class="listdate" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time> <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        else:
            __M_writer('    <p>')
            __M_writer(str(messages("No posts found.")))
            __M_writer('</p>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Volumes/macTF/Application/miniconda3/lib/python3.7/site-packages/nikola/data/themes/base/templates/list_post.tmpl", "uri": "list_post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "32": 0, "51": 2, "52": 3, "53": 4, "58": 8, "63": 27, "69": 6, "80": 6, "81": 7, "82": 7, "88": 10, "104": 10, "105": 13, "106": 13, "107": 15, "108": 15, "109": 16, "110": 16, "111": 17, "112": 18, "113": 19, "114": 20, "115": 20, "116": 20, "117": 20, "118": 20, "119": 20, "120": 20, "121": 20, "122": 20, "123": 20, "124": 20, "125": 22, "126": 23, "127": 24, "128": 24, "129": 24, "130": 26, "136": 130}}
__M_END_METADATA
"""
