"""
Provides basic request.
"""

import requests


def fields_generator(fields: list[str]) -> str:
    """Generate fields"""
    return f'fields {",".join(fields)};'


def abstract_request(base_url: str, headers: dict[str, str]):
    """return a function which is applied with base_url and headers"""
    def endpoint_request(end_point: str, fields: list[str], id_array: list[int]):
        if isinstance(id_array, int):
            return requests.post(f'{base_url}/{end_point}', headers=headers, data=f'{fields_generator(fields)} where id={id_array};').json()[0]
        else:
            urls = [requests.post(f'{base_url}/{end_point}', headers=headers,
                                  data=f'{fields_generator(fields)} where id={id};').json()[0] for id in id_array]
            return urls
    return endpoint_request
