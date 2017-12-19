# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513659691.416761
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_livefyre.tmpl'
_template_uri = 'comments_helper_livefyre.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'comment_form', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <a href="')
        __M_writer(str(link))
        __M_writer('">\n    <span class="livefyre-commentcount" data-lf-site-id="')
        __M_writer(str(comment_system_id))
        __M_writer('" data-lf-article-id="')
        __M_writer(str(identifier))
        __M_writer('">\n    0 Comments\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div id="livefyre-comments"></div>\n<script src="http://zor.livefyre.com/wjs/v3.0/javascripts/livefyre.js"></script>\n<script>\n(function () {\n    var articleId = "')
        __M_writer(str(identifier))
        __M_writer('";\n    fyre.conv.load({}, [{\n        el: \'livefyre-comments\',\n        network: "livefyre.com",\n        siteId: "')
        __M_writer(str(comment_system_id))
        __M_writer('",\n        articleId: articleId,\n        signed: false,\n        collectionMeta: {\n            articleId: articleId,\n            url: fyre.conv.load.makeCollectionUrl(),\n        }\n    }], function() {});\n}());\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n<script src="http://zor.livefyre.com/wjs/v1.0/javascripts/CommentCount.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 31, "34": 23, "35": 24, "36": 24, "37": 25, "38": 25, "39": 25, "40": 25, "55": 11, "46": 2, "61": 31, "16": 0, "51": 2, "52": 7, "21": 21, "22": 28, "23": 33, "71": 65, "54": 11, "29": 23, "53": 7}, "filename": "/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_livefyre.tmpl", "source_encoding": "utf-8", "uri": "comments_helper_livefyre.tmpl"}
__M_END_METADATA
"""
