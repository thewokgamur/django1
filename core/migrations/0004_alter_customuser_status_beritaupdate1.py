# Generated by Django 4.2.7 on 2023-11-17 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_customuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(blank=True, choices=[('viewers', 'viewers'), ('admin', 'admin')], default='admin', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='beritaupdate1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=225)),
                ('deskripsi', models.CharField(max_length=225, null=True)),
                ('isi', models.CharField(max_length=9999)),
                ('kategoriid', models.IntegerField(blank=True, null=True)),
                ('gambar', models.ImageField(upload_to='media')),
                ('penulis', models.CharField(max_length=225)),
                ('status', models.CharField(blank=True, choices=[('publish', 'publish'), ('draft', 'draft')], max_length=255, null=True)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.kategori')),
            ],
        ),
    ]