Change Data Capture (CDC) with Debezium, Kafka, Postgres Docker Setup
=====================================================================

This project demonstrates setting up a Change Data Capture (CDC) pipeline using Debezium, Kafka, and PostgreSQL within Docker containers. CDC is a method used to track and capture changes in a database and propagate them to other systems in real-time.

Setup Instructions
------------------

1.  Clone this repository.
2.  Navigate to the project directory.
3.  Run `docker-compose up -d` to start all services in detached mode.

Components
----------

-   Zookeeper: Coordination service for Kafka.
-   Kafka Broker: Messaging backbone.
-   Control Center: Web-based GUI for monitoring Kafka clusters.
-   Debezium: Distributed platform for change data capture.
-   Debezium UI: Graphical interface for managing Debezium connectors.
-   PostgreSQL: Source database for capturing changes.

Usage
-----

1.  After starting the services, access Control Center at `http://localhost:9021` and Debezium UI at `http://localhost:8080` in your browser.
2.  Set up Debezium connectors to capture changes from PostgreSQL database tables.
3.  Execute the Python script `main.py` to add the initial transaction to the PostgreSQL database. Ensure that the script is executed after the PostgreSQL container is fully initialized and ready to accept connections.
4.  Apply the SQL scripts from the `scripts.sql` to the PostgreSQL database. This script adds additional columns to the transactions table, configures Debezium to capture before records, and creates a trigger function to capture changes to specific columns into a JSON object.

    `python main.py`

Additional Notes
----------------

-   This setup uses Docker Compose for easy deployment and management of containers.
-   Ensure proper network configuration (`dev-net`) for communication between services.

Feel free to contribute or report any issues encountered.