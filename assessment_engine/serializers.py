from decimal import Decimal
from assessment_engine.models import Standard, Subject
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','name','created_on','updated_on','status']

class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = ['id','name','created_on','updated_on','status']

