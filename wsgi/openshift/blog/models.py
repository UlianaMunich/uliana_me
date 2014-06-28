from django.db import models
from django.utils.translation import ugettext as _
from markdown import markdown

class Category(models.Model) :
    """Category Model"""
    title = models.CharField(
        verbose_name = _(u'Title'),
        help_text = _(u' '),
        max_length = 255
    )
    slug = models.SlugField(
        verbose_name = _(u'Slug'),
        help_text = _(u'Uri identifier.'),
        max_length = 255,
        unique = True
    )

    class Meta:
        app_label = _(u'blog')
        verbose_name = _(u"Category")
        verbose_name_plural = _(u"Categories")
        ordering = ['title',]

    def __unicode__(self):
        return "%s" % (self.title,)


class Article(models.Model) :
    """Article Model"""
    title = models.CharField(
        verbose_name = _(u'Title'),
        help_text = _(u' '),
        max_length = 255
    )
    slug = models.SlugField(
        verbose_name = _(u'Slug'),
        help_text = _(u'Uri identifier.'),
        max_length = 255,
        unique = True
    )
    content_markdown = models.TextField(
        verbose_name = _(u'Content (Markdown)'),
        help_text = _(u' '),
    )
    content_markup = models.TextField(
        verbose_name = _(u'Content (Markup)'),
        help_text = _(u' '),
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name = _(u'Categories'),
        help_text = _(u' '),
        null = True,
        blank = True
    )
    date_publish = models.DateTimeField(
        verbose_name = _(u'Publish Date'),
        help_text = _(u' ')
    )

    class Meta:
        app_label = _(u'blog')
        verbose_name = _(u"Article")
        verbose_name_plural = _(u"Articles")
        ordering = ['-date_publish']

    def save(self):
        self.content_markup = markdown(self.content_markdown, ['codehilite'])
        super(Article, self).save()

    def __unicode__(self):
        return "%s" % (self.title,)
