
from django import template

register = template.Library()


@register.tag(name='template')
def do_template(parser, token):
    nodes = parser.parse(('endtemplate',))
    parser.delete_first_token()
    return TemplateTagNode(nodes)


class TemplateTagNode(template.Node):
    def __init__(self, nodes):
        self.children = nodes

    def render(self, context):
        tmpl = template.Template(self.children.render(context))
        return tmpl.render(context)
