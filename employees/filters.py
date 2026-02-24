import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    designation=django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_name=django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    id_min=django_filters.CharFilter(method='filter_id_min',label='FROM ID')
    id_max=django_filters.CharFilter(method='filter_id_max',label='TO ID')

    class Meta:
        model=Employee
        fields=['designation', 'emp_name', 'id_min', 'id_max']
        
    def filter_id_min(self, queryset, name, value):
        if name=='id_min':
            return queryset.filter(employee_id__gte=value)
        elif name=='id_max':
            return queryset.filter(employee_id__lte=value)
        return queryset