# FastAPI Project

This is a FastAPI project that provides a RESTful API for updating resources.

## Installation

1. Clone the repository:

2. Install the dependencies:

3. Set up the database connection:

- Create a `db_conn.py` file in the project root directory
- Define a `conn_db` function in `db_conn.py` that returns a `database` and `collection` object

## Usage

1. Run the FastAPI application:

2. Make a PUT request to the `/update/{id}` endpoint, replacing `{id}` with the ID of the resource you want to update.

The request body should be a JSON object with the fields you want to update. The response will be a JSON object with a success message.

## Contributing

Contributions are welcome! Please follow these guidelines:

- Fork the repository
- Create a new branch for your changes
- Make your changes
- Commit your changes
- Push your changes to your fork
- Create a pull request

## License

This project is licensed under the [MIT License](LICENSE).