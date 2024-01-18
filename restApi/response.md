# API Overview

This API provides two endpoints for retrieving and importing electricity consumption data from a MongoDB database.

## Endpoints

### `/getKwh`

**Method:** GET

**Description:** Retrieves the electricity consumption for a specified day.

**Request Parameters:**

- `dia` (required): The day for which to retrieve consumption data. The day should be specified in the format YYYY-MM-DD.

**Response:**

- `msg`: A message indicating the retrieved consumption data.
- `kwh`: The electricity consumption for the specified day in kWh.

**Example Request:**

```
GET /getKwh?dia=2023-10-04
```

**Example Response:**

JSON

```
{
  "msg": "El dia 2023-10-04: 50.3 Kwh"
}
```

### `/importCSV`

**Method:** POST

**Description:** Imports electricity consumption data from a CSV file into the MongoDB database.

**Request Body:**

- `file`: A JSON object containing the path to the CSV file to be imported.

**Response:**

- `msg`: A message indicating the success of the import operation.

**Example Request Body:**

JSON

```
{
  "file": "data.csv"
}
```

**Example Response:**

JSON

```
{
  "msg": "Archivo CSV importado exitosamente"
}
```

Error Handling

The API returns error responses with the following codes:

- `400`: Bad request - Invalid request parameters.
- `404`: Not found - No data found for the specified day.
