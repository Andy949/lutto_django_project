# Generated by Django 2.1.1 on 2018-10-17 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GoodClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GoodPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('intergal', models.CharField(max_length=50)),
                # ('note1', models.CharField(max_length=50, null=True)),
                # ('note2', models.CharField(max_length=50, null=True)),
                ('goodbrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.GoodBrand')),
                ('goodclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.GoodClass')),
            ],
        ),
        migrations.AddField(
            model_name='goodpicture',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Goods'),
        ),
    ]
