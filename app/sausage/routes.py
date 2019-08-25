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
    sausage_form = SausageForm()
    if sausage_form.validate_on_submit():
        image_file = request.files['image_file']
        image_mimetype = image_file.mimetype
        image_data = image_file.read()


        computer_vision_client = Client()
        image_analysis = computer_vision_client.analyse_image(image_data)
        human_label = sausage_form.human_label.data

        image_result = {
            'image_tag': image_analysis['image_tag'],
            'is_adult_content': image_analysis['is_adult_content'],
            'is_racy_content': image_analysis['is_racy_content'],
            'human_label': human_label,
            'image_src': 'data:{};base64,{}'.format(
                image_mimetype,
                base64.b64encode(image_data).decode(),
            )
        }
    else:
        image_result = None

    return render_template(
        'index.html',
        sausage_form=sausage_form,
        image_result=image_result,
    )
