from decimal import Decimal
import random
from faker import Faker

from models.account import Account
from models.customer import Customer


def seed_database(db):
    if not db.session.query(Customer).first():
        print("Seeding!")
        min_amount = 0
        max_amount = 10**5  # 10^5
        customers: list[Customer] = []
        fake = Faker("sv_SE")
        for _ in range(10):
            new_customer = Customer(
                name=fake.name(),
                email=fake.unique.email(),
                address=fake.address(),
                city=fake.city(),
                date_of_birth=fake.date_of_birth(),
                accounts=[
                    Account(balance=Decimal(random.randrange(min_amount, max_amount))),
                    Account(balance=Decimal(random.randrange(min_amount, max_amount))),
                ],
            )

            if random.random() > 0.5:
                new_customer.telephone = fake.phone_number()
                new_customer.secondary_address = fake.address()
                new_customer.national_id = fake.ssn()

            customers.append(new_customer)
        db.session.add_all(customers)
        db.session.commit()
    else:
        print("Seeding already done!")
