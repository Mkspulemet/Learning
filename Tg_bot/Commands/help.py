from typing import Dict, Union, List


def help(config: Dict[str, Union[Dict[str, Dict[str, Union[str, List]]], str]]) -> str:
    commands: str = 'Список доступных команд:\n'
    for index, command in enumerate(config['intents']['commands']):
        commands += f'{index + 1}. {command}\n'
    return commands