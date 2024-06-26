from rest_framework import serializers
from .models import *


class EmployerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        employer = Employer()
        employer.name = validated_data.get('name')
        employer.save()
        return validated_data

    def update(self, instance: Employer, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        role = Role()
        role.employer = validated_data.get('employer')
        role.description = validated_data.get('description')
        role.save()
        return validated_data

    def update(self, instance: Role, validated_data):
        instance.employer = validated_data.get('employer')
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        employee = Employee()
        employee.employer = validated_data.get('employer')
        employee.first_name = validated_data.get('first_name')
        employee.last_name = validated_data.get('last_name')
        employee.role = validated_data.get('role')
        employee.salary = validated_data.get('salary')
        employee.save()
        return validated_data

    def update(self, instance: Employee, validated_data):
        instance.employer = validated_data.get('employer')
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.role = validated_data.get('role')
        instance.salary = validated_data.get('salary', instance.salary)
        instance.save()
        return instance
