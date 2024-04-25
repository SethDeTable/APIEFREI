# Generated by Django 5.0.4 on 2024-04-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EggGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=79)),
            ],
            options={
                'db_table': 'egg_groups',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=79)),
                ('category_id', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('fling_power', models.IntegerField(null=True)),
                ('fling_effect_id', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('region_id', models.IntegerField(null=True)),
                ('identifier', models.CharField(max_length=79)),
            ],
            options={
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=79)),
                ('generation_id', models.IntegerField()),
                ('type_id', models.IntegerField()),
                ('power', models.SmallIntegerField(null=True)),
                ('pp', models.SmallIntegerField(null=True)),
                ('accuracy', models.SmallIntegerField(null=True)),
                ('priority', models.SmallIntegerField()),
                ('target_id', models.IntegerField()),
                ('damage_class_id', models.IntegerField()),
                ('effect_id', models.IntegerField()),
                ('effect_chance', models.IntegerField(null=True)),
                ('contest_type_id', models.IntegerField(null=True)),
                ('contest_effect_id', models.IntegerField(null=True)),
                ('super_contest_effect_id', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'moves',
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=79)),
                ('species_id', models.IntegerField(null=True)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('base_experience', models.IntegerField()),
                ('order', models.IntegerField()),
                ('is_default', models.BooleanField()),
            ],
            options={
                'db_table': 'pokemon',
            },
        ),
        migrations.CreateModel(
            name='PokemonEggGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_id', models.IntegerField()),
                ('egg_group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'pokemon_egg_groups',
            },
        ),
        migrations.CreateModel(
            name='PokemonFormGenerations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_form_id', models.IntegerField()),
                ('generation_id', models.IntegerField()),
                ('game_index', models.IntegerField()),
            ],
            options={
                'db_table': 'pokemon_form_generations',
            },
        ),
        migrations.CreateModel(
            name='PokemonMoves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_id', models.IntegerField()),
                ('version_group_id', models.IntegerField()),
                ('move_id', models.IntegerField()),
                ('pokemon_move_method_id', models.IntegerField()),
                ('level', models.IntegerField()),
                ('order', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'pokemon_moves',
            },
        ),
        migrations.CreateModel(
            name='PokemonStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_id', models.IntegerField()),
                ('stat_id', models.IntegerField()),
                ('base_stat', models.IntegerField()),
                ('effort', models.IntegerField()),
            ],
            options={
                'db_table': 'pokemon_stats',
            },
        ),
        migrations.CreateModel(
            name='PokemonTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_id', models.IntegerField()),
                ('type_id', models.IntegerField()),
                ('slot', models.IntegerField()),
            ],
            options={
                'db_table': 'pokemon_types',
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('damage_class_id', models.IntegerField(null=True)),
                ('identifier', models.CharField(max_length=79)),
                ('is_battle_only', models.BooleanField()),
                ('game_index', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'stats',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=79)),
                ('generation_id', models.IntegerField()),
                ('damage_class_id', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'types',
            },
        ),
    ]
