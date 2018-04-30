from django.contrib import admin


from .models import Breed, Anime, Website
# Register your models here.

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    '''Admin View for Breed'''

    list_display = ('name', 'country', )


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    '''Admin View for Anime'''

    list_display = ('title', 'score', )


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    '''Admin View for Website'''

    list_display = ('name', 'link', 'owner', )
