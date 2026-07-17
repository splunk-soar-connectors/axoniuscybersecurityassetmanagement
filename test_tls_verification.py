# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pathlib import Path


CONNECTOR_SOURCE = Path("axoniuscybersecurityassetmanagement_connector.py").read_text()
MANIFEST_SOURCE = Path("axoniuscybersecurityassetmanagement.json").read_text()


def test_server_certificate_verification_defaults_to_enabled():
    assert '"verify_server_cert"' in MANIFEST_SOURCE
    assert '"default": true' in MANIFEST_SOURCE
    assert "config.get(VERIFY_SERVER_CERT_KEY, True)" in CONNECTOR_SOURCE


def test_platform_ca_bundle_is_not_removed():
    assert 'os.environ.pop("REQUESTS_CA_BUNDLE"' not in CONNECTOR_SOURCE
