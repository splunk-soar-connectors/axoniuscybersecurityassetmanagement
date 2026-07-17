from pathlib import Path


CONNECTOR_SOURCE = Path("axoniuscybersecurityassetmanagement_connector.py").read_text()
MANIFEST_SOURCE = Path("axoniuscybersecurityassetmanagement.json").read_text()


def test_server_certificate_verification_defaults_to_enabled():
    assert '"verify_server_cert"' in MANIFEST_SOURCE
    assert '"default": true' in MANIFEST_SOURCE
    assert 'config.get(VERIFY_SERVER_CERT_KEY, True)' in CONNECTOR_SOURCE


def test_platform_ca_bundle_is_not_removed():
    assert 'os.environ.pop("REQUESTS_CA_BUNDLE"' not in CONNECTOR_SOURCE
