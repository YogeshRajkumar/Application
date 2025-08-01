from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import MenuItem, Booking

class MenuBookingTestCase(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_menu_item(self):
        """Test creating a menu item."""
        data = {"title": "Pasta", "price": "15.50", "inventory": 10}
        response = self.client.post("/api/menu/", data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(MenuItem.objects.count(), 1)

    def test_create_booking(self):
        """Test creating a booking."""
        data = {"name": "John Doe", "no_of_guests": 4, "booking_date": "2025-08-10"}
        response = self.client.post("/api/bookings/", data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)
