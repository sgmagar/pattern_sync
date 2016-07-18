from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from django.db import models

class Pattern(models.Model):
	pattern = models.CharField(max_length=10)

	class Meta:
		verbose_name = _('Pattern')
		verbose_name_plural = _('Patterns')

	def __unicode__(self):
		return u'Pattern: %s' % self.pattern


class Code(models.Model):
	code = models.CharField(max_length=10)

	class Meta:
		verbose_name = _('Code')
		verbose_name_plural = _('Codes')

	def __unicode__(self):
		return u'Code: %s' % self.code