# serializers.py
from rest_framework import serializers

class AudioTranscriptionSerializer(serializers.Serializer):
    audio = serializers.FileField()

    def validate_audio(self, audio):
        """
        Validate the audio file format and size here if needed.
        For example, you can check the file extension or limit the file size.
        """
        # Check if the file size is within the allowed limit (10 MB)
        max_file_size = 10 * 1024 * 1024  # 10 MB in bytes
        if audio.size > max_file_size:
            raise serializers.ValidationError('File size exceeds the allowed limit (10 MB).')

        # Add validation logic for file format (if required)
        # For example, you can check the file extension
        allowed_extensions = ['.mp3', '.wav', '.ogg']
        if not audio.name.lower().endswith(tuple(allowed_extensions)):
            raise serializers.ValidationError('Invalid file format. Only .mp3, .wav, or .ogg files are allowed.')

        return audio
