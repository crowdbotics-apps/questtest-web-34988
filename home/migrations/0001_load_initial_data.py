from django.db import migrations


def create_site(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    custom_domain = "questtest-web-34988.botics.co"

    site_params = {
        "name": "QuestTest Web",
    }
    if custom_domain:
        site_params["domain"] = custom_domain

    Site.objects.update_or_create(defaults=site_params, id=1)


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RunPython(create_site),
    ]
