from django.test import TestCase
from django.contrib.auth.models import User as DjangoUser
from .models import User, Estate_Associate, ADMIN
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError


class UserModelTest(TestCase):
    def setUp(self):
        self.django_user = DjangoUser.objects.create_user(
            username="Alinemutesi", password="testpassword1563"
        )

        self.user = User.objects.create(
            user=self.django_user,
            first_name="Mutesi",
            last_name="Aline",
            phone_number="1234567890",
            email="alinemutesi@gmail.com",
            password="testpassword",
            role=Estate_Associate,
        )

    def test_user_creation(self):
        self.assertEqual(self.user.first_name, "Mutesi")
        self.assertEqual(self.user.last_name, "Aline")
        self.assertEqual(self.user.phone_number, "1234567890")
        self.assertEqual(self.user.email, "alinemutesi@gmail.com")
        self.assertEqual(self.user.role, Estate_Associate)

    def test_default_role(self):
        self.assertEqual(self.user.role, Estate_Associate)

    def test_role_choices(self):
        self.user.role = ADMIN
        self.user.save()
        self.assertEqual(self.user.role, ADMIN)

    def test_str_representation(self):
        self.assertEqual(str(self.user), "Mutesi Aline (alinemutesi@gmail.com)")

    def test_unique_email(self):
        with self.assertRaises(IntegrityError):
            User.objects.create(
                user=self.django_user,
                first_name="linet",
                last_name="mkandoe",
                phone_number="0987654321",
                email="alinemutesi@gmail.com",
                password="linet56678",
                role=Estate_Associate,
            )

    def test_missing_email(self):
        with self.assertRaises(ValidationError):
            user = User(
                user=self.django_user,
                first_name="Nyabang",
                last_name="Wech",
                phone_number="1234567890",
                password="testpassword200366",
                role=Estate_Associate,
            )
            user.full_clean()

    def test_missing_role(self):
        with self.assertRaises(ValidationError):
            user = User(
                user=self.django_user,
                first_name="Nyabang",
                last_name="wech",
                phone_number="1234567890",
                email="nyabangwech@gmail.com",
                password="testpassword200366",
            )
            user.full_clean()

    def test_invalid_role(self):
        with self.assertRaises(ValidationError):
            user = User(
                user=self.django_user,
                first_name="Nyabang",
                last_name="wech",
                phone_number="1234567890",
                email="nyabangwech@gmail.com",
                password="testpassword200366",
                role="invalid_role",
            )
            user.full_clean()

    def test_long_phone_number(self):
        with self.assertRaises(ValidationError):
            user = User(
                user=self.django_user,
                first_name="Nyabang",
                last_name="wech",
                phone_number="1" * 21,
                email="nyabangwech@gmail.com",
                password="testpassword200366",
                role=Estate_Associate,
            )
            user.full_clean()

    def test_long_password(self):
        with self.assertRaises(ValidationError):
            user = User(
                user=self.django_user,
                first_name="Nyabang",
                last_name="Wech",
                phone_number="1234567890",
                email="nyabangwech@gmail.com",
                password="p" * 201,
                role=Estate_Associate,
            )
            user.full_clean()
