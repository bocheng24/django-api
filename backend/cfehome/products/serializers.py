from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product

        fields = [
            'id',
            'title',
            'description',
            'price',
            'sale_price',
            'applyCoupon'
        ]

        def get_coupon_applied(self, obj):
            # Check if obj is a valid model instance
            if not hasattr(obj, 'id'):
                return None
            
            if not isinstance(obj, Product):
                return None

            return obj.applyCoupon()
