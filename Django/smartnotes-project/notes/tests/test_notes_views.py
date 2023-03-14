import pytest

from django.contrib.auth.models import User
from notes.models import Notes

@pytest.fixture
def logged_user(client):
    user = User.objects.create_user('Jake Chang', 'jakechang@outlook.com','password')
    client.login(username=user.username, password='password')
    return user

@pytest.mark.django_db
def test_list_endpoint_return_user_notes(client, logged_user):
    # user = User.objects.create_user('Jake Chang', 'jakechang@outlook.com','password')
    # client.login(username=user.username, password='password')
    
    # note = Notes.objects.create(title="An interesting title", text='', user=user)
    # note2 = Notes.objects.create(title="Another title", text='', user=user)
    
    note = Notes.objects.create(title="An interesting title", text='', user=logged_user)
    note2 = Notes.objects.create(title="Another title", text='', user=logged_user)
    
    response = client.get(path='/smart/notes')
    assert 200 == response.status_code
    content = str(response.content)
    assert "An interesting title" in str(response.content)
    assert "Another title" in str(response.content)
    assert 2 == content.count('<h3>')