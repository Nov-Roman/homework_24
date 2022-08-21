from dataclasses import dataclass
from typing import Union

import marshmallow_dataclass
from marshmallow import ValidationError

from resources.constants import COMMANDS


@dataclass
class Commands:
    file_name: str
    cmd1: str
    value1: Union[str, int]
    cmd2: str
    value2: Union[str, int]

    def __post_init__(self):
        """Проверяет поля и объединять имена команд с '_'"""
        if self.cmd1 not in COMMANDS:
            raise ValidationError(f'Команда передана как cmd1 ({self.cmd1}) недопустимая команда. '
                                  f'Только {", ".join(COMMANDS)} допустимый')
        if self.cmd2 not in COMMANDS:
            raise ValidationError(f'Команда передана как cmd2 ({self.cmd2}) недопустимая команда. '
                                  f'Только {", ".join(COMMANDS)} допустимый')

        self.cmd1 = self.cmd1 + '_'
        self.cmd2 = self.cmd2 + '_'


CommandsSchema = marshmallow_dataclass.class_schema(Commands)
