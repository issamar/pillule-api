from rest_framework import serializers
from .models import SalesDetails, PilsDetail
from datetime import datetime
 
class PilsdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PilsDetail
        fields = '__all__'


class SalesDetailsSerializer(serializers.ModelSerializer):
    pils_name = serializers.SlugRelatedField(
        slug_field="name", queryset=PilsDetail.objects.all())
    remain_time = serializers.SerializerMethodField()
    
    
    def get_remain_time(self, obj):
        toDay = datetime.now().date()
        saling_date = obj.sale_date
        timestamp = toDay - saling_date
        cond = obj.pils_name.cond
        remain_time = int(cond) - int(timestamp.days)
        return remain_time

    class Meta:
        model = SalesDetails
        fields = ("id", "patient_name", "pils_name", "remain_time","sale_date")
