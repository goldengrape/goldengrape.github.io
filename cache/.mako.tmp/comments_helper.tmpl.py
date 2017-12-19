# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513662845.086803
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link_script', 'comment_link', 'comment_form']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('livefyre', context._clean_inheritance_tokens(), templateuri='comments_helper_livefyre.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'livefyre')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

    ns = runtime.TemplateNamespace('googleplus', context._clean_inheritance_tokens(), templateuri='comments_helper_googleplus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'googleplus')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

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


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        disqus = _mako_get_namespace(context, 'disqus')
        isso = _mako_get_namespace(context, 'isso')
        comment_system = context.get('comment_system', UNDEFINED)
        muut = _mako_get_namespace(context, 'muut')
        googleplus = _mako_get_namespace(context, 'googleplus')
        livefyre = _mako_get_namespace(context, 'livefyre')
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
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        disqus = _mako_get_namespace(context, 'disqus')
        isso = _mako_get_namespace(context, 'isso')
        comment_system = context.get('comment_system', UNDEFINED)
        muut = _mako_get_namespace(context, 'muut')
        googleplus = _mako_get_namespace(context, 'googleplus')
        livefyre = _mako_get_namespace(context, 'livefyre')
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


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        disqus = _mako_get_namespace(context, 'disqus')
        isso = _mako_get_namespace(context, 'isso')
        comment_system = context.get('comment_system', UNDEFINED)
        muut = _mako_get_namespace(context, 'muut')
        googleplus = _mako_get_namespace(context, 'googleplus')
        livefyre = _mako_get_namespace(context, 'livefyre')
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


"""
__M_BEGIN_METADATA
{"uri": "comments_helper.tmpl", "source_encoding": "utf-8", "line_map": {"23": 5, "26": 4, "29": 8, "32": 3, "35": 7, "38": 6, "41": 9, "44": 0, "49": 2, "50": 3, "51": 4, "52": 5, "53": 6, "54": 7, "55": 8, "56": 9, "57": 27, "58": 45, "59": 63, "65": 47, "77": 47, "78": 48, "79": 49, "80": 49, "81": 49, "82": 50, "83": 51, "84": 51, "85": 51, "86": 52, "87": 53, "88": 53, "89": 53, "90": 54, "91": 55, "92": 55, "93": 55, "94": 56, "95": 57, "96": 57, "97": 57, "98": 58, "99": 59, "100": 59, "101": 59, "102": 60, "103": 61, "104": 61, "105": 61, "111": 29, "123": 29, "124": 30, "125": 31, "126": 31, "127": 31, "128": 32, "129": 33, "130": 33, "131": 33, "132": 34, "133": 35, "134": 35, "135": 35, "136": 36, "137": 37, "138": 37, "139": 37, "140": 38, "141": 39, "142": 39, "143": 39, "144": 40, "145": 41, "146": 41, "147": 41, "148": 42, "149": 43, "150": 43, "151": 43, "157": 11, "169": 11, "170": 12, "171": 13, "172": 13, "173": 13, "174": 14, "175": 15, "176": 15, "177": 15, "178": 16, "179": 17, "180": 17, "181": 17, "182": 18, "183": 19, "184": 19, "185": 19, "186": 20, "187": 21, "188": 21, "189": 21, "190": 22, "191": 23, "192": 23, "193": 23, "194": 24, "195": 25, "196": 25, "197": 25, "203": 197}, "filename": "/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl"}
__M_END_METADATA
"""
