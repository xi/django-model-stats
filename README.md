# django-model-stats

Display how often models and model fields are used in the database.

## Installation

1.  Add `'model_stats'` to your `INSTALLED_APPS`
2.  Add `path('admin/stats/', include('model_stats.urls'))` to your
    `urlpatterns`. Make sure it’s included *before* the `'admin/'` entry, so
    that requests to `/admin/stats/` don’t get handled by the latter entry.
