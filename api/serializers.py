from rest_framework import serializers
from .models import StudentMarks,Students

class StudentAPI(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class MarksAPI(serializers.ModelSerializer):
    class Meta:
        model = StudentMarks
        fields = '__all__'
        extra_kwargs = {'Grade': {'required': False,'default':''}}

    def create(self, validated_data):
        m = validated_data.get('Marks')
        g = validated_data.get('Grade')
        if g == '':
            if m in range(91,101) :
                validated_data['Grade'] = 'A'
            elif m in range(81,91):
                validated_data['Grade'] = 'B'
            elif m in range(71,81):
                validated_data['Grade'] = 'C'
            elif m in range(61,71):
                validated_data['Grade'] = 'D'
            elif m in range(55,61):
                validated_data['Grade'] = 'E'
            elif m < 55:
                validated_data['Grade'] = 'F'
            return super().create(validated_data)