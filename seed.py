import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.contrib.auth.models import User
from recipes.models import Recipe, Category, Tag
from faker import Faker
from random import randint, sample
from django.utils.text import slugify
import uuid


def run_seed():
    fake = Faker('pt_BR')

    author, _ = User.objects.get_or_create(
        username='admin',
        defaults={'email': 'admin@email.com'}
    )
    author.set_password('123456')
    author.save()

    categories = [
        Category.objects.get_or_create(name=fake.word())[0]
        for _ in range(5)
    ]

    tags = [
        Tag.objects.get_or_create(name=fake.word())[0]
        for _ in range(10)
    ]

    for _ in range(50):
        title = fake.sentence(nb_words=3).replace('.', '')
        slug = f"{slugify(title)}-{uuid.uuid4().hex[:8]}"

        recipe = Recipe.objects.create(
            title=title,
            slug=slug,
            description=fake.sentence(),
            preparation_time=randint(10, 90),
            preparation_time_unit='minutos',
            servings=randint(1, 6),
            servings_unit='porções',
            preparation_steps='\n'.join(fake.paragraphs(3)),
            category=sample(categories, 1)[0],
            author=author,
            is_published=True,
        )

        recipe.tags.set(sample(tags, randint(1, 3)))

    print('✅ Seed executado com sucesso!')


if __name__ == "__main__":
    run_seed()
