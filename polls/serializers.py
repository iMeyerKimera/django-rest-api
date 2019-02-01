from rest_framework import serializers
from .models import Poll, Choice, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    # We can utilize a number of methods in this class

    # is_valid(self, ..) method which can tell if the data is sufficient and valid to create/update a model instance.

    # save(self, ..) method, which khows how to create or update an instance.

    # create(self, validated_data, ..) method which knows how to create an instance. This method can be overriden to customize the create behaviour.

    # update(self, instance, validated_data, ..) method which knows how to update an instance. This method can be overriden to customize the update behaviour

    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'