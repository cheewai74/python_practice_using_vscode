import pytest

from django.contrib.auth.models import User


def test_home_view(client):
    response = client.get(path='/')
    assert response.status_code == 200
    assert 'Welcome to SmartNotes!' in str(response.content)
    
def test_signup(client):
    response = client.get(path='/signup')
    assert response.status_code == 200
    assert 'home/register.html' in response.template_name
   
@pytest.mark.django_db
def test_signup_authenticated(client):
    # user = User.objects.create_user('Jake Chang', 'jakechang@outlook.com','password')
    # client.login(username=user.username, password='password')
    
    user = User.objects.create_user('Jake Chang', 'jakechang@outlook.com','password')
    client.login(username=user.username, password='password')
    
    response = client.get(path='/signup', follow=True)
    print(type(response))
    assert response.status_code == 200
    assert 'notes/notes_list.html' in response.template_name 