from ..usecase import usecase
import requests


def error_response(response):
    """
    Raises errors matching the response code
    """
    pass


class MapClient():

    def __init__(self, YOUR_CLIENT_ID: str) -> None:
        self.CLIENT_ID = YOUR_CLIENT_ID
        self.BASE_DOMAIN = 'https://a.mapillary.com/v3/map_features'

    def trafficinfo(self, lowerbbox: list, upperbbox: list,
                    perpage: int = 1, value=None):
        bbox_list = [*lowerbbox[::-1], *upperbbox[::-1]]
        bbox = (','.join([repr(point) for point in bbox_list]))
        if value:
            params = '?layers=trafficsigns&bbox={}&value={}&per_page={}&\
                     client_id={}'.format(bbox, value, perpage, self.CLIENT_ID)
        else:
            params = '?layers=trafficsigns&bbox={}&per_page={}&\
                     client_id={}'.format(bbox, perpage, self.CLIENT_ID)
        complete_url = self.BASE_DOMAIN + params
        response = requests.get(complete_url)
        if response.status_code != 200:
            return error_response(response)
        json_dict = response.json()
        transform_json = usecase.Properties()
        transform_json.transform_json_(json_dict)
