from datetime import date
from enum import Enum
from openpyxl_templates import TemplatedWorkbook
from openpyxl_templates.table_sheet import TableSheet
from openpyxl_templates.table_sheet.columns import CharColumn, ChoiceColumn, DateColumn


class Fruits(Enum):
    apple = 1
    banana = 2
    orange = 3


class PersonSheet(TableSheet):
    first_name = CharColumn()
    last_name = CharColumn()
    date_of_birth = DateColumn()
    favorite_fruit = ChoiceColumn(choices=(
        (Fruits.apple, "Apple"),
        (Fruits.banana, "Banana"),
        (Fruits.orange, "Orange"),
    ))


class PersonsWorkbook(TemplatedWorkbook):
    persons = PersonSheet()


# --------------- Write ---------------

wb = PersonsWorkbook()
wb.persons.write(
    title="List of fruit lovers",
    objects=(
        ("John", "Doe", date(year=1992, month=7, day=17), Fruits.banana),
        ("Jane", "Doe", date(year=1986, month=3, day=2), Fruits.apple),
    )
)

wb.save("fruit_lovers.xlsx")

# --------------- Read ---------------

wb = PersonsWorkbook("fruit_lovers.xlsx")

for person in wb.persons:
    print(person.first_name, person.last_name, person.favorite_fruit)
