# Venex API

Python backend API for fetching Venezuela currency exchange rates.

## Running the application

To run the application, you need to have Docker and Docker Compose installed.

1.  Create a `.env` file with the following content:

    ```
    APP_SUPABASE_URL=your_supabase_url
    APP_SUPABASE_API_KEY=your_supabase_api_key
    ```

2.  Run the application with the following command:

    ```
    docker-compose up -d
    ```

The application will be running at `http://localhost:8000`.

## API Endpoints

*   `/v1/health`: Health check endpoint.
*   `/v1/help`: Help endpoint.
