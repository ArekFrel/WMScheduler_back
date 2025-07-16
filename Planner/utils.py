from Planner.models import ItemsToPlan
from Planner.const import CURSOR ,ENGINE
from sqlalchemy import text


def fetch_data():
    with ENGINE.connect() as conn:
        result = conn.execute(text("SELECT * FROM [dbo].[items_to_plan]() order by id"))
        items = [row for row in result]
    return items


def refresh_data():
    ItemsToPlan.objects.all().delete()
    items = fetch_data()
    for item in items:
        ItemsToPlan.objects.create(
            item_id=item[0],
            drawing=item[1],
            po=item[2],
            material=item[3],
            comment=item[4],
            przygotowka=item[5],
            order_start=item[6],
            all_operations=item[7],
            is_saw=bool(item[8]),
            sawcutting_time=item[9],
            sawcutting_start=item[10],
            sawcutting_finish=item[11],
            is_milling=bool(item[12]),
            milling_time=item[13],
            milling_start=item[14],
            milling_finish=item[15],
            is_turning=bool(item[16]),
            turning_time=item[17],
            turning_start=item[18],
            turning_finish=item[19]
        )
        # print(item[0])


if __name__ == '__main__':
    pass
    # a = fetch_data()
    # for b in a:
    #     print(type(b[14]))