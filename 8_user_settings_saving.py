def create_user_settings():
    default_settings = {
        'theme': 'light',
        'language': 'en',
        'notifications': True
    }

    def user_settings(action, key=None, value=None):
        settings = default_settings
        match action:
            case 'get':
                return settings.get(key, f"Setting '{key}' not found.")

            case 'set':
                if key in settings:
                    old_value = settings[key]
                    settings[key] = value
                    return f"Setting '{key}' changed from '{old_value}' to '{value}'."

            case 'all':
                return settings

            case _:
                return f"Unknown action '{action}'."

    return user_settings


new_user_settings = create_user_settings()
print("Output result of all user settings (default in this case):", new_user_settings('all'))
print("Output result of the user's color theme:", new_user_settings('get', 'theme'))
print("Output result of changing the user's color theme:", new_user_settings('set', 'theme', 'dark'))
print("Output result of all user settings:", new_user_settings('all'))
