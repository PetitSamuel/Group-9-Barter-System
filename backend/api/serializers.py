from rest_framework import serializers
from query.models import User
import json
import re

sorted_days_of_week = ['monday', 'tuesday', 'wednesday',
                       'thursday', 'friday', 'saturday', 'sunday']


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=128)
    phone_number = serializers.CharField(required=True, max_length=128)
    latitude = serializers.FloatField(required=False, default=None)
    longitude = serializers.FloatField(required=False, default=None)
    bio = serializers.CharField(required=False, max_length=256, default='')
    username = serializers.CharField(required=True, max_length=128)
    password = serializers.CharField(required=True, max_length=128)

    def validate(self, data):
        """
        Check that the model is valid.
        """
        if not data['username']:
            raise serializers.ValidationError("username cannot be empty")

        data['username'] = re.sub(
            r"\s", "", data['username']).lower()

        if not data['password']:
            raise serializers.ValidationError("password cannot be empty")

        if not data['name']:
            raise serializers.ValidationError("name cannot be empty")
        if not data['phone_number']:
            raise serializers.ValidationError("phone_number cannot be empty")

        return data


class BusinessSerializer(serializers.Serializer):
    business_name = serializers.CharField(required=True, max_length=128)
    working_days = serializers.CharField(required=True, max_length=128)
    work_tags = serializers.CharField(required=True, max_length=256)
    description = serializers.CharField(required=True, max_length=256)
    contact = serializers.CharField(required=True, max_length=128)
    start_time = serializers.IntegerField(required=True, min_value=0)
    end_time = serializers.IntegerField(required=True, min_value=0)

    def validate(self, data):
        """
        Check that the model is valid.
        """
        if not data['business_name']:
            raise serializers.ValidationError("business_name cannot be empty")
        if not data['description']:
            raise serializers.ValidationError("description cannot be empty")
        if not data['contact']:
            raise serializers.ValidationError("contact cannot be empty")
        if type(data['start_time']) != int:
            raise serializers.ValidationError("start_time cannot be empty")
        if type(data['end_time']) != int:
            raise serializers.ValidationError("end_time cannot be empty")
        if not data['working_days']:
            raise serializers.ValidationError("working_days cannot be empty")
        if not data['work_tags']:
            raise serializers.ValidationError("work_tags cannot be empty")
        """
        Check that the start date and the end date are valid (<24).
        """
        if data['start_time'] > 24:
            raise serializers.ValidationError(
                "start_time must be between 0 and 24")
        if data['end_time'] > 24:
            raise serializers.ValidationError(
                "end_time must be between 0 and 24")
        """
        Check that the start date is before the end date.
        """
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError(
                "start_time must be before end_time")

        """
        Check that the working_days is a csv of days.
        """
        working_days = re.sub(
            r"\s", "", data['working_days']).lower().split(",")
        working_days = set(working_days)  # keep unique days
        for day in working_days:
            if day not in sorted_days_of_week:
                raise serializers.ValidationError(
                    "Day: %s must be a valid day. Field should be a comma separated list of days" % (day))
        if len(working_days) > 7:
            raise serializers.ValidationError(
                "working_days cannot be more than 7 days")
        data['working_days'] = ','.join(
            sorted(working_days, key=sorted_days_of_week.index))

        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError(
                "start_time must be before end_time")
        return data


class ReviewSerializer(serializers.Serializer):
    business_id = serializers.IntegerField(required=True)
    review_text = serializers.CharField(required=True, max_length=256)
    stars = serializers.IntegerField(required=True, max_value=5, min_value=0)

    def validate(self, data):
        """
        Check that the model is valid.
        """
        if not data['business_id']:
            raise serializers.ValidationError("business_id cannot be empty")
        if not data['review_text']:
            raise serializers.ValidationError("review_text cannot be empty")
        if type(data['stars']) != int:
            raise serializers.ValidationError("stars cannot be empty")
        """
        Check that the start date and the end date are valid (<24).
        """
        if data['stars'] > 5 or data['stars'] < 0:
            raise serializers.ValidationError(
                "start_time must be between 0 and 5")
        return data
