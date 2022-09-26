from rest_framework import serializers
from currency.models import *


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name', 'symbol']

    
class ExchangeRateSerializer(serializers.ModelSerializer):
    exchange_currency1 = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    exchange_currency2 = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ExchangeRate
        fields = ['id', 'exchange_currency1', 'exchange_currency2', 'open_cost', 'high_cost', 'low_cost', 'close_cost', 'adj_close_cost', 'date']

    



# class PostSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.first_name') # ReadOnlyField is a class that returns data unchanged. In this case, it is used to return the field instead of the standard ID.
#     comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'body', 'owner', 'comments']
        

# class CommentSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.first_name')

#     class Meta:
#         model = Comment
#         fields = ['id', 'body', 'owner', 'post']


# class CategorySerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.first_name')
#     posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'owner', 'posts']