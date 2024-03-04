from model.group import Group


def test_add_group(app):
    app.session.log_in(username="admin", password="secret")
    app.group.create_group(Group(name="dfgh", header="dfgh", footer="dfgh"))
    app.session.log_out()


def test_add_empty_group(app):
    app.session.log_in(username="admin", password="secret")
    app.group.create_group(Group(name="", header="", footer=""))
    app.session.log_out()
