"""Temp"""


import re


class Validator:
    """
    A validator class that verifies different formats including names, age,
    country, region, living place, index, phone number, email, and ID.
    """

    def validate_name_surname(self, name: str) -> bool:
        """
        Validates a full name consisting of a first and last name.

        :param name: The full name in "Firstname Lastname" format.
        :type name: str
        :return: True if the name is valid, False otherwise.
        :rtype: bool
        """
        return bool(re.fullmatch(r"[A-Z][a-z]{2,29} [A-Z][a-z]{2,29}", name))

    def validate_age(self, age: str) -> bool:
        """
        Validates an age between 16 and 99.

        :param age: The age as a string.
        :type age: str
        :return: True if the age is between 16 and 99, False otherwise.
        :rtype: bool
        """
        return bool(re.fullmatch(r"1[6-9]|[2-9]\d", age))

    def validate_country(self, country: str) -> bool:
        """
        Validates a country name (2-10 characters, either capitalized or uppercase like "USA").

        :param country: The country name.
        :type country: str
        :return: True if the country name is valid, False otherwise.
        :rtype: bool
        """
        return bool(re.fullmatch(r"[A-Z][a-z]{1,9}|[A-Z]{2,10}", country))

    def validate_region(self, region: str) -> bool:
        """
        Validates a region name (2-10 characters, may include numbers).

        :param region: The region name.
        :type region: str
        :return: True if the region name is valid, False otherwise.
        :rtype: bool
        """
        return bool(re.fullmatch(r"[A-Z][a-z\d]{1,9}", region))

    def validate_living_place(self, living_place: str) -> bool:
        """
        Validates a living place address in the format "StreetName st. 2a".

        :param living_place: The address, including street type and number.
        :type living_place: str
        :return: True if the address is valid, False otherwise.
        :rtype: bool
        """
        pattern = r"[A-Z][a-z]{2,19} (st\.|av\.|prosp\.|rd\.) \d[a-z\d]"
        return bool(re.fullmatch(pattern, living_place))

    def validate_index(self, index: str) -> bool:
        """
        Validates a postal index (exactly 5 digits).

        :param index: The postal code.
        :type index: str
        :return: True if the postal code is valid, False otherwise.
        :rtype: bool
        """
        return bool(re.fullmatch(r"\d{5}", index))

    def validate_phone(self, phone: str) -> bool:
        """
        Validates a phone number in formats "+380951234567" or "+38 (095) 123-45-67".

        :param phone: The phone number.
        :type phone: str
        :return: True if the phone number is valid, False otherwise.
        :rtype: bool
        """
        return bool(re.fullmatch(r"\+(\d{9,12}|\d{2} \(\d{3}\) \d{3}-\d{2}-\d{2})", phone))

    def validate_email(self, email: str) -> bool:
        """
        Validates an email address in the format "username@domain.type".

        :param email: The email address.
        :type email: str
        :return: True if the email format is valid, False otherwise.
        :rtype: bool
        """
        pattern = (r"[a-zA-Z\d!#$%&'*+/=?^_`{|}~]{1,64}"
                   r"(?:\.[a-zA-Z\d!#$%&'*+/=?^_`{|}~]+)*"
                   r"@[a-z\d.-]{1,255}\.(com|org|edu|gov|net|ua)")
        return bool(re.fullmatch(pattern, email))

    def validate_id(self, id_num: str) -> bool:
        """
        Validates an ID number (exactly 6 digits, containing exactly one zero).

        :param id_num: The ID number.
        :type id_num: str
        :return: True if the ID is valid, False otherwise.
        :rtype: bool
        """
        return bool(re.fullmatch(r"\d{6}", id_num)) and id_num.count("0") == 1

    def validate(self, data: str) -> bool:
        """
        Validates a full dataset string containing all required fields.

        :param data: A string containing name, age, country, region, living place,
                     index, phone, email, and ID, separated by commas or semicolons.
        :type data: str
        :return: True if all fields are valid, False otherwise.
        :rtype: bool
        """
        data = [i.strip() for i in re.split(r"[;,]", data)]

        if len(data) != 9:
            return False

        return (self.validate_name_surname(data[0]) and
                self.validate_age(data[1]) and
                self.validate_country(data[2]) and
                self.validate_region(data[3]) and
                self.validate_living_place(data[4]) and
                self.validate_index(data[5]) and
                self.validate_phone(data[6]) and
                self.validate_email(data[7]) and
                self.validate_id(data[8]))
