# Generated by Django 4.0.3 on 2022-06-24 01:41

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_mostdownloaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='mostdownloaded',
            name='Bottom_discription',
            field=froala_editor.fields.FroalaField(null=True),
        ),
        migrations.AddField(
            model_name='mostdownloaded',
            name='Top_discription',
            field=froala_editor.fields.FroalaField(null=True),
        ),
    ]