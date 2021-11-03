from django.template.response import TemplateResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


def percent(part, total):
    if total == 0:
        return None
    p = part * 100 // total
    return '{}%'.format(p)


def get_stats():
    for ct in ContentType.objects.order_by('app_label', 'model'):
        cls = ct.model_class()
        if not cls:
            continue
        count = cls.objects.count()

        fields = []
        for field in cls._meta.get_fields():
            if isinstance(field, GenericForeignKey):
                pass  # FIXME
            else:
                try:
                    kwargs = {field.name: field.get_default()}
                    field_count = cls.objects.exclude(**kwargs).count()
                except (AttributeError, ValueError):
                    kwargs = {field.name: None}
                    field_count = cls.objects.exclude(**kwargs).count()
                fields.append({
                    'name': field.name,
                    'count': field_count,
                    'percent': percent(field_count, count),
                })

        yield {
            'name': cls.__name__,
            'count': count,
            'fields': fields,
        }


@staff_member_required
def stats_view(request):
    context = {'stats': get_stats()}
    return TemplateResponse(request, 'model_stats/stats.html', context)
