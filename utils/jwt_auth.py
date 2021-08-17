from users.serializers import UserSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    user_details = UserSerializer(user, context={'request': request}).data
    del user_details["password"]
    del user_details["last_login"]
    
    return {
        'token': token,
        'user':  user_details
    }