from behave import given, when, then
from flaskr import app

@given('flaskr is setup')
def setup_flaskr(context):
    context.client = app.test_client()
    # Slightly changed some chatGPT code
    # with app.app_context():
    #     db.create_all()
    db = context.db

@when('i login with "{username}" and "{password}"')
def login(context, username, password):
    response = context.client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)
    context.response = response

@then('i should see the alert "{message}"')
def see_alert(context, message):
    assert message in context.response.data.decode()

@given('i login with "{username}" and "{password}"')
def login_given(context, username, password):
    context.execute_steps(f'When i login with "{username}" and "{password}"')

@when('i logout')
def logout(context):
    response = context.client.get('/logout', follow_redirects=True)
    context.response = response
