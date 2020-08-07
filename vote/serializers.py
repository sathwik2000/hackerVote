from rest_framework import serializers
from .models import Hacker


class HackerSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=200)
    no_challenges = serializers.IntegerField()
    code = serializers.IntegerField()
    except_level = serializers.IntegerField()
    Data_structures = serializers.IntegerField()
    Algo = serializers.IntegerField()
    cpp = serializers.IntegerField()
    java = serializers.IntegerField()
    python = serializers.IntegerField()
    votes = serializers.IntegerField()
    # timezone = forms.ChoiceField(choices=[(x, x
    def create(self,validated_data):
        validated_data['votes'] = 0
        return Hacker.objects.create(**validated_data)
    def update(self, instance, validated_data):
        print(validated_data.get('no_challenges', instance.no_challenges))
        instance.Name = validated_data.get('Name', instance.Name)
        instance.code = validated_data.get('code', instance.code)
        instance.no_challenges = validated_data.get('no_challenges', instance.no_challenges)
        instance.except_level = validated_data.get('except_level', instance.except_level)
        instance.Data_structures = validated_data.get('Data_structures', instance.Data_structures)
        instance.cpp = validated_data.get('cpp', instance.cpp)
        instance.java = validated_data.get('java', instance.java)
        instance.python = validated_data.get('python', instance.python)
        instance.votes = validated_data.get('votes', instance.votes)
        instance.Algo = validated_data.get('Algo', instance.Algo)
        return instance