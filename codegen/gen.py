import os
import shutil

import configs
import context
from models import path


def main():
    shutil.rmtree(path.generated, ignore_errors=True)

    folders = [path.generated, path.generated_configs]
    for folder in folders:
        os.makedirs(folder, exist_ok=False)
        with open(os.path.join(folder, '__init__.py'), 'w') as f:
            f.write('')

    cfg_generator = configs.ConfigGenerator()
    cfg_generator.codegen()

    context.codegen(cfg_generator.get_context_dict())

    os.makedirs('../data', exist_ok=True)


if __name__ == '__main__':
    main()
