from json_checker import  Or
class ThemeValidator:
    config_schema = {
        "name": str,
        "description": str,
        "version": str,
        "creators": [
            {
                "name": str,
                "email": str
            }
        ],
        "layout_support": {
            "portrait": bool,
            "landscape": bool
        }
    }
    variables_schema = [
        {
            "text": {
                "key": str,
                "default": str,
                "value": str,
                "requirements": {
                    "nullable": bool,
                    "min_length": int,
                    "max_length": int
                }
            }
        },
        {
            "number": {
                "key": str,
                "default": Or(int, float),
                "value": Or(int, float),
                "requirements": {
                    "nullable": bool,
                    "min_value": Or(int, float),
                    "max_value": Or(int, float)
                }
            }
        },
        {
            "file_img": {
                "key": str,
                "default": str,
                "value": str,
                "requirements": {
                    "nullable": bool,
                    "file_extensions": [str]
                }
            }
        }
    ]
