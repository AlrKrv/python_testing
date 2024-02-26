import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.log_in(username="admin", password="secret")
    app.create_contact(Contact(firstname="Yuriy", middlename="Ivanovich", lastname="Mishin",
                               nickname="Yesman", title_company="OOO Horns and Hooves", address="Moscow City",
                               homephone="84951231234",
                               mobilephone="89997776655", position="QA Engineer", fax="8495",
                               main_email="pochta1@ru.ru", other_email="pochta2@ru.ru", extra_email="pochta3@ru.ru",
                               web_site="wwww", day_b="1", month_b="October", year_b="1990", day_a="1",
                               month_a="January", year_a="2000"))
    app.session.log_out()
