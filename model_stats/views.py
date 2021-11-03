from django.template.response import TemplateResponse


def stats_view(request):
    context = {}
    return TemplateResponse(request, 'model_stats/stats.html', context)
