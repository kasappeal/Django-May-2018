# Generated by Django 2.0.5 on 2018-05-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('image', models.FileField(null=True, upload_to='')),
                ('send_choice', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('BUY', 'Buying'), ('SEL', 'Selling')], default='SEL', max_length=3)),
                ('status', models.CharField(choices=[('PEN', 'Pending'), ('APR', 'Approved'), ('FIN', 'Finished')], default='PEN', max_length=3)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]