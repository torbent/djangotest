import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Event(models.Model):
    """ Represents an Event in the system """
    STATUS_ASSIGNED = 0
    STATUS_SENT2SA = 1
    STATUS_HAS_RESPONSES = 2
    STATUS_NO_RESPONSES = 3

    EVENT_STATUS_CHOICES = (
        (STATUS_ASSIGNED, _('Assigned')),                   # green
        (STATUS_SENT2SA, _('Sent to staffing agency')),     # blue
        (STATUS_HAS_RESPONSES, _('Has responses')),         # yellow
        (STATUS_NO_RESPONSES, _('Does not have responses')) # red
        )

    start_date = models.DateField()
    end_date = models.DateField()
    # The reason for the separation of dates and times is legacy compliance --
    # merge them in the future if feasible. (jh, 2011-04-16)
    start_time = models.TimeField()
    end_time = models.TimeField()

    deleted = models.BooleanField(default=False)

    # The event was published this datetime.
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    status = models.PositiveSmallIntegerField(choices=EVENT_STATUS_CHOICES,
                                              default=STATUS_NO_RESPONSES, verbose_name=('Status'))

    class Meta:
        db_table = 'event'
        ordering = ('start_date', 'start_time', 'end_time', 'end_date')

    def __unicode__(self):
        return u"event %s" % self.pk