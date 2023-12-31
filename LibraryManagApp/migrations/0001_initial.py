# Generated by Django 4.2.4 on 2023-08-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=200)),
                ('average_rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('isbn', models.CharField(max_length=13)),
                ('isbn13', models.CharField(max_length=13)),
                ('language_code', models.CharField(max_length=10)),
                ('num_pages', models.PositiveIntegerField(null=True)),
                ('ratings_count', models.PositiveIntegerField()),
                ('text_reviews_count', models.PositiveIntegerField()),
                ('publication_date', models.DateField()),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RentedBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('book_id', models.PositiveBigIntegerField()),
                ('title', models.TextField()),
                ('authors', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
    ]
