
from decimal import Decimal

# Predefined federal tax brackets using Decimal
brackets_by_year = {
    2021: {
        "Single": [
            (Decimal("0"), Decimal("9950"), Decimal("0.10")),
            (Decimal("9950"), Decimal("40525"), Decimal("0.12")),
            (Decimal("40525"), Decimal("86375"), Decimal("0.22")),
            (Decimal("86375"), Decimal("164925"), Decimal("0.24")),
            (Decimal("164925"), Decimal("209425"), Decimal("0.32")),
            (Decimal("209425"), Decimal("523600"), Decimal("0.35")),
            (Decimal("523600"), None, Decimal("0.37")),
        ],
        "Married Filing Jointly": [
            (Decimal("0"), Decimal("19900"), Decimal("0.10")),
            (Decimal("19900"), Decimal("81050"), Decimal("0.12")),
            (Decimal("81050"), Decimal("172750"), Decimal("0.22")),
            (Decimal("172750"), Decimal("329850"), Decimal("0.24")),
            (Decimal("329850"), Decimal("418850"), Decimal("0.32")),
            (Decimal("418850"), Decimal("628300"), Decimal("0.35")),
            (Decimal("628300"), None, Decimal("0.37")),
        ],
        "Married Filing Separately": [
            (Decimal("0"), Decimal("9950"), Decimal("0.10")),
            (Decimal("9950"), Decimal("40525"), Decimal("0.12")),
            (Decimal("40525"), Decimal("86375"), Decimal("0.22")),
            (Decimal("86375"), Decimal("164925"), Decimal("0.24")),
            (Decimal("164925"), Decimal("209425"), Decimal("0.32")),
            (Decimal("209425"), Decimal("314150"), Decimal("0.35")),
            (Decimal("314150"), None, Decimal("0.37")),
        ],
        "Head of Household": [
            (Decimal("0"), Decimal("14200"), Decimal("0.10")),
            (Decimal("14200"), Decimal("54200"), Decimal("0.12")),
            (Decimal("54200"), Decimal("86350"), Decimal("0.22")),
            (Decimal("86350"), Decimal("164900"), Decimal("0.24")),
            (Decimal("164900"), Decimal("209400"), Decimal("0.32")),
            (Decimal("209400"), Decimal("523600"), Decimal("0.35")),
            (Decimal("523600"), None, Decimal("0.37")),
        ]
    },
    2022: {
        "Single": [
            (Decimal("0"), Decimal("10275"), Decimal("0.10")),
            (Decimal("10275"), Decimal("41775"), Decimal("0.12")),
            (Decimal("41775"), Decimal("89075"), Decimal("0.22")),
            (Decimal("89075"), Decimal("170050"), Decimal("0.24")),
            (Decimal("170050"), Decimal("215950"), Decimal("0.32")),
            (Decimal("215950"), Decimal("539900"), Decimal("0.35")),
            (Decimal("539900"), None, Decimal("0.37")),
        ],
        "Married Filing Jointly": [
            (Decimal("0"), Decimal("20550"), Decimal("0.10")),
            (Decimal("20550"), Decimal("83550"), Decimal("0.12")),
            (Decimal("83550"), Decimal("178150"), Decimal("0.22")),
            (Decimal("178150"), Decimal("340100"), Decimal("0.24")),
            (Decimal("340100"), Decimal("431900"), Decimal("0.32")),
            (Decimal("431900"), Decimal("647850"), Decimal("0.35")),
            (Decimal("647850"), None, Decimal("0.37")),
        ],
        "Married Filing Separately": [
            (Decimal("0"), Decimal("10275"), Decimal("0.10")),
            (Decimal("10275"), Decimal("41775"), Decimal("0.12")),
            (Decimal("41775"), Decimal("89075"), Decimal("0.22")),
            (Decimal("89075"), Decimal("170050"), Decimal("0.24")),
            (Decimal("170050"), Decimal("215950"), Decimal("0.32")),
            (Decimal("215950"), Decimal("323925"), Decimal("0.35")),
            (Decimal("323925"), None, Decimal("0.37")),
        ],
        "Head of Household": [
            (Decimal("0"), Decimal("14650"), Decimal("0.10")),
            (Decimal("14650"), Decimal("55900"), Decimal("0.12")),
            (Decimal("55900"), Decimal("89050"), Decimal("0.22")),
            (Decimal("89050"), Decimal("170050"), Decimal("0.24")),
            (Decimal("170050"), Decimal("215950"), Decimal("0.32")),
            (Decimal("215950"), Decimal("539900"), Decimal("0.35")),
            (Decimal("539900"), None, Decimal("0.37")),
        ]
    },
    2023: {
        "Single": [
            (Decimal("0"), Decimal("11000"), Decimal("0.10")),
            (Decimal("11000"), Decimal("44725"), Decimal("0.12")),
            (Decimal("44725"), Decimal("95375"), Decimal("0.22")),
            (Decimal("95375"), Decimal("182100"), Decimal("0.24")),
            (Decimal("182100"), Decimal("231250"), Decimal("0.32")),
            (Decimal("231250"), Decimal("578125"), Decimal("0.35")),
            (Decimal("578125"), None, Decimal("0.37")),
        ],
        "Married Filing Jointly": [
            (Decimal("0"), Decimal("22000"), Decimal("0.10")),
            (Decimal("22000"), Decimal("89450"), Decimal("0.12")),
            (Decimal("89450"), Decimal("190750"), Decimal("0.22")),
            (Decimal("190750"), Decimal("364200"), Decimal("0.24")),
            (Decimal("364200"), Decimal("462500"), Decimal("0.32")),
            (Decimal("462500"), Decimal("693750"), Decimal("0.35")),
            (Decimal("693750"), None, Decimal("0.37")),
        ],
        "Married Filing Separately": [
            (Decimal("0"), Decimal("11000"), Decimal("0.10")),
            (Decimal("11000"), Decimal("44725"), Decimal("0.12")),
            (Decimal("44725"), Decimal("95375"), Decimal("0.22")),
            (Decimal("95375"), Decimal("182100"), Decimal("0.24")),
            (Decimal("182100"), Decimal("231250"), Decimal("0.32")),
            (Decimal("231250"), Decimal("346875"), Decimal("0.35")),
            (Decimal("346875"), None, Decimal("0.37")),
        ],
        "Head of Household": [
            (Decimal("0"), Decimal("15700"), Decimal("0.10")),
            (Decimal("15700"), Decimal("59850"), Decimal("0.12")),
            (Decimal("59850"), Decimal("95350"), Decimal("0.22")),
            (Decimal("95350"), Decimal("182100"), Decimal("0.24")),
            (Decimal("182100"), Decimal("231250"), Decimal("0.32")),
            (Decimal("231250"), Decimal("578100"), Decimal("0.35")),
            (Decimal("578100"), None, Decimal("0.37")),
        ]
    }
}

def compute_tax_decimal(income, status, year):
    brackets = brackets_by_year[year][status]
    tax = Decimal("0.00")
    for lower, upper, rate in brackets:
        if upper is None or income <= upper:
            tax += (income - lower) * rate
            break
        else:
            tax += (upper - lower) * rate
    after_tax = income - tax
    return tax.quantize(Decimal("0.01")), after_tax.quantize(Decimal("0.01"))
