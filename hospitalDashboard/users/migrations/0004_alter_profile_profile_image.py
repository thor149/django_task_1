# Generated by Django 5.0.7 on 2024-07-31 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_profile_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(
                blank=True, default="user-default.png", null=True, upload_to=""
            ),
        ),
    ]
