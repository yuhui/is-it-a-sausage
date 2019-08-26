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

import base64

from flask import render_template, request, current_app

from app.sausage import bp
from app.sausage.forms import SausageForm

from azure_modules.computervision.client import Client
from azure_modules.computervision.exception import ComputerVisionException

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    """Controller for the homepage.

    If a form has been uploaded, then show:
        - the image (if it's not of an adult nature)
        - what the user guessed the image contains
        - what ComputerVision identified in the image

    Then, show the form to accept the user's image and label.
    """
    image_src = None
    human_label = None
    image_analysis = None

    sausage_form = SausageForm()
    if sausage_form.validate_on_submit():
        image_file = request.files['image_file']
        image_mimetype = image_file.mimetype
        image_data = image_file.read()

        human_label = sausage_form.human_label.data

        # display the image using its binary data
        # so that the image itself does not need to be saved
        image_src = 'data:{};base64,{}'.format(
            image_mimetype,
            base64.b64encode(image_data).decode(),
        )

        try:
            computer_vision_client = Client()
            image_analysis = computer_vision_client.analyse_image(image_data)

            # convert the float confidences to (integer) percentage confidences
            image_analysis['image_tags'] = [
                {'name': t['name'], 'confidence': int(t['confidence'] * 100)} \
                    for t in image_analysis['image_tags']
            ]
        except ComputerVisionException as e:
            image_analysis = {
                'error_message': e,
            }

    return render_template(
        'index.html',
        sausage_form=sausage_form,
        image_src=image_src,
        human_label=human_label,
        image_analysis=image_analysis,
    )
