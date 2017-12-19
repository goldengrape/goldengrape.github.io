# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513659691.829276
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        date_format = context.get('date_format', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
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
        def extra_head():
            return render_extra_head(context)
        index_file = context.get('index_file', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        index_teasers = context.get('index_teasers', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        date_format = context.get('date_format', UNDEFINED)
        def content():
            return render_content(context)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('            </span></p>\n            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 23, "129": 23, "130": 24, "131": 25, "132": 25, "133": 25, "134": 27, "135": 28, "136": 28, "137": 28, "138": 28, "139": 28, "140": 28, "141": 28, "142": 28, "143": 29, "144": 30, "145": 30, "146": 30, "147": 32, "148": 34, "149": 35, "150": 36, "23": 3, "152": 37, "153": 38, "26": 2, "155": 39, "156": 41, "154": 39, "158": 45, "159": 45, "32": 0, "161": 46, "162": 47, "163": 47, "169": 14, "157": 44, "180": 169, "54": 2, "55": 3, "56": 4, "151": 36, "61": 11, "160": 46, "66": 48, "72": 6, "82": 6, "83": 7, "84": 7, "85": 8, "86": 9, "87": 9, "88": 9, "94": 13, "110": 13, "115": 14, "116": 16, "117": 17, "118": 17, "119": 17, "120": 19, "121": 19, "122": 19, "123": 19, "124": 22, "125": 23, "126": 23, "127": 23}, "filename": "/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/index.tmpl", "source_encoding": "utf-8", "uri": "index.tmpl"}
__M_END_METADATA
"""
