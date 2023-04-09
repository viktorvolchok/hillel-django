# Generated by Django 4.1.6 on 2023-04-09 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthtokenToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'authtoken_token',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('pages_count', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('count_sold', models.IntegerField()),
                ('is_archived', models.BooleanField()),
                ('code', models.IntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'books',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksAuthor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('starred', models.BooleanField()),
                ('bio', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'books_author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksAuthorprofile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('bio', models.TextField()),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'books_authorprofile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksAuthors',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'books_authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksCountry',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'books_country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksOrder',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'books_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksOrderlineitem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'books_orderlineitem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksPackaging',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('length', models.FloatField()),
            ],
            options={
                'db_table': 'books_packaging',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksPen',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('count_sold', models.IntegerField()),
            ],
            options={
                'db_table': 'books_pen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Classrooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10)),
                ('capacity', models.IntegerField()),
            ],
            options={
                'db_table': 'classrooms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomersCustomer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'customers_customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoCeleryBeatClockedschedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clocked_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_celery_beat_clockedschedule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoCeleryBeatCrontabschedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minute', models.CharField(max_length=240)),
                ('hour', models.CharField(max_length=96)),
                ('day_of_week', models.CharField(max_length=64)),
                ('day_of_month', models.CharField(max_length=124)),
                ('month_of_year', models.CharField(max_length=64)),
                ('timezone', models.CharField(max_length=63)),
            ],
            options={
                'db_table': 'django_celery_beat_crontabschedule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoCeleryBeatIntervalschedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('every', models.IntegerField()),
                ('period', models.CharField(max_length=24)),
            ],
            options={
                'db_table': 'django_celery_beat_intervalschedule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoCeleryBeatPeriodictask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('task', models.CharField(max_length=200)),
                ('args', models.TextField()),
                ('kwargs', models.TextField()),
                ('queue', models.CharField(blank=True, max_length=200, null=True)),
                ('exchange', models.CharField(blank=True, max_length=200, null=True)),
                ('routing_key', models.CharField(blank=True, max_length=200, null=True)),
                ('expires', models.DateTimeField(blank=True, null=True)),
                ('enabled', models.BooleanField()),
                ('last_run_at', models.DateTimeField(blank=True, null=True)),
                ('total_run_count', models.IntegerField()),
                ('date_changed', models.DateTimeField()),
                ('description', models.TextField()),
                ('one_off', models.BooleanField()),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('headers', models.TextField()),
                ('expire_seconds', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_celery_beat_periodictask',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoCeleryBeatPeriodictasks',
            fields=[
                ('ident', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_celery_beat_periodictasks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoCeleryBeatSolarschedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=24)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
            options={
                'db_table': 'django_celery_beat_solarschedule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LessonClassroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'lesson_classroom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'lessons',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LessonStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(blank=True, null=True)),
                ('present', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lesson_student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'students',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'teachers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksGiftpackaging',
            fields=[
                ('packaging_ptr', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='students.bookspackaging')),
                ('gift_message', models.TextField()),
            ],
            options={
                'db_table': 'books_giftpackaging',
                'managed': False,
            },
        ),
    ]
