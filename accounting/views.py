from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages

from .models import JournalEntry, JournalEntryLine
from .forms import JournalEntryForm, JournalEntryLineFormSet
from .services import create_journal_entry
from .utils import get_default_company
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages

from .models import JournalEntry, JournalEntryLine
from .forms import JournalEntryForm, JournalEntryLineFormSet
from .utils import get_default_company


@transaction.atomic
def create_journal_entry_view(request):

    company = get_default_company()

    if request.method == "POST":

        print("=" * 50)
        print("POST DATA")
        print(request.POST)
        print("=" * 50)

        entry_form = JournalEntryForm(request.POST)

        formset = JournalEntryLineFormSet(
            request.POST,
            queryset=JournalEntryLine.objects.none()
        )

        print("ENTRY FORM VALID:", entry_form.is_valid())
        print("ENTRY FORM ERRORS:", entry_form.errors)

        print("FORMSET VALID:", formset.is_valid())
        print("FORMSET ERRORS:", formset.errors)

        if entry_form.is_valid() and formset.is_valid():

            try:

                # =========================
                # SAVE HEADER
                # =========================
                journal = entry_form.save(commit=False)

                journal.company = company

                # Auto Journal Number
                if not journal.journal_number:
                    next_no = JournalEntry.objects.count() + 1
                    journal.journal_number = f"JE-{next_no:05d}"

                journal.save()

                print("JOURNAL SAVED:", journal.id)
                print("JOURNAL NUMBER:", journal.journal_number)

                total_debit = 0
                total_credit = 0

                saved_lines = 0

                for form in formset:

                    print("LINE DATA:", form.cleaned_data)

                    if not form.cleaned_data:
                        continue

                    account = form.cleaned_data.get("account")
                    description = form.cleaned_data.get("description")
                    debit = form.cleaned_data.get("debit") or 0
                    credit = form.cleaned_data.get("credit") or 0

                    print(
                        "ACCOUNT:",
                        account,
                        "DEBIT:",
                        debit,
                        "CREDIT:",
                        credit
                    )

                    if not account:
                        print("SKIPPED - NO ACCOUNT")
                        continue

                    total_debit += float(debit)
                    total_credit += float(credit)

                    JournalEntryLine.objects.create(
                        journal_entry=journal,
                        account=account,
                        description=description,
                        debit=debit,
                        credit=credit
                    )

                    saved_lines += 1

                    print("LINE SAVED")

                print("TOTAL DEBIT:", total_debit)
                print("TOTAL CREDIT:", total_credit)
                print("LINES SAVED:", saved_lines)

                # Must have at least one line
                if saved_lines == 0:

                    transaction.set_rollback(True)

                    messages.error(
                        request,
                        "Please select at least one account."
                    )

                    return render(
                        request,
                        "accounting/journal_form.html",
                        {
                            "entry_form": entry_form,
                            "formset": formset
                        }
                    )

                # Must balance
                if total_debit != total_credit:

                    transaction.set_rollback(True)

                    messages.error(
                        request,
                        f"Journal not balanced. Debit={total_debit} Credit={total_credit}"
                    )

                    return render(
                        request,
                        "accounting/journal_form.html",
                        {
                            "entry_form": entry_form,
                            "formset": formset
                        }
                    )

                messages.success(
                    request,
                    "Journal Entry created successfully!"
                )

                return redirect("journal_list")

            except Exception as e:

                print("ERROR:", str(e))

                messages.error(
                    request,
                    f"Error saving journal: {e}"
                )

        else:

            print("FORM VALIDATION FAILED")

    else:

        entry_form = JournalEntryForm()

        formset = JournalEntryLineFormSet(
            queryset=JournalEntryLine.objects.none()
        )

    return render(
        request,
        "accounting/journal_form.html",
        {
            "entry_form": entry_form,
            "formset": formset
        }
    )


from django.shortcuts import render, get_object_or_404, redirect
from .models import AccountType
from .forms import AccountTypeForm


