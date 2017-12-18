# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513621936.617112
_enable_loop = True
_template_filename = '/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_intensedebate.tmpl'
_template_uri = 'comments_helper_intensedebate.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link_script', 'comment_link', 'comment_form']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<a href="{link}" onclick="this.href=\'')
        __M_writer(str(link))
        __M_writer('\'; this.target=\'_self\';"><span class=\'IDCommentsReplace\' style=\'display:none\'>')
        __M_writer(str(identifier))
        __M_writer("</span>\n<script>\nvar idcomments_acct = '")
        __M_writer(str(comment_system_id))
        __M_writer('\';\nvar idcomments_post_id = "')
        __M_writer(str(identifier))
        __M_writer('";\nvar idcomments_post_url = "')
        __M_writer(str(link))
        __M_writer('";\n</script>\n<script src="http://www.intensedebate.com/js/genericLinkWrapperV2.js"></script>\n</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\n<script>\nvar idcomments_acct = '")
        __M_writer(str(comment_system_id))
        __M_writer('\';\nvar idcomments_post_id = "')
        __M_writer(str(identifier))
        __M_writer('";\nvar idcomments_post_url = "')
        __M_writer(str(url))
        __M_writer('";\n</script>\n<span id="IDCommentsPostTitle" style="display:none"></span>\n<script src=\'http://www.intensedebate.com/js/genericCommentWrapperV2.js\'></script>\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "comments_helper_intensedebate.tmpl", "source_encoding": "utf-8", "line_map": {"65": 2, "66": 4, "67": 4, "68": 5, "69": 5, "70": 6, "71": 6, "77": 71, "16": 0, "21": 11, "22": 22, "23": 25, "29": 24, "33": 24, "39": 13, "44": 13, "45": 14, "46": 14, "47": 14, "48": 14, "49": 16, "50": 16, "51": 17, "52": 17, "53": 18, "54": 18, "60": 2}, "filename": "/Users/goldengrape/anaconda3/envs/blog/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_intensedebate.tmpl"}
__M_END_METADATA
"""
