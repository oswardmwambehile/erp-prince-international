from accounts.models import Company


def get_default_company():
    company, _ = Company.objects.get_or_create(
        name="Prince International"
    )
    return company