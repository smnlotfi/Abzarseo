import pytest
from django.contrib.auth.models import User

def test_hompage(client):
    response=client.get(path="/")
    assert response.status_code == 200

# @pytest.mark.django_db
# def test_signup_user(client):
#     response=client.get(path="/")
#     # user=User.objects.create_user('saman','saman@example.com','saman')
#     client.login(username='admin',password='admin_admin@3')
#     assert response.status_code == 200



# def test_check_user1(user_1):
#     user_1.set_password('admin')
#     assert user_1.username == 'saman'
#     assert user_1.check_password('admin') is True


# def test_check_user2(user_1):
#     print('test_check_2')
#     user_1.set_password('admin2')
#     assert user_1.check_password('admin2') is True


def test_user_saman(user_saman):
    assert user_saman.username == 'saman'

def tests_new_user(db,user_factory):
    user=user_factory.create()
    print(User.objects.all().count())
    assert False


def test_create_product(db,product_factory):
    product=product_factory.create()
    print(product.category)
    assert False