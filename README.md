# HTTP Status Code Checker

This script checks the HTTP status codes of a list of subdomains and saves the results to different files based on the status codes.

## Requirements

* Python 3.x
* requests library
* multiprocessing library

## Usage

1. Clone the repository:

    ```
    git clone https://github.com/M4fiaB0y/HTTP-status-codes-.git
    ```

2. Install the required libraries:

    ```
    pip install -r requirements.txt
    ```

3. Prepare a file containing a list of subdomains, with each subdomain on a new line.

4. Run the script:

    ```
    python status.py
    ```

5. When prompted, enter the name of the file containing the subdomains.

6. The script will start processing the subdomains and output the HTTP status codes to the console.

7. The script will also save the subdomains to different files based on the HTTP status codes.

## Output

* 200_OK.txt - Subdomains with HTTP status code 200 (OK)
* 301_MovedPermanently.txt - Subdomains with HTTP status code 301 (Moved Permanently)
* 403_Forbidden.txt - Subdomains with HTTP status code 403 (Forbidden)
* 404_NotFound.txt - Subdomains with HTTP status code 404 (Not Found)
* 500_InternalServerError.txt - Subdomains with HTTP status code 500 (Internal Server Error)

## Example

Suppose you have a file named `subdomains.txt` with the following content:

