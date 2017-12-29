# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1514522988.3221781
_enable_loop = True
_template_filename = 'themes/lanyon/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('header', context._clean_inheritance_tokens(), templateuri='base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'header')] = ns

    ns = runtime.TemplateNamespace('footer', context._clean_inheritance_tokens(), templateuri='base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'footer')] = ns

    ns = runtime.TemplateNamespace('annotations', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'annotations')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        footer = _mako_get_namespace(context, 'footer')
        header = _mako_get_namespace(context, 'header')
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        base = _mako_get_namespace(context, 'base')
        lanyon_subtheme = _import_ns.get('lanyon_subtheme', context.get('lanyon_subtheme', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n')
        if lanyon_subtheme:
            __M_writer('<body class="')
            __M_writer(str(lanyon_subtheme))
            __M_writer('">\n')
        else:
            __M_writer('<body>\n')
        __M_writer('    <a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(str(messages("Skip to main content")))
        __M_writer('</a>\n    <!-- Target for toggling the sidebar `.sidebar-checkbox` is for regular\n            styles, `#sidebar-checkbox` for behavior. -->\n    <input type="checkbox" class="sidebar-checkbox" id="sidebar-checkbox">\n\n    <!-- Toggleable sidebar -->\n    <div class="sidebar" id="sidebar">\n        <div class="sidebar-item">\n            <p>Welcome</p>\n        </div>\n        ')
        __M_writer(str(header.html_navigation_links()))
        __M_writer('\n    </div>\n\n    <!-- Wrap is the content to shift when toggling the sidebar. We wrap the\n         content to avoid any CSS collisions with our real content. -->\n    <div class="wrap">\n      <div class="masthead">\n        <div class="container">\n          ')
        __M_writer(str(header.html_site_title()))
        __M_writer('\n        </div>\n      </div>\n\n      <div class="container content" id="content">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        ')
        __M_writer(str(footer.html_footer()))
        __M_writer('\n      </div>\n    </div>\n    <label for="sidebar-checkbox" class="sidebar-toggle"></label>\n    ')
        __M_writer(str(body_end))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n    ')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n    <!-- fancy dates -->\n    <script>\n    moment.locale("')
        __M_writer(str(momentjs_locales[lang]))
        __M_writer('");\n    fancydates(')
        __M_writer(str(date_fanciness))
        __M_writer(', ')
        __M_writer(str(js_date_format))
        __M_writer(');\n    </script>\n    <!-- end fancy dates -->\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/lanyon/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 0, "62": 2, "63": 3, "64": 4, "65": 5, "66": 6, "67": 6, "68": 7, "69": 7, "74": 10, "75": 11, "76": 11, "77": 13, "78": 14, "79": 14, "80": 14, "81": 15, "82": 16, "83": 18, "84": 18, "85": 18, "86": 28, "87": 28, "88": 36, "89": 36, "94": 41, "95": 42, "96": 42, "97": 46, "98": 46, "99": 47, "100": 47, "101": 48, "102": 48, "103": 51, "104": 51, "105": 52, "106": 52, "107": 52, "108": 52, "113": 55, "119": 8, "129": 8, "135": 41, "150": 55, "165": 150}}
__M_END_METADATA
"""
