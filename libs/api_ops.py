"""
THIS TECHNICAL CLASS COVERS API OPERATIONS
Author: Chinmay Mudholkar
Date: 04/2024
"""

import requests


class api_operations:
    def api_get(
        self,
        endpoint: str,
        headers: dict = None,
        params: dict = None,
        body: dict = None,
    ):
        response = None
        try:
            options = {}
            if headers is not None:
                options["headers"] = headers

            if params is not None:
                options["params"] = params

            if body is not None:
                options["json"] = body

            response = requests.get(url=endpoint, **options)
        except Exception as e:
            print(f"An error occurred: {e}")
            response = None
        finally:
            return response

    def api_post(
        self,
        endpoint: str,
        headers: dict = None,
        params: dict = None,
        body: dict = None,
    ):
        response = None
        try:
            options = {}
            if headers is not None:
                options["headers"] = headers

            if params is not None:
                options["params"] = params

            if body is not None:
                options["json"] = body

            response = requests.post(url=endpoint, **options)
        except Exception as e:
            print(f"An error occurred: {e}")
            response = None
        finally:
            return response

    def api_delete(
        self,
        endpoint: str,
        headers: dict = None,
        params: dict = None,
        body: dict = None,
    ):
        response = None
        try:
            options = {}
            if headers is not None:
                options["headers"] = headers

            if params is not None:
                options["params"] = params

            if body is not None:
                options["json"] = body

            response = requests.delete(url=endpoint, **options)
        except Exception as e:
            print(f"An error occurred: {e}")
            response = None
        finally:
            return response

    def api_put(
        self,
        endpoint: str,
        headers: dict = None,
        params: dict = None,
        body: dict = None,
    ):
        response = None
        try:
            options = {}
            if headers is not None:
                options["headers"] = headers

            if params is not None:
                options["params"] = params

            if body is not None:
                options["json"] = body

            response = requests.put(url=endpoint, **options)
        except Exception as e:
            print(f"An error occurred: {e}")
            response = None
        finally:
            return response

    def api_patch(
        self,
        endpoint: str,
        headers: dict = None,
        params: dict = None,
        body: dict = None,
    ):
        response = None
        try:
            options = {}
            if headers is not None:
                options["headers"] = headers

            if params is not None:
                options["params"] = params

            if body is not None:
                options["json"] = body

            response = requests.put(url=endpoint, **options)
        except Exception as e:
            print(f"An error occurred: {e}")
            response = None
        finally:
            return response
