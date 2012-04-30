from django.views.generic.edit import FormView
from analytics.forms import AnalyticsFilterForm

def events_stat_daily(date_from=None, date_to=None):
    """ Calculates the daily statistics of the Events """


    # ... the major part of the calculation comes here


    return 'data'

class AnalyticsView(FormView):
    """ Django generic FormView to show statistics about Events """
    template_name='analytics/analytics.html'
    form_class = AnalyticsFilterForm

    def get(self, request, *args, **kwargs):
        """ Sets self.form, even on GET request """
        self.form = self.get_form_class()(request.GET)
        return super(AnalyticsView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """ Provides extra context data for the template """
        context = super(AnalyticsView, self).get_context_data(**kwargs)

        data = self.form.is_valid() and \
                        events_stat_daily(**self.form.cleaned_data) or None

        context.update({
            'data': data,
            'form': self.form,
            })
        return context


