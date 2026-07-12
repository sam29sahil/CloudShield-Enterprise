"""
CloudShield Enterprise
Settings Services
"""


class SettingsService:

    @staticmethod
    def profile(user):

        return {

            "username": user.username,

            "email": user.email

        }