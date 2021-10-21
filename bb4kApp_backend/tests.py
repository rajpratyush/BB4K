from django.test import TestCase
from django.test import SimpleTestCase
from .models import KidModel, ParentModel

# Create your tests here.

class SimpleTestCase():
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class PostModelTest(TestCase):

    def setUp(self):
        KidModel.object.create(name="Testing")
        ParentModel.object.create(name="Testing")


    def test_name_content(self):
        kid_name = KidModel.object.get(id=1)
        parent_name = ParentModel.object.get(id=1)

        expected_object_kidname= f"{kid_name.name}"
        assertEqual(expected_object_kidname, "Testing")


        expected_object_parentname = f"{parent_name.name}"
        assertEqual(expected_object_,parentname "Testing")

