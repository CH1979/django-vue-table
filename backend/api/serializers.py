from rest_framework.serializers import ModelSerializer

from api.models import Row

class RowSerializer(ModelSerializer):
    """
    Сериалайзер строк таблицы
    """
    model = Row
    fields = "__all__"
