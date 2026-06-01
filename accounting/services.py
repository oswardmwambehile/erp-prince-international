from django.db import transaction
from django.utils import timezone

from .models import JournalEntry, JournalEntryLine
from .utils import get_default_company


def generate_journal_number():
    year = timezone.now().year
    count = JournalEntry.objects.count() + 1
    return f"JE-{year}-{count:04d}"


@transaction.atomic
def create_journal_entry(company, entry_data, lines):
    """
    CORE ERP JOURNAL ENGINE
    """

    journal = JournalEntry.objects.create(
        company=company,
        journal_number=entry_data.get("journal_number") or generate_journal_number(),
        reference=entry_data.get("reference"),
        description=entry_data.get("description"),
        posting_date=entry_data.get("posting_date"),
        status="posted"
    )

    total_debit = 0
    total_credit = 0

    for line in lines:
        obj = JournalEntryLine.objects.create(
            journal_entry=journal,
            account=line["account"],
            description=line.get("description"),
            debit=line.get("debit", 0),
            credit=line.get("credit", 0),
        )

        total_debit += float(obj.debit)
        total_credit += float(obj.credit)

    # ERP RULE: MUST BALANCE
    if total_debit != total_credit:
        raise ValueError("Journal Entry not balanced (Debit ≠ Credit)")

    return journal