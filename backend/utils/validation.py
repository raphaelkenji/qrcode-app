import validators

def validate_url(url: str) -> str:
    if not validators.url(url):
        return False
    return True