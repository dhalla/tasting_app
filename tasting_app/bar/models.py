# -*- coding: utf-8 -*-

from django.db import models


class Region(models.Model):
    """
        Herkunftsland / Region, z.B. Highlands, Japan, usw.
    """

    name = models.CharField("Region", max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    description = models.TextField("Kommentar", blank=True)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regionen'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Spirittype(models.Model):
    """
        Scotch, Single Malt, Scotch Blend, Bourbon, Irish, Canadian, usw.
    """

    name = models.CharField("Typ", max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    description = models.TextField("Kommentar", blank=True)

    class Meta:
        verbose_name = 'Typ'
        verbose_name_plural = 'Typen'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Distillery(models.Model):
    """
        Destillen
    """

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    description = models.TextField("Kommentar", blank=True)
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, verbose_name=u'Region', null=True
    )
    founded = models.PositiveSmallIntegerField("Gegründet", blank=True, null=True)
    capacity = models.IntegerField("Kapazität", blank=True, null=True,
                                   help_text="in metrischen Litern")
    location = models.CharField("Ort", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Destille'
        verbose_name_plural = 'Destillen'
        ordering = ['name', 'region']

    def __unicode__(self):
        return self.name


class Spirit(models.Model):
    """
        Eine ganz bestimmte Spirituose, z.B. Ardbeg Ten, Balvenie Doublewood, etc.
    """

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField("Kommentar", blank=True)
    age = models.PositiveSmallIntegerField("Alter", blank=True, null=True, help_text='In Jahren')
    web = models.URLField("Website", max_length=255, blank=True)
    volume = models.PositiveSmallIntegerField("Vol. %", help_text="Alkoholgehalt")
    distillery = models.ForeignKey(
        Distillery, on_delete=models.SET_NULL, verbose_name=u'Destille', null=True
    )
    spirittype = models.ForeignKey(
        Spirittype, on_delete=models.SET_NULL, verbose_name=u'Typ', null=True
    )
    public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Whisky'
        verbose_name_plural = 'Whiskies'
        ordering = ['name', 'age']

    def __unicode__(self):
        if self.age:
            age = ' (' + str(self.age) + ' Jahre)'
        else:
            age = ''
        return self.distillery.name + ' ' + self.name + age


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
