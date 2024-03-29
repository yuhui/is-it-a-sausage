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

class ComputerVisionException(Exception):
    """Exception when the API returns an error.

    Attributes:
        message (str):
            The general error message to display when the error is raised.
        errors (list of str):
            (optional) Other messages that were part of the raised error.
    """
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
