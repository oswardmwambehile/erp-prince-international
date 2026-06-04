from django.contrib import admin
from .models import AccountType, ChartOfAccount, JournalEntry, JournalEntryLine


class JournalEntryLineInline(admin.TabularInline):
    model = JournalEntryLine
    extra = 1


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('journal_number', 'company', 'posting_date', 'status')
    inlines = [JournalEntryLineInline]


admin.site.register(AccountType)
admin.site.register(ChartOfAccount)