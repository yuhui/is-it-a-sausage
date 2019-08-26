# Copyright (C) 2019 Yuhui
#
# Licensed under the MIT License (the "License"); you may not use this file
# except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
# Need to use `requests` because `azure-cognitiveservices-vision-computervision`
# does not support uploads.
#
# Reference:
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

from .exception import ComputerVisionException

ENDPOINT = 'insert-endpoint'
MS_COGNITIVE_VISION_KEY_1 = 'insert-key-1'
MS_COGNITIVE_VISION_KEY_2 = 'insert-key-2'
ANALYZE_ENDPOINT_PATH = '/vision/v2.0/analyze'
VISUAL_FEATURES = ['Adult', 'Tags']

class Client(object):
    """Client for interacting with Azure Cognitive Services.

    Attributes:
        key (str):
            ComputerVision key 1.
        endpoint (str):
            Azure Cognitive Services endpoint URL.
    """
    def __init__(self):
        self.key = MS_COGNITIVE_VISION_KEY_1
        self.endpoint = ENDPOINT

    def analyse_image(self, image_data):
        """Send image data to ComputerVision and return the identified tags
        and adult nature.

        Arguments:
            image_data (str):
                Binary string of the image.

        Returns:
            (dict) Image tags and whether it is of adult and racy nature.
            Keys: "image_tags", "is_adult_content", "is_racy_content".
        """
        url = self.endpoint + ANALYZE_ENDPOINT_PATH

        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            'Content-Type': 'application/octet-stream',
        }

        params = {
            'visualFeatures': ','.join(VISUAL_FEATURES),
        }

        response = requests.post(
            url,
            headers=headers,
            params=params,
            data=image_data,
        )

        response_json = response.json()
        if response.status_code != requests.codes['ok']:
            raise ComputerVisionException(
                response_json['message'],
                errors=response_json,
            )

        image_analysis = response_json

        adult_info = image_analysis['adult']
        is_adult_content = adult_info['isAdultContent']
        is_racy_content = adult_info['isRacyContent']

        image_tags = image_analysis['tags']
        if len(image_tags) is 0:
            raise ComputerVisionException('Failed to label the image.')

        return {
            'image_tags': image_tags,
            'is_adult_content': is_adult_content,
            'is_racy_content': is_racy_content,
        }