def account_type_list_create(request):
    account_types = AccountType.objects.all().order_by('-id')

    # EDIT MODE
    edit_instance = None
    if request.GET.get('edit'):
        edit_instance = get_object_or_404(AccountType, id=request.GET.get('edit'))

    # FORM
    form = AccountTypeForm(instance=edit_instance)

    # CREATE / UPDATE SUBMIT
    if request.method == "POST":
        if request.POST.get("id"):  # update
            instance = get_object_or_404(AccountType, id=request.POST.get("id"))
            form = AccountTypeForm(request.POST, instance=instance)
        else:  # create
            form = AccountTypeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("account_type_list_create")

    return render(request, "accounting/account_type.html", {
        "form": form,
        "account_types": account_types,
        "edit_instance": edit_instance,
    })



from django.shortcuts import render, redirect, get_object_or_404
from .models import ChartOfAccount
from .forms import ChartOfAccountForm


def chart_of_accounts(request):
    edit_instance = None

    # EDIT MODE
    if request.GET.get("edit"):
        edit_instance = get_object_or_404(
            ChartOfAccount,
            id=request.GET.get("edit")
        )

    # FORM INIT
    form = ChartOfAccountForm(instance=edit_instance)

    # POST HANDLING
    if request.method == "POST":

        if request.POST.get("id"):
            edit_instance = get_object_or_404(
                ChartOfAccount,
                id=request.POST.get("id")
            )
            form = ChartOfAccountForm(request.POST, instance=edit_instance)
        else:
            form = ChartOfAccountForm(request.POST)

        if form.is_valid():
            account = form.save(commit=False)

            # DEFAULT COMPANY (optional but safe)
            if not account.company_id:
                from .models import get_default_company
                account.company = get_default_company()

            # AUTO CODE IF EMPTY
            if not account.account_code:
                count = ChartOfAccount.objects.count() + 1
                account.account_code = f"ACC-{count:04d}"

            account.save()
            return redirect("chart_of_accounts")

    # LIST DATA
    accounts = ChartOfAccount.objects.all().order_by("account_code")

    return render(request, "accounting/chart_of_accounts.html", {
        "form": form,
        "accounts": accounts,
        "edit_instance": edit_instance,
    })


from django.shortcuts import render
from .models import JournalEntry


def journal_list(request):

    journals = JournalEntry.objects.prefetch_related(
        "lines"
    ).order_by("-created_at")

    return render(
        request,
        "accounting/journal_list.html",
        {
            "journals": journals
        }
    )

from decimal import Decimal

from django.shortcuts import render

from .models import ChartOfAccount, JournalEntryLine


def general_ledger_view(request):

    accounts = ChartOfAccount.objects.select_related(
        "account_type"
    ).all()

    ledger_data = []

    for account in accounts:

        lines = (
            JournalEntryLine.objects
            .filter(account=account)
            .select_related("journal_entry")
            .order_by(
                "journal_entry__posting_date",
                "journal_entry__id",
                "id"
            )
        )

        balance = Decimal("0.00")
        ledger_lines = []

        account_type = ""
        if account.account_type:
            account_type = account.account_type.name.lower()

        debit_normal_accounts = [
            "asset",
            "assets",
            "expense",
            "expenses",
        ]

        for line in lines:

            debit = line.debit or Decimal("0.00")
            credit = line.credit or Decimal("0.00")

            # =========================
            # ACCOUNTING LOGIC (KEEP)
            # =========================
            if account_type in debit_normal_accounts:
                balance += debit - credit
            else:
                balance += credit - debit

            # =========================
            # DISPLAY FORMAT FIX
            # =========================
            display_balance = abs(balance)
            balance_type = "Dr" if balance >= 0 else "Cr"

            ledger_lines.append({
                "date": line.journal_entry.posting_date,
                "journal_no": line.journal_entry.journal_number,
                "description": line.description,
                "debit": debit,
                "credit": credit,
                "balance": display_balance,
                "balance_type": balance_type,
            })

        if ledger_lines:
            final_display_balance = abs(balance)
            final_balance_type = "Dr" if balance >= 0 else "Cr"

            ledger_data.append({
                "account": account,
                "lines": ledger_lines,
                "closing_balance": final_display_balance,
                "closing_balance_type": final_balance_type,
            })

    return render(
        request,
        "accounting/general_ledger.html",
        {
            "ledger_data": ledger_data
        }
    )


