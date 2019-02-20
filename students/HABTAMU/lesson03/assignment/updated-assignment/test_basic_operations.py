
# import os
# import peewee
import basic_operations as bo
import customers_model as cm
import pytest

CUSTOMER_1 = {'customer_id': 'WHi32145',
              'first_name': 'Daniel',
              'last_name': 'Thomas',
              'home_address': '23 Jackson Avenue, Seattle, WA, 98122',
              'phone_number': '205-123-2334',
              'email_address': 'Daniel.Thomas@yay.com',
              'status': False,
              'credit_limit': '40.0'
              }

CUSTOMER_2 = {'customer_id': 'W54Hi66',
              'first_name': 'Cho',
              'last_name': 'Asfaw',
              'home_address': '123 S LakeCity way, Seattle, WA, 98121',
              'phone_number': '232-322-1886',
              'email_address': 'cho.asfaw@uw.edu',
              'status': False,
              'credit_limit': '80.0'
            }


def drop_db():
    cm.database.drop_tables(
        [cm.Customer]
    )
    cm.database.close()


def create_db():
    drop_db()
    cm.database.create_tables(
        [cm.Customer]
    )
    cm.database.close()


def test_add_customer():
    create_db()
    bo.add_customer(**CUSTOMER_1)
    # bo.add_customer(**CUSTOMER_2)

    test_customer = cm.Customer.get(cm.Customer.customer_id == CUSTOMER_1['customer_id'])
    assert test_customer.first_name == CUSTOMER_1['first_name']
    assert test_customer.email_address == CUSTOMER_1['email_address']

    drop_db()


def create_customer_db():
    drop_db()
    cm.database.create_tables([
        cm.Customer
    ])
    bo.add_customer(**CUSTOMER_1)
    bo.add_customer(**CUSTOMER_2)

    cm.database.close()
# def test_credit_limit_float():
#     create_database()
#     bad_customer = dict(CUSTOMER_1)
#     bad_customer['credit_limit'] = '$40'
#
#     with pytest.raises(ValueError):
#         add_customer(**bad_customer)
#
#     drop_customer()


def test_search_for_customer_exists():
    create_customer_db()
    test_customer = bo.search_customer('WHi32145')
    assert test_customer['first_name'] == CUSTOMER_1['first_name']
    assert test_customer['last_name'] == CUSTOMER_1['last_name']
    assert test_customer['email_address'] == CUSTOMER_1['email_address']
    assert test_customer['phone_number'] == '205-123-2334'

    drop_db()


def test_search_for_customer_not_exist():
    create_customer_db()
    assert bo.search_customer('32145') == dict()

    drop_db()


def test_delete_customer():
    create_customer_db()
    bo.delete_customer(cm.Customer.get(cm.Customer.customer_id == CUSTOMER_1['customer_id']))

    deleted = bo.search_customer(CUSTOMER_1['customer_id'])
    assert deleted == {}

    drop_db()


def test_delete_customer_count():
    create_customer_db()
    number_of_customers = (cm.Customer.select().count())
    assert number_of_customers == 2

    bo.delete_customer("W54Hi66")

    current_number_of_customers = (cm.Customer.select().count())
    assert current_number_of_customers == 1

    drop_db()


def test_list_active_customers():
    create_customer_db()
    list_active_customers = cm.Customer.get(cm.Customer.customer_id == CUSTOMER_1['customer_id'])
    assert list_active_customers.status == 0

    drop_db()


#
# def test_update_customer_credit_limit_exists():
#     create_customer_db()
#
#     updated_customer = cm.Customer.get(cm.Customer.customer_id == 'W54Hi66')
#     assert updated_customer.credit_limit == 80.0
#
#     bo.update_customer_credit('W54Hi66', 801.0)
#
#     assert updated_customer.credit_limit == 801.0
#
#     drop_db()

def test_integration():
    # Add customer records
    create_customer_db()
    # bo.add_customer(**CUSTOMER_1)
    # bo.add_customer(**CUSTOMER_2)

    # Delete customer records
    bo.delete_customer(CUSTOMER_1["customer_id"])
    #
    # # Update customer credit limit record
    # bo.update_customer_credit("WHi32145", 500.0)
    #
    # update_customer = cm.Customer.get(cm.Customer.customer_id == "WHi32145")
    # assert update_customer.credit_limit == 500.0

    # Search customer records
    search_customer = bo.search_customer('WHi32145')
    assert search_customer['first_name'] == CUSTOMER_1['first_name']

    # # List active customers
    # assert bo.list_active_customers() == 1