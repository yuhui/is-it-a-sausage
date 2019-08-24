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

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from app import images

class SausageForm(FlaskForm):
    """Form specification for receiving an image upload and label."""
    image_file = FileField(
        'JPEG Image',
        validators=[
            FileRequired(),
            FileAllowed(images, 'Images only!'),
        ],
    )
    human_guess = StringField(
        'What I think the image shows',
        validators=[DataRequired()],
    )
    submit = SubmitField('Submit')
