from django.db import models
from django.conf import settings


class Contact(models.Model):
    telegram_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=25)
    address = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()
    email_address = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Contacts"

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class MainPageSettings(models.Model):
    logo = models.FileField(
        upload_to='uploads/main_page_settings/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def logo_url(self):
        if self.logo:
            return "%s%s" % (settings.HOST, self.logo.url)

    def __str__(self):
        return "Main Page Settings"

    class Meta:
        db_table = 'settings'
        verbose_name = 'Main Page Settings'
        verbose_name_plural = 'Main Page Settings'


class MainPageSettingsBanner(models.Model):
    main_page_settings = models.ForeignKey(
        MainPageSettings, on_delete=models.CASCADE)
    banner_image = models.FileField(
        upload_to='uploads/main_page_settings/banner_image/')

    @property
    def banner_image_url(self):
        if self.banner_image:
            return "%s%s" % (settings.HOST, self.banner_image.url)

    def __str__(self):
        return f"{self.main_page_settings.pk} - banner"


class About(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'About'

    class Meta:
        db_table = 'about'
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Menu(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500, null=True)
    order = models.IntegerField()
    is_footer = models.BooleanField(default=False)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='childs', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class Meta:
        db_table = 'menu'
        ordering = ['order']
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
