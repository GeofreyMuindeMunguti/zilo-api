import django_filters
from django.utils import formats
from rest_framework import ISO_8601
from distutils.util import strtobool
from django.utils.encoding import force_str
from django.utils.dateparse import parse_datetime
from django import forms

DATE_INPUT_FORMATS = formats.get_format(
    'DATETIME_INPUT_FORMATS').append(ISO_8601)

BOOLEAN_CHOICES = (
    ('false', 'False'),
    ('true', 'True'),
    ('yes', 'True'),
    ('no', 'False'),
    ('Yes', 'True'),
    ('No', 'False'),
    ('y', 'True'),
    ('n', 'False'),
    ('Y', 'True'),
    ('N', 'False'),
    ('1', 'True'),
    ('0', 'False')
)


class IsoDateTimeField(forms.DateTimeField):
    def strptime(self, value, format):
        value = force_str(value)
        if format == ISO_8601:
            parsed = parse_datetime(value)
            if parsed is None:  # Continue with other formats if doesn't match
                raise ValueError
            return parsed
        return super(IsoDateTimeField, self).strptime(value, format)


class IsoDateTimeFilter(django_filters.DateTimeFilter):
    """ Extend ``DateTimeFilter`` to filter by ISO 8601 formated dates too"""
    field_class = IsoDateTimeField


class CommonFieldsFilterset(django_filters.FilterSet):
    """
        Every model that descends from AbstractBase should have this
    """
    is_active = django_filters.TypedChoiceFilter(
        choices=BOOLEAN_CHOICES, coerce=strtobool)
    is_deleted = django_filters.TypedChoiceFilter(
        choices=BOOLEAN_CHOICES, coerce=strtobool)

    updated_before = IsoDateTimeFilter(
        field_name='updated_at', lookup_expr='lte',
        input_formats=DATE_INPUT_FORMATS)
    created_before = IsoDateTimeFilter(
        field_name='created_at', lookup_expr='lte',
        input_formats=DATE_INPUT_FORMATS)

    updated_after = IsoDateTimeFilter(
        field_name='updated_at', lookup_expr='gte',
        input_formats=DATE_INPUT_FORMATS)
    created_after = IsoDateTimeFilter(
        field_name='created_at', lookup_expr='gte',
        input_formats=DATE_INPUT_FORMATS)

    updated_on = IsoDateTimeFilter(
        field_name='updated_at__date', lookup_expr='exact',
        input_formats=DATE_INPUT_FORMATS)
    created_on = IsoDateTimeFilter(
        field_name='created_at__date', lookup_expr='exact',
        input_formats=DATE_INPUT_FORMATS)