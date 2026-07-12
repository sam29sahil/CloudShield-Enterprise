"""
CloudShield Enterprise
User Service
"""

from app.extensions import db
from app.models.user import User


class UserService:

    def all(self):
        """
        Return all users.
        """
        return User.query.all()

    def get(self, user_id):
        """
        Get user by ID.
        """
        return User.query.get(user_id)

    def get_by_username(self, username):
        """
        Get user by username.
        """
        return User.query.filter_by(
            username=username
        ).first()

    def get_by_email(self, email):
        """
        Get user by email.
        """
        return User.query.filter_by(
            email=email
        ).first()

    def create(
        self,
        username,
        email,
        password,
        role="User"
    ):
        """
        Create a new user.
        """

        user = User(
            username=username,
            email=email,
            password=password,
            role=role
        )

        db.session.add(user)
        db.session.commit()

        return user

    def update(
        self,
        user,
        username=None,
        email=None,
        role=None
    ):
        """
        Update user details.
        """

        if username is not None:
            user.username = username

        if email is not None:
            user.email = email

        if role is not None:
            user.role = role

        db.session.commit()

        return user

    def update_password(
        self,
        user,
        password
    ):
        """
        Update user password.
        """

        user.password = password

        db.session.commit()

        return user

    def delete(
        self,
        user_id
    ):
        """
        Delete user.
        """

        user = self.get(user_id)

        if not user:
            return None

        db.session.delete(user)
        db.session.commit()

        return True