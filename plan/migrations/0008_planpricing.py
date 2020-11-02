# Generated by Django 3.1.2 on 2020-11-01 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0007_subscriberregistration_paid_until'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('planname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.plan')),
            ],
        ),
    ]