# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513659692.00893
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/tag.tmpl'
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
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        translations = context.get('translations', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        description = context.get('description', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
        title = context.get('title', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        translations = context.get('translations', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS for ')
                __M_writer(str(kind))
                __M_writer(' ')
                __M_writer(filters.html_escape(str(tag)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')" href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('">\n')
        elif generate_rss:
            __M_writer('        <link rel="alternate" type="application/rss+xml" title="RSS for ')
            __M_writer(str(kind))
            __M_writer(' ')
            __M_writer(filters.html_escape(str(tag)))
            __M_writer('" href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        description = context.get('description', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        title = context.get('title', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        def content():
            return render_content(context)
        date_format = context.get('date_format', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="tagpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('        <p>')
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
        __M_writer('        <div class="metadata">\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('                <p class="feedlink">\n                    <a href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="application/rss+xml">')
                __M_writer(str(messages('RSS feed', language)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')</a>&nbsp;\n                </p>\n')
        elif generate_rss:
            __M_writer('                <p class="feedlink"><a href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('" type="application/rss+xml">')
            __M_writer(str(messages('RSS feed')))
            __M_writer('</a></p>\n')
        __M_writer('        </div>\n    </header>\n')
        if posts:
            __M_writer('    <ul class="postlist">\n')
            for post in posts:
                __M_writer('        <li><time class="listdate" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time><a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('<a></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 19, "129": 20, "130": 21, "131": 21, "132": 21, "133": 23, "134": 24, "135": 24, "136": 24, "137": 26, "138": 27, "139": 27, "140": 27, "141": 27, "142": 27, "143": 29, "144": 31, "145": 32, "146": 33, "147": 34, "148": 35, "149": 35, "150": 35, "151": 35, "152": 35, "153": 35, "154": 35, "27": 0, "156": 38, "157": 39, "158": 39, "159": 39, "160": 39, "161": 39, "162": 41, "155": 35, "164": 44, "163": 43, "166": 46, "167": 46, "168": 46, "169": 46, "170": 46, "171": 46, "172": 46, "173": 46, "174": 46, "175": 46, "176": 46, "177": 48, "50": 2, "55": 13, "184": 178, "60": 51, "66": 4, "80": 4, "81": 5, "82": 5, "83": 6, "84": 7, "85": 8, "86": 8, "87": 8, "88": 8, "89": 8, "90": 8, "91": 8, "92": 8, "93": 8, "94": 10, "95": 11, "96": 11, "97": 11, "98": 11, "99": 11, "100": 11, "101": 11, "165": 45, "178": 50, "107": 16, "126": 16, "127": 19}, "filename": "/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/tag.tmpl", "source_encoding": "utf-8", "uri": "tag.tmpl"}
__M_END_METADATA
"""
