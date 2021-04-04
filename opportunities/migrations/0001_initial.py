from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('stage', models.CharField(choices=[('QUALIFICATION', 'QUALIFICATION'), ('NEEDS ANALYSIS', 'NEEDS ANALYSIS'), ('VALUE PROPOSITION', 'VALUE PROPOSITION'), ('ID.DECISION MAKERS', 'ID.DECISION MAKERS'), ('PERCEPTION ANALYSIS', 'PERCEPTION ANALYSIS'), ('PROPOSAL/PRICE QUOTE', 'PROPOSAL/PRICE QUOTE'), ('NEGOTIATION/REVIEW', 'NEGOTIATION/REVIEW'), ('CLOSED WON', 'CLOSED WON'), ('CLOSED LOST', 'CLOSED LOST')], max_length=64)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Opportunity Amount')),
                ('lead_source', models.CharField(blank=True, choices=[('NONE', 'NONE'), ('CALL', 'CALL'), ('EMAIL', ' EMAIL'), ('EXISTING CUSTOMER', 'EXISTING CUSTOMER'), ('PARTNER', 'PARTNER'), ('PUBLIC RELATIONS', 'PUBLIC RELATIONS'), ('CAMPAIGN', 'CAMPAIGN'), ('WEBSITE', 'WEBSITE'), ('OTHER', 'OTHER')], max_length=255, null=True, verbose_name='Source of Lead')),
                ('probability', models.IntegerField(blank=True, default=0, null=True)),
                ('closedOn', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('isActive', models.BooleanField(default=False)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opportunities', to='accounts.Account')),
                ('closedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contacts', models.ManyToManyField(to='contacts.Contact')),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opportunity_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
