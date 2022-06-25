from readsettings import ReadSettings
import os

class Theme:
    def __init__(self, theme_path ) -> None:
        self.theme_path = theme_path
        self.config = self.read_theme_config()
    
    def read_theme_config(self) -> dict:
        # Todo 
        # Validate json config file with json_checker
        file = ReadSettings(os.path.join(self.theme_path, 'config.json'))
        return file.json()