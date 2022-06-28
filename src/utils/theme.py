from readsettings import ReadSettings
from json_checker import Checker
from ..models import Settings
from .theme_validator import ThemeValidator
import os


class Theme:
    def __init__(self, theme_path=None) -> None:

        self.theme_path = theme_path
        if theme_path == None:
            self.theme_path = Settings.query.filter_by(
                id=1).one_or_none().theme_path

        self.config = {}
        self.variables = {}

        if self.theme_path != None or self.theme_path != '':

            self.config = self.read_theme_config()
            self.variables = self.read_theme_variables()




    def read_theme_config(self) -> dict:

        file = ReadSettings(os.path.join(self.theme_path, 'config.json'))
        config_json = file.json()
        
        checker = Checker(ThemeValidator.config_schema)
        result = checker.validate(config_json)
        
        return result

    def read_theme_variables(self) -> dict:

        file = ReadSettings(os.path.join(self.theme_path, 'variables.json'))
        variables_json = file.json()
        
        checker = Checker(ThemeValidator.variables_schema)
        result = checker.validate(variables_json)
        
        return result
