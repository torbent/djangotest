from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class Activity(models.Model):
    """
        Model for logging activities in the system.
        It can be tied to specific user, and can have a target object.
    """
    user = models.ForeignKey(User, null=True, blank=True)

    verb = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # GenericForeignKey to subject
    subject_content_type = models.ForeignKey(ContentType, related_name='subject',
                                             blank=True, null=True)
    subject_object_id = models.CharField(max_length=255, blank=True, null=True)
    subject = generic.GenericForeignKey('subject_content_type',
                                        'subject_object_id')

    # GenericForeignKey to target
    target_content_type = models.ForeignKey(ContentType, related_name='target',
                                            blank=True, null=True)
    target_object_id = models.CharField(max_length=255, blank=True, null=True)
    target = generic.GenericForeignKey('target_content_type',
                                       'target_object_id')

    timestamp = models.DateTimeField(default=datetime.now)

    def timesince(self, now=None):
        """
        Shortcut for the ``django.utils.timesince.timesince`` function of the
        current timestamp.
        """
        from django.utils.timesince import timesince as timesince_
        return timesince_(self.timestamp, now)

    def __unicode__(self):
        return u"[%s] %s [%s] to [%s]" % (self.user or "<no user>", self.verb,
                                          self.subject or "<no subject>",
                                          self.target or "<no target>")

    class Meta:
        verbose_name_plural = 'activities'
