# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513621936.603058
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_disqus.tmpl'
_template_uri = 'comments_helper_disqus.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link_script', 'comment_link', 'comment_form']


import json 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('       <script>var disqus_shortname="')
            __M_writer(str(comment_system_id))
            __M_writer('";(function(){var a=document.createElement("script");a.async=true;a.src="//"+disqus_shortname+".disqus.com/count.js";(document.getElementsByTagName("head")[0]||document.getElementsByTagName("body")[0]).appendChild(a)}());</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('    <a href="')
            __M_writer(str(link))
            __M_writer('#disqus_thread" data-disqus-identifier="')
            __M_writer(str(identifier))
            __M_writer('">Comments</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <div id="disqus_thread"></div>\n        <script>\n        var disqus_shortname ="')
            __M_writer(str(comment_system_id))
            __M_writer('",\n')
            if url:
                __M_writer('            disqus_url="')
                __M_writer(str(url))
                __M_writer('",\n')
            __M_writer('        disqus_title=')
            __M_writer(str(json.dumps(title)))
            __M_writer(',\n        disqus_identifier="')
            __M_writer(str(identifier))
            __M_writer('",\n        disqus_config = function () {\n')
            if lang == 'es':
                __M_writer('            this.language = "es_ES";\n')
            else:
                __M_writer('            this.language = "')
                __M_writer(str(lang))
                __M_writer('";\n')
            __M_writer('        };\n        (function() {\n            var dsq = document.createElement(\'script\'); dsq.async = true;\n            dsq.src = \'//\' + disqus_shortname + \'.disqus.com/embed.js\';\n            (document.getElementsByTagName(\'head\')[0] || document.getElementsByTagName(\'body\')[0]).appendChild(dsq);\n        })();\n    </script>\n    <noscript>Please enable JavaScript to view the <a href="//disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>\n    <a href="//disqus.com" class="dsq-brlink" rel="nofollow">Comments powered by <span class="logo-disqus">Disqus</span></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "comments_helper_disqus.tmpl", "source_encoding": "utf-8", "line_map": {"16": 3, "18": 0, "23": 2, "24": 3, "25": 31, "26": 37, "27": 44, "33": 40, "38": 40, "39": 41, "40": 42, "41": 42, "42": 42, "48": 33, "53": 33, "54": 34, "55": 35, "56": 35, "57": 35, "58": 35, "59": 35, "65": 5, "71": 5, "72": 6, "73": 7, "74": 9, "75": 9, "76": 10, "77": 11, "78": 11, "79": 11, "80": 13, "81": 13, "82": 13, "83": 14, "84": 14, "85": 16, "86": 17, "87": 18, "88": 19, "89": 19, "90": 19, "91": 21, "97": 91}, "filename": "/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_disqus.tmpl"}
__M_END_METADATA
"""
