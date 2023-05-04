import os
import jinja2
import tomli
import typing as tp
from models import path
from models import cg_settings


class ConfigGenerator:
    def __init__(self):
        self.config_files = os.listdir(path.configs)
        self.context_dict = {}

    def codegen(self):
        for config_file_name in self.config_files:
            if not config_file_name.endswith('.toml'):
                continue

            config_path = os.path.join(path.configs, config_file_name)

            with open(config_path, 'rb') as f:
                config_dict = tomli.load(f)

            template = get_template(config_dict['config_type'])
            if template is None:
                continue

            config_name = config_file_name.split('.')[0]
            class_name = config_name.capitalize()

            rendered = template.render(
                config_name=class_name,
                config_dict=config_dict['config'],
                config_path='/app/' + config_path,
                update_interval=cg_settings.update_interval,
            )

            gen_file_path = get_gen_file_path(config_name)
            with open(gen_file_path, 'w') as f:
                f.write(rendered)

            self.context_dict[config_name] = class_name

    def get_context_dict(self) -> dict:
        return self.context_dict


def get_template(config_type: str) -> tp.Optional[jinja2.Template]:
    if config_type in ['skip']:
        return None

    with open(f'{path.templates}{config_type}.jinja2', 'r') as f:
        template = f.read()

    template = jinja2.Template(template)
    return template


def get_gen_file_path(config_name: str) -> str:
    return os.path.join(path.generated_configs, f'{config_name}.py')
