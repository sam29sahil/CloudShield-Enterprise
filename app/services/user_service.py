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
<<<<<<< HEAD
        return User.query.filter_by(username=username).first()
=======
        return User.query.filter_by(
            username=username
        ).first()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def get_by_email(self, email):
        """
        Get user by email.
        """
<<<<<<< HEAD
        return User.query.filter_by(email=email).first()

    def create(self, username, email, password, role="User"):
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        """
        Create a new user.
        """

<<<<<<< HEAD
        user = User(username=username, email=email, password=password, role=role)
=======
        user = User(
            username=username,
            email=email,
            password=password,
            role=role
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        db.session.add(user)
        db.session.commit()

        return user

<<<<<<< HEAD
    def update(self, user, username=None, email=None, role=None):
=======
    def update(
        self,
        user,
        username=None,
        email=None,
        role=None
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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

<<<<<<< HEAD
    def update_password(self, user, password):
=======
    def update_password(
        self,
        user,
        password
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        """
        Update user password.
        """

        user.password = password

        db.session.commit()

        return user

<<<<<<< HEAD
    def delete(self, user_id):
=======
    def delete(
        self,
        user_id
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        """
        Delete user.
        """

        user = self.get(user_id)

        if not user:
            return None

        db.session.delete(user)
        db.session.commit()

<<<<<<< HEAD
        return True
=======
        return True
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
