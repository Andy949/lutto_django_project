# Generated by Django 2.1.1 on 2018-10-17 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
        ('course', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courselike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='coursecommentlike',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseComment'),
        ),
        migrations.AddField(
            model_name='coursecommentlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='coursecomment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
        migrations.AddField(
            model_name='coursecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseLevel'),
        ),
        migrations.AddField(
            model_name='course',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Machine'),
        ),
        migrations.AddField(
            model_name='course',
            name='picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CoursePicture'),
        ),
        migrations.AddField(
            model_name='course',
            name='recipes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.RecipesPlan'),
        ),
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseType'),
        ),
    ]
