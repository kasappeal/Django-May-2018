from django.contrib import admin
from django.contrib.admin import register
from django.utils.safestring import mark_safe

from ads.models import Ad


@register(Ad)
class AdAdmin(admin.ModelAdmin):

    autocomplete_fields = ['owner']
    list_display = ['image_html', 'name', 'owner_name', 'price', 'send_choice', 'status']
    list_filter = ['owner', 'type', 'status']
    search_fields = ['name', 'price', 'owner__first_name', 'owner__last_name', 'owner__username']

    def owner_name(self, ad):
        return '{0} {1}'.format(ad.owner.first_name, ad.owner.last_name)

    owner_name.short_description = 'Owner\'s name'
    owner_name.admin_order_field = 'owner__first_name'

    def image_html(self, ad):
        return mark_safe('<img src="{0}" alt="{1}" title="{2}" width="100">'.format(ad.image.url, ad.name, ad.name))

    image_html.short_description = 'Image'
    image_html.admin_order_field = 'image'

    readonly_fields = ['created_on', 'modified_on', 'image_html']

    fieldsets = [
        [None, {
            'fields': ['name', 'image', 'image_html', 'owner']
        }],
        ['Price & Description', {
            'fields': ['price', 'description']
        }],
        ['Attributtes', {
            'fields': ['type', 'send_choice', 'status']
        }],
        ['Important dates', {
            'fields': ['created_on', 'modified_on'],
            'classes': ['collapse']
        }]
    ]



# Cambiamos el título del admin
admin.site.site_header = 'Django Pop Admin'
admin.site.site_title = 'Django Pop Admin'
admin.site.index_title = 'Dashboard'
