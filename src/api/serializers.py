from rest_framework import serializers
from .models import Account
from datetime import date

class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Account
        fields = ['id', 'fullName', 'email', 'phone', 'document', 'birthDate']

    def validate_document(self, data):
        data = data.replace('.', '').replace('-', '')
        if len(data) == 12:
            raise serializers.ValidationError('CPF INVALIDO')
        return data

    def validate_birthDate(self, data):
        today = date.today()
        years = today.year-data.year
        if years < 18:
            raise serializers.ValidationError('IDADE INVALIDA')
        return data

    def validate_phone(self, data):
        data = data.replace('(', '').replace(')', '').replace('-', '')
        if len (data) == 11:
            raise serializers.ValidationError('TELEFONE INVALIDO')
        return data