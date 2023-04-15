import requests
import multiprocessing

http_status_codes = [200, 301, 403, 404, 500]

default_input_file = 'subdomains.txt'
default_output_files = {
    200: '200_OK.txt',
    301: '301_MovedPermanently.txt',
    403: '403_Forbidden.txt',
    404: '404_NotFound.txt',
    500: '500_InternalServerError.txt'
}

input_file = input(f"Enter input file name (default: {default_input_file}): ") or default_input_file


output_files = {}
for status_code in http_status_codes:
    default_output_file = default_output_files[status_code]
    output_file = input(f"Enter output file name for status code {status_code} (default: {default_output_file}): ") or default_output_file
    output_files[status_code] = output_file


def check_subdomain(subdomain):
    url = f'http://{subdomain}'
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        status_code = response.status_code
        print(f'{subdomain}: {status_code}')
    except:
        status_code = 500  # Set status code to 500 if there's an error with the request
        print(f'{subdomain}: {status_code}')

    if status_code in output_files:
        with open(output_files[status_code], 'a') as f:
            f.write(subdomain + '\n')


with open(input_file) as f:
    subdomains = f.read().splitlines()

pool = multiprocessing.Pool()
pool.map(check_subdomain, subdomains)
pool.close()
pool.join()

