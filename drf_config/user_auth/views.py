from email.quoprimime import decode
import jwt
from jwt import InvalidTokenError, ExpiredSignatureError

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import UserModel
from .user_serializer import UserSerializer
SECRET_KEY = 'django-insecure-)x*_9&b@&zdjuu#$rwug^8+6g@9pbt_09!0jse)q)ya!rv5!ep'
def is_authenticated(func):
    def wrapper(request):
        auth_header=request.headers.get("Authorization")
        if auth_header is None:
            return Response({
                "message":"Token is missing"
            })
        else:
            token=auth_header.split(" ")[1]
            try:
                decoded_token = jwt.decode(
                    token,
                    SECRET_KEY,
                    algorithms=['HS256']
                )
            except jwt.ExpiredSignatureError as e:
                return ExpiredSignatureError()
            except jwt.InvalidTokenError as e:
                raise InvalidTokenError()

            user = UserModel.objects.filter(email=decoded_token['email'])
            return func(request)
    return wrapper



@api_view(['POST'])
@is_authenticated
def register_user(request):
   if request.method=='POST':
       try:
           serializer = UserSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
           else:
               return Response(serializer.errors)

       except Exception as e:
           return Response(e)



@api_view(['POST'])
def login_user(request):
    check_email=UserModel.objects.filter(email=request.data['email'])
    if not check_email.exists():
        return Response({
            "message":"Invalid Email Given"
        })
    if check_email.first().password==request.data['password']:
        payload={
            "email":check_email.first().email,
            "phone":check_email.first().phone
        }
        token=jwt.encode(
            payload,
            SECRET_KEY,
            algorithm="HS256"
        )
        return Response({
            "message":"User Logged in",
            "token":token
        })
    return Response({
        "message":"Given Password is wrong"
    })
