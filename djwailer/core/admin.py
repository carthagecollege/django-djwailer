from django.contrib import admin

from djwailer.core.models import LivewhaleCourseCatalog

class LivewhaleCourseCatalogAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'crs_no', 'cat', 'dept', 'credits', 'sess', 'terms'
    )
    search_fields = (
        'title', 'crs_no', 'cat', 'dept', 'credits', 'sess', 'terms'
    )
    using = "livewhale"

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(LivewhaleCourseCatalogAdmin, self).queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(LivewhaleCourseCatalogAdmin, self).formfield_for_foreignkey(db_field, request=request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(LivewhaleCourseCatalogAdmin, self).formfield_for_manytomany(db_field, request=request, using=self.using, **kwargs)

admin.site.register(LivewhaleCourseCatalog, LivewhaleCourseCatalogAdmin)
