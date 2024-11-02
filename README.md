# FastAPI Project

This is a FastAPI project that provides a RESTful API for performing CRUD operations on resources, leveraging FastAPI for backend handling and MongoDB for data storage. The application uses modular route files to organize HTTP requests and configuration settings for database connectivity.

## Project Structure

```
Fastapi tutorial/
│
├── app.py                # Main application file that initiates FastAPI app and includes route integrations
├── db_conn.py            # Database connection setup for MongoDB
├── config/
│   ├── config.ini        # Configuration file for database settings and other environment variables
│   └── config.py         # Python file for reading and parsing config.ini settings
├── routes/               # Folder containing individual route files for each CRUD operation
│   ├── delete.py         # DELETE route for resource deletion
│   ├── get_all.py        # GET route for retrieving all resources
│   ├── get_by_id.py      # GET route for retrieving a single resource by ID
│   ├── post.py           # POST route for creating a new resource
│   └── put.py            # PUT route for updating an existing resource
└── test_conn.py          # Testing script to check database connection
└── README.md             # Project documentation
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository_url>
cd Fastapi tutorial
```

### 2. Install Dependencies

Make sure you have Python installed. Then, install the required packages:

```bash
pip install fastapi uvicorn pymongo python-dotenv
```

### 3. Set Up Database Connection

1. Update the `config/config.ini` file with your MongoDB credentials:
   ```ini
   [mongodb]
   uri = mongodb://<username>:<password>@localhost:27017
   db_name = your_database_name
   collection_name = your_collection_name
   ```

2. The database connection is handled in `db_conn.py` with a `conn_db` function, which returns database and collection objects for CRUD operations.

## Usage

### Running the Application

Use Uvicorn to start the FastAPI server:

```bash
uvicorn app:app --reload
```

### Endpoints

The application provides the following endpoints:

- **Create a Resource**  
  - **POST** `/create`  
  - **Description:** Creates a new resource with provided JSON data.
  - **File:** `routes/post.py`

- **Get All Resources**  
  - **GET** `/get_all`  
  - **Description:** Fetches all resources from the database.
  - **File:** `routes/get_all.py`

- **Get Resource by ID**  
  - **GET** `/get/{id}`  
  - **Description:** Fetches a resource by its unique identifier.
  - **File:** `routes/get_by_id.py`

- **Update a Resource**  
  - **PUT** `/update/{id}`  
  - **Description:** Updates the fields of a resource identified by its ID with provided JSON data.
  - **File:** `routes/put.py`

- **Delete a Resource**  
  - **DELETE** `/delete/{id}`  
  - **Description:** Deletes a resource identified by its ID.
  - **File:** `routes/delete.py`

### Testing the Database Connection

To verify the database connection, run the `test_conn.py` script:

```bash
python test_conn.py
```

## Contributing

Contributions are welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Implement and test your changes.
4. Commit and push your changes to your fork.
5. Open a pull request for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
