# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1515144873.2647722
_enable_loop = True
_template_filename = 'themes/lanyon/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'late_load_js', 'html_stylesheets', 'html_feedlinks', 'html_translations']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs_link = context.get('abs_link', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        blog_title = context.get('blog_title', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        prevlink = context.get('prevlink', UNDEFINED)
        description = context.get('description', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        title = context.get('title', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n')
            __M_writer('        <script src="/assets/js/moment-with-locales.min.js"></script>\n        <script src="/assets/js/fancydates.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            __M_writer('        <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/poole.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/lanyon.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        __M_writer('    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=PT+Serif:400,400italic,700|PT+Sans:400">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rss_link = context.get('rss_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs_link = context.get('abs_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="translations">\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/lanyon/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 61, "23": 81, "24": 96, "25": 119, "26": 129, "32": 3, "59": 3, "60": 6, "61": 7, "62": 8, "63": 10, "64": 11, "65": 13, "66": 14, "67": 15, "68": 17, "69": 18, "70": 21, "71": 21, "72": 21, "73": 24, "74": 25, "75": 25, "76": 25, "77": 27, "78": 28, "79": 28, "80": 28, "81": 28, "82": 30, "83": 30, "84": 31, "85": 31, "86": 32, "87": 33, "88": 33, "89": 33, "90": 35, "91": 36, "92": 37, "93": 38, "94": 38, "95": 38, "96": 38, "97": 38, "98": 38, "99": 38, "100": 41, "101": 42, "102": 43, "103": 43, "104": 43, "105": 45, "106": 46, "107": 47, "108": 47, "109": 47, "110": 49, "111": 50, "112": 50, "113": 50, "114": 52, "115": 53, "116": 53, "117": 54, "118": 55, "119": 56, "120": 57, "121": 57, "122": 57, "123": 59, "124": 60, "125": 60, "131": 63, "138": 63, "139": 64, "140": 65, "141": 66, "142": 68, "143": 69, "144": 71, "145": 72, "146": 73, "147": 74, "148": 75, "149": 77, "150": 80, "151": 80, "152": 80, "158": 83, "164": 83, "165": 84, "166": 85, "167": 86, "168": 87, "169": 91, "170": 92, "171": 95, "177": 98, "187": 98, "188": 99, "189": 100, "190": 100, "191": 100, "192": 101, "193": 102, "194": 103, "195": 104, "196": 104, "197": 104, "198": 104, "199": 104, "200": 106, "201": 107, "202": 107, "203": 107, "204": 110, "205": 111, "206": 112, "207": 113, "208": 113, "209": 113, "210": 113, "211": 113, "212": 115, "213": 116, "214": 116, "215": 116, "221": 121, "230": 121, "231": 123, "232": 124, "233": 125, "234": 125, "235": 125, "236": 125, "237": 125, "238": 125, "239": 125, "240": 128, "246": 240}}
__M_END_METADATA
"""
