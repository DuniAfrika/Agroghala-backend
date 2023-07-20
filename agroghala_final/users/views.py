from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import generics
from .models import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model, login
from django.views.decorators.csrf import csrf_exempt

NewUser=get_user_model()

class NewUserView(generics.ListCreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer
    def post(self, request):
        serializer = NewUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Customize token claims, if desired
        # token['custom_claim'] = 'custom_value'

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class TwitterLoginView(APIView):
    @csrf_exempt
    def post(self, request):
        access_token = request.data.get('access_token')
        access_secret = request.data.get('access_secret')

        # Implement your verification logic
        def authenticate_with_twitter_api(self, access_token, access_secret):
            # Step 1: Authenticate with the Twitter API using the access token and secret
            auth_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json',
            }
            response = requests.get(auth_url, headers=headers)

            if response.status_code != 200:
                # Authentication failed, handle the error
                raise Exception('Twitter authentication failed.')

            # Step 2: Retrieve user details such as username and email from the Twitter API response
            def authenticate_with_twitter_api(self, access_token, access_secret):
                # ...existing code...

                # Step 2: Retrieve user details such as first name, last name, email, phone number, and address from the Twitter API response
                user_data = response.json()

                serializer = TwitterUserSerializer(data=user_data)
                serializer.is_valid(raise_exception=True)
                validated_data = serializer.validated_data

                first_name = validated_data.get('first_name')
                last_name = validated_data.get('last_name')
                email = validated_data.get('email')
                phone_number = validated_data.get('phone_number')
                address = validated_data.get('address')

                return first_name, last_name, email, phone_number, address

        # Example user creation/sign-in logic:
        try:
            # Check if the user already exists based on the Twitter user ID or email
            user = NewUser.objects.get(twitter_id=twitter_user_id)  # Replace 'twitter_user_id' with the actual Twitter user ID field in your User model
        except NewUser.DoesNotExist:
            # User does not exist, create a new user
            user = NewUser.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                            phone_number=phone_number, address=address)  # Replace 'username' and 'email' with the retrieved values

            # Optional: Save the Twitter user ID in your User model
            user.twitter_id = twitter_user_id
            user.save()

        # Sign in the user
        login(request, user)

        return Response({'message': 'Logged in successfully.'})