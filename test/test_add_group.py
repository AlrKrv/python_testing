import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.log_in(username="admin", password="secret")
    app.helper.GroupHelper.create_group(Group(name="dfgh", header="dfgh", footer="dfgh"))
    app.session.log_out()


def test_add_empty_group(app):
    app.session.log_in(username="admin", password="secret")
    app.helper.GroupHelper.create_group(Group(name="", header="", footer=""))
    app.session.log_out()
