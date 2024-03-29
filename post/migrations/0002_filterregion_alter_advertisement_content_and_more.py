from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Алатауский', 'Алатауский'), ('Алмалинский', 'Алмалинский район'), ('Ауэзовский', 'Ауэзовский район'), ('Бостандыкский район', 'Бостандыкский район'), ('Медеуский район', 'Медеуский район'), ('Наурызбайский', 'Наурызбайский район'), ('Турксибский', 'Турксибский район'), ('Жетысуский', 'Жетысуский район')], max_length=50, unique=True)),
                ('selected', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='regions',
            field=models.ManyToManyField(blank=True, related_name='advertisements', to='post.filterregion'),
        ),
    ]
