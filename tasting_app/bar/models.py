# -*- coding: utf-8 -*-

from django.db import models


class Region(models.Model):
    """
        Herkunftsland / Region, z.B. Highlands, Japan, usw.
    """

    name = models.CharField("Land/Region", max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    description = models.CharField("Kommentar", blank=True, max_length=250)

    class Meta:
        verbose_name = 'Land/Region'
        verbose_name_plural = 'Länder/Regionen'
        ordering = ['name']

    def __unicode__(self):
        pass


class Spirittype(models.Model):
    """
        Scotch, Single Malt, Scotch Blend, Bourbon, Irish, Canadian, ...
    """

    name = models.CharField("Typ", max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    description = models.CharField("Kommentar", blank=True, max_length=250)

    class Meta:
        verbose_name = 'Typ'
        verbose_name_plural = 'Typen'
        ordering = ['name']

    def __unicode__(self):
        pass


class Spirit(models.Model):
    """
        Eine ganz bestimmte Spirituose, z.B. Ardbeg Ten, Balvenie Doublewood, etc.
    """

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField("Kommentar", null=True, max_length=250)
    age = models.PositiveSmallIntegerField("Alter", null=True)
    web = models.URLField("Website", max_length=255, null=True)
    spirittype = models.ForeignKey(
        Spirittype, on_delete=models.SET_NULL, verbose_name=u'Typ', null=True
    )
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, verbose_name=u'Land/Region', null=True
    )
    public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'spirit'
        verbose_name_plural = 'spirits'
        ordering = ['name', 'age']

    def __unicode__(sel):
        pass


class Image(models.Model):
    """
        Die Bilder zu den jeweiligen Spirits
    """

    image = models.ImageField("Bild", upload_to="upload/bar")
    name = models.CharField("Bildtitel", max_length=250)
    caption = models.CharField("Bildbeschriftung", max_length=250)
    alt = models.CharField("Alt-Text", max_length=250, null=True)
    hero = models.BooleanField("Hero-Image", default=False)
    spirit = models.ForeignKey(
        Spirit, on_delete=models.SET_NULL, null=True
    )
    ordering = models.PositiveSmallIntegerField("Reihenfolge", null=True, default=0)
    public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __unicode__(self):
        pass
