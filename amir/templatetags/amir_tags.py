from django import template



register = template.Library()


class SetVarNode(template.Node):

	def __init__(self, var_name, var_value):
		self.var_name = var_name
		self.var_value = var_value

	def render(self, context):
		try:
			value = template.Variable(self.var_value).resolve(context)
		except template.VariableDoesNotExist:
			value = ""
		context[self.var_name] = value

		return u""


@register.tag(name='set')
def set_var(parser, token):
	"""
    {% set some_var = '123' %}
    """
	parts = token.split_contents()
	if len(parts) < 4:
		raise template.TemplateSyntaxError("'set' tag must be of the form: {% set <var_name> = <var_value> %}")

	return SetVarNode(parts[1], parts[3])


@register.filter(name='amir')
def lower(value, ami=None):  # Only one argument.
	"""Converts a string into all lowercase"""

	ami = value + 12
	return ami


@register.filter(name='tostr')
def tostr(value, stri=None):
	stri = str(value)
	return stri


@register.filter(name='equal')
def equal(var,args):
	if args is None:
		return False
	else:
		ar = {}


		args_list = [arg.strip() for arg in args.split(',')]
		for arg in args_list:
			ar [arg] = arg

		if ar['1']>ar['2']:

			return True
		else:
			return False