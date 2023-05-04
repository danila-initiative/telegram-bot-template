import os
import tomli


class Path:
    def __init__(self):
        with open('configs/codegen.toml', 'rb') as f:
            config_dict = tomli.load(f)['path']

        self.configs = config_dict['configs']

        self.templates = config_dict['templates']
        self.tmpl_context = os.path.join(self.templates, 'context.jinja2')

        self.generated = config_dict['generated']
        self.generated_configs = os.path.join(self.generated, 'configs')
        self.generated_context = os.path.join(self.generated, 'context.py')


class CodegenSettings:
    def __init__(self):
        with open('configs/codegen.toml', 'rb') as f:
            config_dict = tomli.load(f)['other']

        self.update_interval = config_dict['update_interval_sec']


path = Path()
cg_settings = CodegenSettings()
