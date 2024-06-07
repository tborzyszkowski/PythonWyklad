import unittest
from unittest.mock import Mock

from my_service import MyService, Request
from single_sign_on import SSOToken, SingleSignOnRegistry


def confirm_token(correct_token):
    def is_valid(actual_token):
        if actual_token != correct_token:
            raise ValueError("wrong token received")

    return is_valid


class MyServiceTest(unittest.TestCase):
    def test_single_sign_on_receives_correct_token(self):
        mock_sso_registry = Mock(SingleSignOnRegistry)
        correct_token = SSOToken()
        mock_sso_registry.is_valid = Mock(side_effect=confirm_token(correct_token))
        service = MyService(mock_sso_registry)
        service.handle(Request("Emily"), correct_token)
        mock_sso_registry.is_valid.assert_called()

    def test_hello_name(self):
        stub_sso_registry = Mock(SingleSignOnRegistry)
        service = MyService(stub_sso_registry)
        response = service.handle(Request("Emily"), SSOToken())
        assert response.text == "Hello Emily!"

    def test_single_sign_on(self):
        spy_sso_registry = Mock(SingleSignOnRegistry)
        service = MyService(spy_sso_registry)
        token = SSOToken()
        service.handle(Request("Emily"), token)
        spy_sso_registry.is_valid.assert_called_with(token)

    def test_single_sign_on_with_invalid_token(self):
        spy_sso_registry = Mock(SingleSignOnRegistry)
        spy_sso_registry.is_valid.return_value = False
        service = MyService(spy_sso_registry)
        token = SSOToken()
        response = service.handle(Request("Emily"), token)
        spy_sso_registry.is_valid.assert_called_with(token)

    def test_single_sign_on_with_invalid_token_response_text(self):
        spy_sso_registry = Mock(SingleSignOnRegistry)
        spy_sso_registry.is_valid.return_value = False
        service = MyService(spy_sso_registry)
        token = SSOToken()
        response = service.handle(Request("Emily"), token)
        assert response.text == "Please sign in"
