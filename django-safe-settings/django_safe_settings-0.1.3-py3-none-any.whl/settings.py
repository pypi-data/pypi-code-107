from fastutils import cipherutils

try:
    from django.conf import settings
    DJANGO_SAFE_SETTINGS_SECRET_KEY_PREFIX = getattr(settings, "DJANGO_SAFE_SETTINGS_SECRET_KEY_PREFIX", "DJANGO_SAFE_SETTINGS_SECRET_KEY:CFksLnnN2wtsCdcQNRUnyEoqzq01ri8G")
    DJANGO_SAFE_SETTINGS_SECRET_KEY = DJANGO_SAFE_SETTINGS_SECRET_KEY_PREFIX + getattr(settings, "DJANGO_SAFE_SETTINGS_SECRET_KEY", settings.SECRET_KEY)
    DJANGO_SAFE_SETTINGS_CIPHER = getattr(settings, "DJANGO_SAFE_SETTINGS_CIPHER", None)

except:
    settings = globals()
    DJANGO_SAFE_SETTINGS_SECRET_KEY_PREFIX = settings.get("DJANGO_SAFE_SETTINGS_SECRET_KEY_PREFIX", "DJANGO_SAFE_SETTINGS_SECRET_KEY:CFksLnnN2wtsCdcQNRUnyEoqzq01ri8G")
    DJANGO_SAFE_SETTINGS_SECRET_KEY = DJANGO_SAFE_SETTINGS_SECRET_KEY_PREFIX + settings.get("DJANGO_SAFE_SETTINGS_SECRET_KEY", settings["SECRET_KEY"])
    DJANGO_SAFE_SETTINGS_CIPHER = settings.get("DJANGO_SAFE_SETTINGS_CIPHER", None)

if not DJANGO_SAFE_SETTINGS_CIPHER:
    DJANGO_SAFE_SETTINGS_CIPHER = cipherutils.AesCipher(password=DJANGO_SAFE_SETTINGS_SECRET_KEY, result_encoder=cipherutils.HexlifyEncoder(), force_text=True)
