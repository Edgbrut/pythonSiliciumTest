import pytest
import allure
from pages.registration_page import Student_registration_page


@pytest.mark.usefixtures("set_up")
class TestRegistrationPage:

    @allure.description("Test Student Registration Form")
    def test_registration_page(self, set_group):

        # Launching Browser And Opening Demoqa Practice Form

        # Submit Student Registration Form
        rp = Student_registration_page(self.driver)
        rp.submit_application()
        print("Thanks for submitting the form!")
