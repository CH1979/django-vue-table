from datetime import datetime

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.validators import ValidationError

from api.models import Row
from api.serializers import RowSerializer


ORDER_OPTIONS = {
    "name",
    "-name",
    "quantity",
    "-quantity",
    "distance",
    "-distance"
}
FILTER_OPTIONS = {
    "date__exact",
    "date__gt",
    "date__lt",
    "name__iexact",
    "name__icontains",
    "quantity__exact",
    "quantity__gt",
    "quantity__lt",
    "distance__exact",
    "distance__gt",
    "distance__lt",
}
DATE_PATTERN = "%Y-%m-%d"


def filter_queryset(queryset, object):
    """
    Фильтрация кверисета
    """
    filter_opt = object.request.query_params.get("filter", None)
    filter_value = object.request.query_params.get("filter_value", None)
    filter_field = filter_opt.split("_")[0]

    if (filter_opt not in FILTER_OPTIONS) or (filter_value is None):
        return queryset

    if filter_opt.startswith("quantity") or filter_opt.startswith("distance"):
        try:
            filter_value = float(filter_value)
        except ValueError:
            raise ValidationError(
                { "error": f"Filter value for {filter_field} "
                "must be numerical" },
                code=status.HTTP_400_BAD_REQUEST
            )
    
    if filter_opt.startswith("date"):
        try:
            filter_value = datetime.strptime(filter_value, DATE_PATTERN)
        except ValueError:
            raise ValidationError(
                { "error": f"Filter value for {filter_field} "
                "does not match format '%Y-%m-%d'" },
                code=status.HTTP_400_BAD_REQUEST
            )

    filter_dict = {filter_opt: filter_value}

    return queryset.filter(**filter_dict)


class RowPagination(PageNumberPagination):
    """
    Пагинация
    """
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class RowListView(ListAPIView):
    """
    Представление таблицы
    """
    serializer_class = RowSerializer
    pagination_class = RowPagination

    def get_queryset(self):
        queryset = Row.objects.all()
        queryset = filter_queryset(queryset, self)

        order = self.request.query_params.get("order", None)
        if order in ORDER_OPTIONS:
            queryset = queryset.order_by(order)

        return queryset
