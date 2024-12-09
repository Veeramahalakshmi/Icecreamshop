from django.db import migrations

def add_initial_icecreams(apps, schema_editor):
    IceCream = apps.get_model('icecreamshop', 'IceCream')
    initial_icecreams = [
        {"name": "Vanilla Delight", "price": 300},
        {"name": "Chocolate Heaven", "price": 400},
        {"name": "Strawberry Bliss", "price": 350},
        {"name": "Mango Magic", "price": 375},
        {"name": "Pistachio Crunch", "price": 425},
        {"name": "Blueberry Burst", "price": 380},
        {"name": "Cookie Dough Delight", "price": 450},
        {"name": "Mint Chocolate Chip", "price": 400},
        {"name": "Caramel Swirl", "price": 410},
    ]

    for ice_cream in initial_icecreams:
        IceCream.objects.create(**ice_cream)

class Migration(migrations.Migration):
    dependencies = [
        ('icecreamshop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_icecreams),
    ]
