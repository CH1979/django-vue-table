from rest_framework.generics import ListAPIView

from api.models import Row
from api.serializers import RowSerializer


class RowListView(ListAPIView):
    """
    Представление таблицы
    """
    queryset = Row.objects.all()
    serializer_class = RowSerializer
