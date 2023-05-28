from myapp.models import quiz_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = quiz_model
  fields = ['id', 'question', 'option1', 'option2','option3','option4','rightans']