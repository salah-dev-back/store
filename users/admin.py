from django.contrib import admin

from users.models import EmailVerification, User

admin.site.register(User)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration',)
    fields = ('code', 'user', 'expiration', 'created_at',)
    readonly_fields = ('created_at',)
