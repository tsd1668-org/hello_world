import datetime
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    dob = serializers.DateField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.save()
        return instance

    def to_representation(self, obj):
        days_difference = self._calculate_days_difference_from_today(obj.dob)
        greeting_msg = self._get_greeting_message(days_difference, obj.name)

        return {
            'data': greeting_msg
        }

    def _calculate_days_difference_from_today(self, dob):
        today_year = datetime.date.today().year
        today_month = datetime.date.today().month
        today_day = datetime.date.today().day
        today = "{0}-{1}-{2}".format(today_year, today_month, today_day)
        today = datetime.datetime.strptime(today, '%Y-%m-%d').date()

        dob_month = dob.month
        dob_day = dob.day
        dob = "{0}-{1}-{2}".format(today_year, dob_month, dob_day)
        dob = datetime.datetime.strptime(dob, '%Y-%m-%d').date()

        days_difference = (today - dob).days

        return days_difference

    def _get_greeting_message(self, days_difference, name):
        if days_difference == -5:
            message = "Hello {0}! Your birthday is in 5 days".format(name)
        elif days_difference == 0:
            message = "Happy birthday, {0}!".format(name)
        else:
            message = "Hello {0}!".format(name)

        return message