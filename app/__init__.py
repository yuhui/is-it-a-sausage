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

name = 'is-it-a-sausage'
version = '1.0'
author = 'Yuhui'
author_email = 'yuhuibc@gmail.com'


from flask import Flask, current_app
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES, configure_uploads

from app.config import Config

bootstrap = Bootstrap()

images = UploadSet('images', IMAGES)

def create_app(config_class=Config):
    """Create a Flask app instance.

    Arguments:
        config_class (Config):
            Configuration parameters for the app.

    Returns:
        (Flask) a Flask app instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)

    configure_uploads(app, images)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.sausage import bp as sausage_bp
    app.register_blueprint(sausage_bp)

    return app
