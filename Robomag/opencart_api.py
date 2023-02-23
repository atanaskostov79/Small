import requests


class OpenCartAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get(self, endpoint):
        """
        Makes a GET request to the specified OpenCart API endpoint with REST Admin authentication.

        Args:
            endpoint (str): The API endpoint to request.

        Returns:
            dict: The JSON response from the API.
        """
        url = self.base_url + endpoint
        headers = {'X-Oc-Restadmin-Id': self.api_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_categories(self):
        """
        Returns a list of categories from the OpenCart API.

        Returns:
            list: A list of category dictionaries.
        """
        endpoint = 'categories'
        response = self.get(endpoint)
        categories = response['data']
        return categories
