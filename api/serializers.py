from .models import User, Category, Product, Attribute, Value
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'password', 'email',
                'first_name', 'last_name', 'phone_number', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                 phone_number=validated_data['phone_number'], user_type=validated_data['user_type'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', )


class ValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    attribute_values = serializers.PrimaryKeyRelatedField(many=True, queryset=Value.objects.all())

    def create(self, validated_data):
        categories = validated_data.pop('categories')
        attribute_values = validated_data.pop('attribute_values')
        product = Product.objects.create(**validated_data)

        for cat_id in categories:
            category = Category.objects.get(pk=cat_id)
            product.categories.add(category)
        
        for value_id in attribute_values:
            value = Value.objects.get(pk=value_id)
            product.attribute_values.add(value)

        product.save()
        return product

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'categories', 'image', 'attribute_values')


class AttributeSerializer(serializers.ModelSerializer):
    values = ValuesSerializer(many=True)

    def create(self, validated_data):
        values_data = validated_data.pop('values')
        attribute = Attribute.objects.create(**validated_data)
        for value_data in values_data:
            Value.objects.create(attribute=attribute, **value_data)
        return attribute

    class Meta:
        model = Attribute
        fields = ('id', 'name', 'displayed_name', 'values')
    
