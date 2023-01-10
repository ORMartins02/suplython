from rest_framework import serializers
from .models import Category
from suppliers.serializers import SupplierSerializer


class CategorySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "supplier"]
        read_only_fields = ["id", "supplier"]

    def create(self, validated_data):
        supplier_list = validated_data.pop("supplier")

        category = Category.objects.create(**validated_data)

        category.supplier.add(supplier_list)

        return category


class DetailCategorySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True, many=True)
    supplier_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "supplier", "supplier_id"]
        read_only_fields = ["id", "supplier"]

    def update(self, instance: Category, validated_data: dict) -> Category:
        supplier = validated_data.pop("supplier_id")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.supplier.add(supplier)

        return instance
