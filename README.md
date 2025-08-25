# Venex API

Python backend API for fetching Venezuela currency exchange rates.

## Features

*   Fetches exchange rates from various sources.
*   Provides a RESTful API to consume the data.

## Technologies

*   Python 3.12
*   FastAPI
*   Supabase

## Running the application

To run the application, you need to have Python 3.12 installed.

1.  Create a `.env` file with the following content:

    ```
    APP_SUPABASE_URL=your_supabase_url
    APP_SUPABASE_API_KEY=your_supabase_api_key
    ```

2.  Run the application with the following command:

    ```
    uvicorn app.main:app --reload
    ```

The application will be running at `http://localhost:8000`.

## API Endpoints

*   `/v1/help/`: Health check endpoint.
*   `/v1/help/status/db`: Database status endpoint (development only).
*   `/v1/rates/binance`: Get Binance rates.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
