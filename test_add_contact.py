import pytest
from contact import *
from application import ApplicationContact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.log_in(username="admin", password="secret")
    app.fill_fio(FIO(firstname="Yuriy", middlename="Ivanovich", lastname="Mishin", nickname="Yesman"))
    app.company_name(Office(title_company="OOO Horns and Hooves"))
    app.contact_information(Contact(address="Moscow City", homephone="84951231234", mobilephone="89997776655",
                                 position="QA Engineer", fax="8495", main_email="pochta1@ru.ru",
                                 other_email="pochta2@ru.ru",
                                 extra_email="pochta3@ru.ru", web_site="wwww"))
    app.specify_the_birthday(Birthday(day_b="1", month_b="October", year_b="1990"))
    app.specify_the_anniversary(Anniversary(day_a="1", month_a="January", year_a="2000"))
    app.selection_group(select_group="dfgh")
    app.log_out()