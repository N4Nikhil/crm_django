
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True, verbose_name='Treatment Pronouns for the customer')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('assigned', 'Assigned'), ('in process', 'In Process'), ('converted', 'Converted'), ('recycled', 'Recycled'), ('dead', 'Dead')], max_length=255, null=True, verbose_name='Status of Lead')),
                ('source', models.CharField(blank=True, choices=[('call', 'Call'), ('email', 'Email'), ('existing customer', 'Existing Customer'), ('partner', 'Partner'), ('public relations', 'Public Relations'), ('compaign', 'Campaign'), ('other', 'Other')], max_length=255, null=True, verbose_name='Source of Lead')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Website')),
                ('description', models.TextField(blank=True, null=True)),
                ('account_name', models.CharField(blank=True, max_length=255, null=True)),
                ('opportunity_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Opportunity Amount')),
                ('createdOn', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('isActive', models.BooleanField(default=False)),
                ('enquery_type', models.CharField(blank=True, max_length=255, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Leads', to='accounts.Account')),
                ('assigned_to', models.ManyToManyField(related_name='lead_assigned_users', to=settings.AUTH_USER_MODEL)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
