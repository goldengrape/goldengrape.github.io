# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513620227.82031
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link_script', 'comment_link']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('livefyre', context._clean_inheritance_tokens(), templateuri='comments_helper_livefyre.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'livefyre')] = ns

    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('googleplus', context._clean_inheritance_tokens(), templateuri='comments_helper_googleplus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'googleplus')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        livefyre = _mako_get_namespace(context, 'livefyre')
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        muut = _mako_get_namespace(context, 'muut')
        isso = _mako_get_namespace(context, 'isso')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_form(url, title, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        livefyre = _mako_get_namespace(context, 'livefyre')
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        muut = _mako_get_namespace(context, 'muut')
        isso = _mako_get_namespace(context, 'isso')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link_script()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        livefyre = _mako_get_namespace(context, 'livefyre')
        disqus = _mako_get_namespace(context, 'disqus')
        comment_system = context.get('comment_system', UNDEFINED)
        muut = _mako_get_namespace(context, 'muut')
        isso = _mako_get_namespace(context, 'isso')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link(link, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl", "uri": "comments_helper.tmpl", "line_map": {"23": 9, "26": 4, "29": 5, "32": 3, "35": 6, "38": 7, "41": 8, "44": 0, "49": 2, "50": 3, "51": 4, "52": 5, "53": 6, "54": 7, "55": 8, "56": 9, "57": 27, "58": 45, "59": 63, "65": 11, "77": 11, "78": 12, "79": 13, "80": 13, "81": 13, "82": 14, "83": 15, "84": 15, "85": 15, "86": 16, "87": 17, "88": 17, "89": 17, "90": 18, "91": 19, "92": 19, "93": 19, "94": 20, "95": 21, "96": 21, "97": 21, "98": 22, "99": 23, "100": 23, "101": 23, "102": 24, "103": 25, "104": 25, "105": 25, "111": 47, "123": 47, "124": 48, "125": 49, "126": 49, "127": 49, "128": 50, "129": 51, "130": 51, "131": 51, "132": 52, "133": 53, "134": 53, "135": 53, "136": 54, "137": 55, "138": 55, "139": 55, "140": 56, "141": 57, "142": 57, "143": 57, "144": 58, "145": 59, "146": 59, "147": 59, "148": 60, "149": 61, "150": 61, "151": 61, "157": 29, "169": 29, "170": 30, "171": 31, "172": 31, "173": 31, "174": 32, "175": 33, "176": 33, "177": 33, "178": 34, "179": 35, "180": 35, "181": 35, "182": 36, "183": 37, "184": 37, "185": 37, "186": 38, "187": 39, "188": 39, "189": 39, "190": 40, "191": 41, "192": 41, "193": 41, "194": 42, "195": 43, "196": 43, "197": 43, "203": 197}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
