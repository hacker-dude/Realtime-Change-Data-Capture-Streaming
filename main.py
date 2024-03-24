# Import necessary libraries
import faker  # Library for generating fake data
import psycopg2  # Library for interacting with PostgreSQL database
from datetime import datetime, timezone  # Library for datetime operations
import random  # Library for generating random numbers

# Instantiate a Faker object for generating fake data
fake = faker.Faker()


def generate_transaction():
    """
    Generates a fake financial transaction.

    Returns:
        dict: A dictionary containing details of the transaction.
    """
    # Generate a fake user profile
    user = fake.simple_profile()

    # Create a transaction dictionary with fake details
    return {
        "transactionId": fake.uuid4(),
        "userId": user["username"],
        "timestamp": datetime.now(timezone.utc).timestamp(),
        "amount": round(random.uniform(10, 1000), 2),
        "currency": random.choice(["USD", "GBP"]),
        "city": fake.city(),
        "country": fake.country(),
        "merchantName": fake.company(),
        "paymentMethod": random.choice(
            ["credit_card", "debit_card", "online_transfer"]
        ),
        "ipAddress": fake.ipv4(),
        "voucherCode": random.choice(["", "DISCOUNT10", ""]),
        "affiliateId": fake.uuid4(),
    }


def create_table(conn):
    """
    Creates a transactions table in the database if it doesn't exist.

    Args:
        conn: Connection object to the PostgreSQL database.
    """
    cursor = conn.cursor()

    # Execute SQL command to create table if not exists
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id VARCHAR(255) PRIMARY KEY,
            user_id VARCHAR(255),
            timestamp TIMESTAMP,
            amount DECIMAL,
            currency VARCHAR(255),
            city VARCHAR(255),
            country VARCHAR(255),
            merchant_name VARCHAR(255),
            payment_method VARCHAR(255),
            ip_address VARCHAR(255),
            voucher_code VARCHAR(255),
            affiliateId VARCHAR(255)
        )
        """
    )

    # Close cursor
    cursor.close()

    # Commit transaction
    conn.commit()


if __name__ == "__main__":
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        database="financials_db",
        user="postgres",
        password="postgres",
        port=5432,
    )

    # Create transactions table
    create_table(conn)

    # Generate a fake transaction
    transaction = generate_transaction()

    # Open a cursor
    cur = conn.cursor()

    # Print the generated transaction
    print(transaction)

    # Execute SQL command to insert transaction into the database
    cur.execute(
        """
        INSERT INTO transactions(transaction_id, user_id, timestamp, amount, currency, city, country, merchant_name, payment_method, 
        ip_address, affiliateId, voucher_code)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            transaction["transactionId"],
            transaction["userId"],
            datetime.fromtimestamp(transaction["timestamp"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            transaction["amount"],
            transaction["currency"],
            transaction["city"],
            transaction["country"],
            transaction["merchantName"],
            transaction["paymentMethod"],
            transaction["ipAddress"],
            transaction["affiliateId"],
            transaction["voucherCode"],
        ),
    )

    # Close cursor
    cur.close()

    # Commit transaction
    conn.commit()