from decimal import Decimal
from django.shortcuts import render
from django.db.models import Sum
from .models import ChartOfAccount, JournalEntryLine


def trial_balance_view(request):

    trial_data = []

    total_debit = Decimal("0.00")
    total_credit = Decimal("0.00")

    # ⚡ FIX 1: ONLY accounts that actually have entries
    accounts = ChartOfAccount.objects.filter(
        journalentryline__isnull=False
    ).distinct().select_related("account_type")

    for account in accounts:

        agg = JournalEntryLine.objects.filter(account=account).aggregate(
            debit=Sum("debit"),
            credit=Sum("credit")
        )

        debit = agg["debit"] or Decimal("0.00")
        credit = agg["credit"] or Decimal("0.00")

        balance = debit - credit

        account_type = (
            account.account_type.name.lower()
            if account.account_type
            else ""
        )

        debit_normal = account_type in ["asset", "assets", "expense", "expenses"]

        if debit_normal:
            tb_debit = balance if balance > 0 else Decimal("0.00")
            tb_credit = Decimal("0.00")
        else:
            tb_debit = Decimal("0.00")
            tb_credit = -balance if balance < 0 else Decimal("0.00")

        # ⚡ FIX 2: skip truly empty rows
        if tb_debit == 0 and tb_credit == 0:
            continue

        trial_data.append({
            "account": account,
            "debit": tb_debit,
            "credit": tb_credit,
        })

        total_debit += tb_debit
        total_credit += tb_credit

    return render(request, "accounting/trial_balance.html", {
        "trial_data": trial_data,
        "total_debit": total_debit,
        "total_credit": total_credit,
    })


from django.db.models import Sum
from decimal import Decimal
from .models import ChartOfAccount, JournalEntryLine

def income_statement_view(request):

    revenue_accounts = ChartOfAccount.objects.filter(account_type__name="Revenue")
    expense_accounts = ChartOfAccount.objects.filter(account_type__name="Expense")

    revenue = Decimal("0.00")
    expenses = Decimal("0.00")

    for acc in revenue_accounts:
        total = JournalEntryLine.objects.filter(account=acc).aggregate(
            total=Sum("credit")
        )["total"] or 0
        revenue += total

    for acc in expense_accounts:
        total = JournalEntryLine.objects.filter(account=acc).aggregate(
            total=Sum("debit")
        )["total"] or 0
        expenses += total

    net_profit = revenue - expenses

    context = {
        "revenue": revenue,
        "expenses": expenses,
        "net_profit": net_profit,
    }

    return render(request, "reports/income_statement.html", context)


def balance_sheet_view(request):

    asset_accounts = ChartOfAccount.objects.filter(account_type__name="Asset")
    liability_accounts = ChartOfAccount.objects.filter(account_type__name="Liability")
    equity_accounts = ChartOfAccount.objects.filter(account_type__name="Equity")

    def get_balance(accounts):

        total = Decimal("0.00")

        for acc in accounts:

            debit = JournalEntryLine.objects.filter(
                account=acc,
                journal_entry__status="posted"
            ).aggregate(total=Sum("debit"))["total"] or 0

            credit = JournalEntryLine.objects.filter(
                account=acc,
                journal_entry__status="posted"
            ).aggregate(total=Sum("credit"))["total"] or 0

            # Asset = Debit - Credit
            total += (debit - credit)

        return total

    assets = get_balance(asset_accounts)
    liabilities = get_balance(liability_accounts)
    equity = get_balance(equity_accounts)

    return render(request, "reports/balance_sheet.html", {
        "assets": assets,
        "liabilities": liabilities,
        "equity": equity,
    })