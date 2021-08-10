from rest_framework import serializers


class OrderItemSerializer(serializers.ModelSerializer):
    pass
    # class Meta:
    #     model = OrderItems
    #     fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    pass
    #
    # class Meta:
    #     model = OrderShippings
    #     fields = "__all__"
#
# class OrderShippingListSerializer(OrderShippingSerializer):
#
#
#     class Meta:
#         model = OrderShippings
#         fields = (
#             "id",
#             "items",
#             "status",
#             "comment",
#             "comment_extra_list",
#             "delivery_at",
#             "delivered_at",
#             "finish_at",
#             "finished_at",
#             "created_at",
#             "cancel_items",
#             "updated_at",
#         )