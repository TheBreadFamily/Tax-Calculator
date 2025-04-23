
def compute_tax(income, status, year):
    # Federal tax brackets
    brackets_by_year = {
        2021: [
            ("Single", 0.10, 0, 9950),
            ("Single", 0.12, 9950, 40525),
            ("Single", 0.22, 40525, 86375),
            ("Single", 0.24, 86375, 164925),
            ("Single", 0.32, 164925, 209425),
            ("Single", 0.35, 209425, 523600),
            ("Single", 0.37, 523600, float("inf")),

            ("Married Filing Jointly", 0.10, 0, 19900),
            ("Married Filing Jointly", 0.12, 19900, 81050),
            ("Married Filing Jointly", 0.22, 81050, 172750),
            ("Married Filing Jointly", 0.24, 172750, 329850),
            ("Married Filing Jointly", 0.32, 329850, 418850),
            ("Married Filing Jointly", 0.35, 418850, 628300),
            ("Married Filing Jointly", 0.37, 628300, float("inf")),

            ("Married Filing Separately", 0.10, 0, 9950),
            ("Married Filing Separately", 0.12, 9950, 40525),
            ("Married Filing Separately", 0.22, 40525, 86375),
            ("Married Filing Separately", 0.24, 86375, 164925),
            ("Married Filing Separately", 0.32, 164925, 209425),
            ("Married Filing Separately", 0.35, 209425, 314150),
            ("Married Filing Separately", 0.37, 314150, float("inf")),

            ("Head of Household", 0.10, 0, 14200),
            ("Head of Household", 0.12, 14200, 54200),
            ("Head of Household", 0.22, 54200, 86350),
            ("Head of Household", 0.24, 86350, 164900),
            ("Head of Household", 0.32, 164900, 209400),
            ("Head of Household", 0.35, 209400, 523600),
            ("Head of Household", 0.37, 523600, float("inf")),
        ],
        2022: [
            ("Single", 0.10, 0, 10275),
            ("Single", 0.12, 10275, 41775),
            ("Single", 0.22, 41775, 89075),
            ("Single", 0.24, 89075, 170050),
            ("Single", 0.32, 170050, 215950),
            ("Single", 0.35, 215950, 539900),
            ("Single", 0.37, 539900, float("inf")),

            ("Married Filing Jointly", 0.10, 0, 20550),
            ("Married Filing Jointly", 0.12, 20550, 83550),
            ("Married Filing Jointly", 0.22, 83550, 178150),
            ("Married Filing Jointly", 0.24, 178150, 340100),
            ("Married Filing Jointly", 0.32, 340100, 431900),
            ("Married Filing Jointly", 0.35, 431900, 647850),
            ("Married Filing Jointly", 0.37, 647850, float("inf")),

            ("Married Filing Separately", 0.10, 0, 10275),
            ("Married Filing Separately", 0.12, 10275, 41775),
            ("Married Filing Separately", 0.22, 41775, 89075),
            ("Married Filing Separately", 0.24, 89075, 170050),
            ("Married Filing Separately", 0.32, 170050, 215950),
            ("Married Filing Separately", 0.35, 215950, 323925),
            ("Married Filing Separately", 0.37, 323925, float("inf")),

            ("Head of Household", 0.10, 0, 14650),
            ("Head of Household", 0.12, 14650, 55900),
            ("Head of Household", 0.22, 55900, 89050),
            ("Head of Household", 0.24, 89050, 170050),
            ("Head of Household", 0.32, 170050, 215950),
            ("Head of Household", 0.35, 215950, 539900),
            ("Head of Household", 0.37, 539900, float("inf")),
        ],
        2023: [
            ("Single", 0.10, 0, 11000),
            ("Single", 0.12, 11000, 44725),
            ("Single", 0.22, 44725, 95375),
            ("Single", 0.24, 95375, 182100),
            ("Single", 0.32, 182100, 231250),
            ("Single", 0.35, 231250, 578125),
            ("Single", 0.37, 578125, float("inf")),

            ("Married Filing Jointly", 0.10, 0, 22000),
            ("Married Filing Jointly", 0.12, 22000, 89450),
            ("Married Filing Jointly", 0.22, 89450, 190750),
            ("Married Filing Jointly", 0.24, 190750, 364200),
            ("Married Filing Jointly", 0.32, 364200, 462500),
            ("Married Filing Jointly", 0.35, 462500, 693750),
            ("Married Filing Jointly", 0.37, 693750, float("inf")),

            ("Married Filing Separately", 0.10, 0, 11000),
            ("Married Filing Separately", 0.12, 11000, 44725),
            ("Married Filing Separately", 0.22, 44725, 95375),
            ("Married Filing Separately", 0.24, 95375, 182100),
            ("Married Filing Separately", 0.32, 182100, 231250),
            ("Married Filing Separately", 0.35, 231250, 346875),
            ("Married Filing Separately", 0.37, 346875, float("inf")),

            ("Head of Household", 0.10, 0, 15700),
            ("Head of Household", 0.12, 15700, 59850),
            ("Head of Household", 0.22, 59850, 95350),
            ("Head of Household", 0.24, 95350, 182100),
            ("Head of Household", 0.32, 182100, 231250),
            ("Head of Household", 0.35, 231250, 578100),
            ("Head of Household", 0.37, 578100, float("inf")),
        ]
    }

    brackets = brackets_by_year.get(year, [])
    tax = 0
    for s, rate, low, high in brackets:
        if s == status and income > low:
            taxable = min(income, high) - low
            tax += taxable * rate
    after_tax = income - tax
    return round(tax, 2), round(after_tax, 2)

# Example usage
if __name__ == "__main__":
    print(compute_tax(60000, "Single", 2023))  # Example
    print(compute_tax(247800, "Married Filing Separately", 2022))
