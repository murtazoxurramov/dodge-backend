from rest_framework import serializers

from .models import Menu, MainPageSettings, MainPageSettingsBanner, About, PromotionApplication, Contact


class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title',]


class CompanyLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageSettings
        fields = ['logo_url']


class MenuSerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'title', 'child']

    def get_child(self, obj):
        sub_menu = Menu.objects.filter(parent=obj)
        if sub_menu.exists():
            return SubMenuSerializer(sub_menu, many=True).data
        return []

    def get_company_logo(self, obj):
        company_logo = MainPageSettings.objects.all()
        if company_logo.exists():
            return CompanyLogoSerializer(company_logo, many=True).data
        return []


class MainPageSettingsBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageSettings
        fields = ['id', 'image', 'is_right']


class MainPageSettingsSerializer(serializers.ModelSerializer):
    banner_image_url = serializers.SerializerMethodField()

    class Meta:
        model = MainPageSettings
        fields = ['id', 'title', 'logo_url', 'banner_image_url']

    def get_banner_image_url(self, obj):
        banner = MainPageSettingsBanner.objects.filter(main_page_settings=obj)
        if banner.exists():
            return MainPageSettingsBannerSerializer(banner, many=True).data
        return []


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['telegram_link', 'instagram_link',
                  'facebook_link', 'youtube_link', 'twitter_link']


class PromotionApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionApplication
        filds = ['phone_number',]
