# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513659691.483757
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/bootstrap3/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
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
        post = context.get('post', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

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


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        parent = context.get('parent', UNDEFINED)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        if post.description():
            __M_writer('    <meta name="description" itemprop="description" content="')
            __M_writer(filters.html_escape(str(post.description())))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(filters.html_escape(str(post.author())))
        __M_writer('">\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\n')
        __M_writer('    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context)
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' h-entry hentry postpage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    ')
        __M_writer(str(pheader.html_post_header()))
        __M_writer('\n    <div class="e-content entry-content" itemprop="articleBody text">\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n    <aside class="postpromonav">\n    <nav>\n    ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n    </nav>\n    </aside>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <section class="comments hidden-print">\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n        </section>\n')
        __M_writer('    ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n</article>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('    <li>\n    <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"139": 30, "140": 31, "141": 31, "142": 32, "143": 32, "144": 34, "145": 34, "146": 38, "147": 38, "148": 39, "149": 39, "150": 42, "23": 3, "152": 44, "153": 44, "26": 4, "155": 45, "156": 48, "29": 2, "158": 48, "159": 50, "160": 50, "35": 0, "166": 53, "154": 45, "157": 48, "176": 54, "177": 55, "178": 56, "179": 56, "180": 56, "181": 56, "54": 2, "55": 3, "56": 4, "57": 5, "187": 181, "151": 43, "62": 28, "175": 53, "67": 51, "72": 59, "78": 7, "87": 7, "88": 8, "89": 8, "90": 9, "91": 10, "92": 10, "93": 10, "94": 12, "95": 13, "96": 13, "97": 13, "98": 15, "99": 15, "100": 15, "101": 16, "102": 17, "103": 17, "104": 17, "105": 17, "106": 17, "107": 19, "108": 20, "109": 20, "110": 20, "111": 20, "112": 20, "113": 22, "114": 23, "115": 25, "116": 25, "117": 25, "118": 26, "119": 26, "120": 27, "121": 27, "127": 30}, "filename": "/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/bootstrap3/templates/post.tmpl", "source_encoding": "utf-8", "uri": "post.tmpl"}
__M_END_METADATA
"""
