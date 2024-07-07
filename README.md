# Biognosys Interview Assignment

## Scaling considerations

### Handling large datasets

- Utilizing the Pandas library is highly efficient for data loading and manipulation. To optimize performance with large files, we could consider reading data in smaller chunks to reduce memory consumption.
- Implementing caching mechanisms to reduce repetitive computations is also a good approach when handling large datasets.
- For long-term scalability, consider storing the data in a data warehouse (e.g., Snowflake, BigQuery, Databricks). Then, use an asynchronous process in another application (microservice) to convert into a user-friendly format, and stroing it in a SQL or NoSQL databases, in order to improve query performance during concurrent user requests.

### Concurrency

- Using a Web Server Gateway Interface (WSGI) like Gunicorn or Waitress to handle concurrent users effectively. These WSGI servers manage multiple worker processes to handle multiple requests concurrently, improving the application's ability to serve many users simultaneously.
- Implement asynchronous processing for handling multiple operations simultaneously. It allows the API to perform I/O operations like reading data from disk or making network requests without blocking the execution of other operations, making it better at handling more requests concurrently, being more responsive and scalable.
- For database connections and queries, use a database with connection pooling capabilities (a pool of database connections that can be reused by multiple requests, reducing the overhead of creating a new connection for each request) to ensure efficient and fast access to the database, even under high load.
- Scale the application horizontally by adding more servers and using a load balancer.

## Reasons for choosing Flask

- Flask allows rapid API development without unnecessary overhead.
- Integrates well with scientific computing libraries like Pandas, SciPy, or NumPy, which are essential for data processing tasks.
- Flask has clear and simple documentation.
- If our approach involves building an asynchronous application, FastAPI would be a suitable choice. FastAPI is built on top of Starlette, a lightweight ASGI framework designed for creating asynchronous web applications. This framework enhances performance and capability in handling high-throughput, asynchronous tasks compared to Flask. This can be particularly advantageous in applications where users frequently import large volumes of data to the cloud, allowing the application to continue running without blocking for each user's data processing.

## Other possible improvements

- For this assignment, I developed the API thinking it would be used in a production environment, with  constantly changing data,  which is why the data processing specific to each endpoint is performed when the endpoint is called. In the particular case of this assignment, where we are reading a static Excel file, we could improve the performance of the app by computing all the data processing when the Flask application is started. This way, when each endpoint is called, we would only retrieve the data, not needing to perform the computations again.


## Instructions to run locally
**Using bash**:
1. **Clone the repository**:
- git clone https://github.com/JoseGuilhermeGois/BiognosysAssignment.git
- cd 'your-repository-directory'

2. **Set up a Virtual Environment**:    # Not necessary but recommended
- python -m venv my-venv
- . my-venv/Scripts/activate      # on Windows
- source my-venv/bin/activate     # on Unix or MacOS

3. **Install dependencies**:
- pip install -r requirements.txt
- Note: You need Python 3.10 to run this SciPy version. If you have an older Python version, you can install SciPy 1.13.1.

4. **Run Flask application**:
- python app.py

5. **Access the endpoints**:

- **Using the web browser**:
- http://localhost:8080/ : Check if the app is running and find the hyperlinks to the 3 endpoints.
- http://localhost:8080/proteins-per-sample : Endpoint for aggregated number of proteins per sample.
- http://localhost:8080/peptides-per-sample : Endpoint for aggregated number of peptides per sample.
- http://localhost:8080/statistical-test : Endpoint for performing a statistical test.

- **Using the command line**:
- curl http://127.0.0.1:8080/ : Check if the app is running and find the hyperlinks to the 3 endpoints.
- curl http://127.0.0.1:8080/proteins-per-sample : Endpoint for aggregated number of proteins per sample.
- curl http://127.0.0.1:8080/peptides-per-sample : Endpoint for aggregated number of peptides per sample.
- curl http://127.0.0.1:8080/statistical-test : Endpoint for performing a statistical test.
