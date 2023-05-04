import jinja2
from codegen.models import path


def codegen(context_data: dict):
    template = jinja2.Template(open(path.tmpl_context, 'r').read())

    rendered = template.render(context_dict=context_data)

    with open(path.generated_context, 'w') as f:
        f.write(rendered)
