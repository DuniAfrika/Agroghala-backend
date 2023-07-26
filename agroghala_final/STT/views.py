# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from .serializers import *
from agroghala_final.secrets import IBM_WATSON_KEY, IBM_WATSON_URL


class AudioTranscriptionView(APIView):
    def post(self, request, format=None):
        serializer = AudioTranscriptionSerializer(data=request.data)
        if serializer.is_valid():
            audio_file = serializer.validated_data['audio']

            api_key = IBM_WATSON_KEY
            authenticator = IAMAuthenticator(api_key)
            stt = SpeechToTextV1(authenticator=authenticator)
            stt.set_service_url(IBM_WATSON_URL)

            # Call the IBM STT service for transcription
            try:
                with audio_file.open('rb') as audio_data:
                    result = stt.recognize(audio=audio_data, content_type='audio/mp3',
                                           model='en-US_BroadbandModel').get_result()
                    recognized_text = result['results'][0]['alternatives'][0]['transcript']

                    # Process the recognized text as needed (e.g., handle navigation commands)

                    return Response({'transcription': recognized_text}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Error transcribing audio.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
