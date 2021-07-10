import random


class DataManager:
    def __init__(self, load_data=True) -> None:
        self._names: list[str] = []
        self._casts: list[str] = []

        if load_data:
            self.load_data()

    # UTILS !!
    @staticmethod
    def read_file(filepath) -> str:
        with open(filepath, "r") as file:
            return file.read()

    # PROPERTIES !!
    @property
    def names(self) -> list[str]:
        self.load_names()
        return self._names

    @property
    def casts(self) -> list[str]:
        self.load_casts()
        return self._casts

    @property
    def random_name(self) -> str:
        self.load_names()
        return random.choice(self._names)

    @property
    def random_cast(self) -> str:
        self.load_casts()
        return random.choice(self._casts)

    @property
    def random_full_name(self) -> str:
        return f"{self.random_name} {self.random_cast}"

    @property
    def random_email(self) -> str:
        return f"{self.random_name}.{self.random_cast}@gmail.com".lower()

    @property
    def random_phone_number(self) -> str:
        return str(random.randint(9800000000, 9899999999))

    # DYNAMIC DATA !!
    def get_random_password(self, name=None, cast=None, phone_number=None):
        name = name or self.random_name
        cast = cast or self.random_cast
        phone_number = phone_number or self.random_phone_number

        prefixes = [""]
        postfixes = [""]
        prefix = random.choice(prefixes)
        postfix = random.choice(postfixes)

        password_generators = [
            lambda: f"{prefix}{name}{postfix}",
            lambda: f"{name}{postfix}@{random.randint(1, 999)}",
            lambda: f"{cast}@{phone_number[:5]}",
            lambda: f"{name}@{phone_number[:5]}",
        ]

        if random.choice([True, False]):
            return random.choice(password_generators)().lower()
        else:
            return random.choice(password_generators)()

    def get_random_email(self, name=None, cast=None, phone_number=None, domain=None) -> str:
        name = name or self.random_name
        cast = cast or self.random_cast
        phone_number = phone_number or self.random_phone_number
        domain = domain or "gmail.com"

        chars = ["."]
        char = random.choice(chars)

        prefixes = ["", f"cool{char}", f"don{char}", f"hacker{char}", f"pubgmaster{char}"]
        postfixes = [""]
        prefix = random.choice(prefixes)
        postfix = random.choice(postfixes)

        email_generators = [
            lambda: f"{prefix}{name}{char}{cast}{postfix}@{domain}",
            lambda: f"{prefix}{name}{char}{cast}{char}{postfix}{random.randint(1, 999)}@{domain}",

            lambda: f"{prefix}{cast}{char}{name}{postfix}@{domain}",
            lambda: f"{prefix}{cast}{char}{name}{char}{postfix}{random.randint(1, 999)}@{domain}",

            lambda: f"{prefix}{name}{char}{postfix}{phone_number[:random.randint(1, 5)]}@{domain}",
        ]

        return random.choice(email_generators)().lower()

    # HELPER !!
    def load_names(self):
        if not self._names:
            self._names = list(
                set(
                    name.strip() for name in
                    self.read_file(
                        "./extras/names/nepali_names.txt"
                    ).split("\n") if name.strip()
                )
            )

    def load_casts(self):
        if not self._casts:
            self._casts = list(
                set(
                    surname.strip() for surname in
                    self.read_file(
                        "./extras/names/nepali_surnames.txt"
                    ).split("\n") if surname.strip()
                )
            )

    def load_data(self):
        self.load_names()
        self.load_casts()
