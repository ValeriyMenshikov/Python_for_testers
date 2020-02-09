# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="asdasdasd", middlename="asdasd", lastname="asdfvf", nickname="asdfsdf",
                      title="sadfvsdf", company="asdfsdfsdf", address="bvbbgfbdfgb", homephone="dcfscfsd",
                      mobilephone="12312323", workphone="dsfsdf", faxphone="123123123", mail="asdasd@mail.ru",
                      email2="asdsad@mail.ru", email3="ghh213@gmail.ru", homepage="asdasd", bday="1",
                      bmonth="January", byear="1999", aday="11", amonth="February", ayear="2000",
                      address2="sdfsdfsdf", secondaryphone="ghjnhjkn", notes="hgjkhmjkhjkm")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
