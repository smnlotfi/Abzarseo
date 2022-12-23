from unicodedata import category
import factory
from faker import Faker
from django.contrib.auth.models import User
from panel.models import Product,ProductCategory


faker=Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=User

    username=faker.name()
    # lastname=faker.name()
    email='smnlotfi@gmail.com'


class ProductCategoryFactory(factory.django.DjangoModelFactory):

    class meta:
        model=ProductCategory

    name='Category One'


class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model=Product

    name=faker.name()
    category=factory.SubFactory(ProductCategory)
    description=faker.text()
    price=150