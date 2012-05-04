from django.contrib import admin
from issuetracker.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'submitter',
        'submitted_date', 'modified_date')
    list_filter = ('priority', 'status', 'submitted_date')
    search_fields = ('title', 'description',)

admin.site.register(Ticket, TicketAdmin)
