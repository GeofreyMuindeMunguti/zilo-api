from rest_framework_jwt.settings import api_settings

def jwt_response_payload_handler(token, _user=None, _request=None):
    """
    Customize response payload handler.

    This function controls the custom payload after login or token refresh.
    This data is returned through the web API.
    """
    expires_at = timezone.now() + api_settings.JWT_EXPIRATION_DELTA
    return {
        "token": token,
        "expires_at": expires_at.strftime(settings.DATETIME_FORMAT)
    }