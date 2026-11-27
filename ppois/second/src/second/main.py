import datetime
from enum import Enum


class TourCompanyException(Exception):
    """Base exception for the whole system."""


class TransportException(TourCompanyException):
    """Problems with transport (cancelled flight, breakdown)."""


class InsufficientFundsException(TourCompanyException):
    """Client does not have enough money."""


class InvalidClientDataException(TourCompanyException):
    """Incorrect client data (age, passport)."""


class BookingNotFoundException(TourCompanyException):
    """Booking not found in the database."""


class InvalidBookingDataException(TourCompanyException):
    """Incorrect booking data (date in the past, etc.)."""


class InvalidBaggageDataException(TourCompanyException):
    """Problems with baggage data (forbidden items)."""


class BaggageOverweightException(TourCompanyException):
    """Exceeded baggage weight limit."""


class VehicleOverloadException(TourCompanyException):
    """Transport is overloaded (more people than seats)."""


class VehicleNotAvailableException(TourCompanyException):
    """Transport is unavailable (under repair, booked)."""


class GuideNotAvailableException(TourCompanyException):
    """Guide is unavailable (busy, sick)."""


class InvalidVisaException(TourCompanyException):
    """Visa problems (missing, expired)."""


class HotelFullyBookedException(TourCompanyException):
    """Hotel is fully booked."""


class TransportType(Enum):
    BUS = "Автобус"
    AIRPLANE = "Самолет"
    TRAIN = "Поезд"
    SHIP = "Круизный лайнер"


class RoomType(Enum):
    STANDARD = "Стандарт"
    LUXURY = "Люкс"
    SUITE = "Апартаменты"


class PaymentMethod(Enum):
    CASH = "Наличные"
    CARD = "Карта"


class Person:
    """Base class representing a human."""

    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def introduce(self) -> str:
        return f"Меня зовут {self.__name}."


class Employee(Person):
    """Class representing an employee."""

    def __init__(self, name: str, salary: float, **kwargs):
        super().__init__(name, **kwargs)
        self.salary = salary

    def _calculate_bonus(self) -> float:
        return self.salary * 0.1

    def get_info(self) -> str:
        return f"Сотрудник: {self.get_name()}, ЗП: {self.salary}"


class Client(Person):
    """Class representing a client with a budget."""

    def __init__(self, name: str, budget: float):
        super().__init__(name)
        self.budget = budget
        self.bookings = []
        self.reviews = []

    def pay(self, amount: float):
        if amount > self.budget:
            raise InsufficientFundsException(
                f"Не хватает {amount - self.budget} средств."
            )
        self.budget -= amount


class TourGuide(Employee):
    """Class representing a tour guide."""

    def __init__(self, name: str, salary: float, languages: list, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.languages = languages
        self.is_available = True

    def work(self) -> str:
        if not self.is_available:
            raise GuideNotAvailableException("Гид занят.")
        return f"Гид {self.get_name()} проводит экскурсию."


class Manager(Employee):
    """Class representing a manager."""

    def __init__(self, name: str, salary: float, department: str, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.department = department

    def work(self) -> str:
        return f"Менеджер {self.get_name()} управляет отделом {self.department}."


class TourGuideManager(TourGuide, Manager):
    """Class combining the roles of a guide and a manager."""

    def __init__(self, name: str, salary: float, languages: list, department: str):
        super().__init__(
            name=name, salary=salary, languages=languages, department=department
        )

    def work(self) -> str:
        return f"Старший гид-менеджер {self.get_name()} совмещает роли."


class MultiRoleEmployee(TourGuide, Manager):
    """Class explicitly resolving method names from both parents."""

    def __init__(self, name: str, salary: float, languages: list, department: str):
        super().__init__(
            name=name, salary=salary, languages=languages, department=department
        )

    def work(self) -> str:
        return TourGuide.work(self) + " И " + Manager.work(self)


class Transport:
    """Base class representing a transport vehicle."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.seats = [True] * capacity  # True = свободно

    def book_seat(self, seat_number: int):
        if seat_number < 0 or seat_number >= self.capacity:
            raise TransportException("Неверный номер места.")
        if not self.seats[seat_number]:
            raise VehicleOverloadException(f"Место {seat_number} уже занято.")
        self.seats[seat_number] = False


class Bus(Transport):
    """Class representing a bus."""

    def __init__(self, capacity: int, route: str, **kwargs):
        super().__init__(capacity, **kwargs)
        self.route = route


class Airplane(Transport):
    """Class representing an airplane."""

    def __init__(self, capacity: int, airline: str, **kwargs):
        super().__init__(capacity, **kwargs)
        self.airline = airline


class Train(Transport):
    """Class representing a train."""

    def __init__(self, capacity: int, train_number: str, **kwargs):
        super().__init__(capacity, **kwargs)
        self.train_number = train_number


class Ship(Transport):
    """Class representing a cruise ship."""

    def __init__(self, capacity: int, ship_name: str, **kwargs):
        super().__init__(capacity, **kwargs)
        self.ship_name = ship_name


class TransferTour(Bus, Airplane):
    """Diamond inheritance (bus + airplane)."""

    def __init__(self, capacity: int, route: str, airline: str):
        super().__init__(capacity=capacity, route=route, airline=airline)


class Country:
    def __init__(self, name: str, visa_required: bool):
        self.name = name
        self.visa_required = visa_required


class City:
    def __init__(self, name: str, country: Country):
        self.name = name
        self.country = country


class Resort:
    def __init__(self, name: str, city: City, rating: float):
        self.name = name
        self.city = city
        self.rating = rating


class Attraction:
    def __init__(self, name: str, location: City, ticket_price: float):
        self.name = name
        self.location = location
        self.ticket_price = ticket_price


class Room:
    def __init__(self, room_number: str, room_type: RoomType, price_per_night: float):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_booked = False

    def book(self):
        if self.is_booked:
            raise HotelFullyBookedException(f"Номер {self.room_number} уже занят.")
        self.is_booked = True


class Hotel:
    def __init__(self, name: str, city: City, stars: int):
        self.name = name
        self.city = city
        self.stars = stars
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_available_rooms(self) -> list:
        return [room for room in self.rooms if not room.is_booked]


class Hostel(Hotel):
    def __init__(self, name: str, city: City, stars: int, dorm_capacity: int):
        super().__init__(name, city, stars)
        self.dorm_capacity = dorm_capacity


class Apartment(Hotel):
    def __init__(self, name: str, city: City, stars: int, owner_name: str):
        super().__init__(name, city, stars)
        self.owner_name = owner_name


class Excursion:
    def __init__(self, name: str, price: float, attraction: Attraction):
        self.name = name
        self.price = price
        self.attraction = attraction


class Tour:
    def __init__(self, name: str, price: float, duration_days: int, resort: Resort):
        self.name = name
        self.price = price
        self.duration_days = duration_days
        self.resort = resort
        self.transports = []
        self.hotels = []
        self.excursions = []

    def add_transport(self, transport: Transport):
        self.transports.append(transport)

    def add_hotel(self, hotel: Hotel):
        self.hotels.append(hotel)

    def calculate_total_price(self) -> float:
        total = self.price
        for exc in self.excursions:
            total += exc.price
        return total


class Payment:
    def __init__(self, amount: float, method: PaymentMethod):
        self.amount = amount
        self.method = method
        self.date = datetime.datetime.now()


class Transaction:
    def __init__(self, payment: Payment, status: str):
        self.payment = payment
        self.status = status


class Invoice:
    def __init__(self, amount: float, tax: float):
        self.amount = amount
        self.tax = tax

    def get_total(self) -> float:
        return self.amount + self.tax


class Passport:
    def __init__(
        self, number: str, issue_date: datetime.date, expiry_date: datetime.date
    ):
        self.number = number
        self.issue_date = issue_date
        self.expiry_date = expiry_date

    def is_valid(self) -> bool:
        if self.expiry_date < datetime.date.today():
            raise InvalidClientDataException("Паспорт просрочен.")
        return True


class Visa:
    def __init__(self, country: Country, expiry_date: datetime.date):
        self.country = country
        self.expiry_date = expiry_date

    def check_validity(self):
        if self.expiry_date < datetime.date.today():
            raise InvalidVisaException("Виза просрочена.")
        return True


class Booking:
    def __init__(self, client: Client, tour: Tour, manager: Manager):
        self.client = client
        self.tour = tour
        self.manager = manager
        self.status = "Создана"
        self.created_at = datetime.datetime.now()

    def confirm(self):
        if self.status == "Отменена":
            raise BookingNotFoundException("Нельзя оплатить отмененную бронь.")

        total_price = self.tour.calculate_total_price()
        self.client.pay(total_price)

        payment = Payment(total_price, PaymentMethod.CARD)
        transaction = Transaction(payment, "Успешно")

        self.status = "Оплачена"
        self.client.bookings.append(self)
        return transaction


class Review:
    def __init__(self, client: Client, tour: Tour, rating: int, text: str):
        self.client = client
        self.tour = tour
        self.rating = rating
        self.text = text
        self.date = datetime.datetime.now()


class Complaint:
    def __init__(self, client: Client, booking: Booking, reason: str):
        self.client = client
        self.booking = booking
        self.reason = reason
        self.is_resolved = False

    def resolve(self):
        self.is_resolved = True


class Agency:
    def __init__(self, name: str):
        self.name = name
        self.branches = []
        self.tours = []

    def add_branch(self, branch):
        self.branches.append(branch)


class Branch:
    def __init__(self, city: City, address: str):
        self.city = city
        self.address = address
        self.employees = []

    def hire_employee(self, employee: Employee):
        self.employees.append(employee)


class Department:
    def __init__(self, name: str, manager: Manager):
        self.name = name
        self.manager = manager


if __name__ == "__main__":
    print("--- Создание базовых сущностей ---")
    client = Client("Иван", 150000)
    manager = Manager("Олег", 80000, "Продажи")
    guide = TourGuide("Анна", 50000, ["EN", "FR"])

    country = Country("Турция", visa_required=False)
    city = City("Анталья", country)
    resort = Resort("Belek", city, 4.8)

    hotel = Hotel("Rixos", city, 5)
    room = Room("101", RoomType.LUXURY, 15000)
    hotel.add_room(room)

    transport = Bus(50, "Аэропорт-Отель")

    tour = Tour("Летний Тур", 50000, 7, resort)
    tour.add_hotel(hotel)
    tour.add_transport(transport)

    print("\n--- Бронирование ---")
    try:
        booking = Booking(client, tour, manager)
        trans = booking.confirm()
        print(f"Бронь успешно оплачена! Остаток: {client.budget}")
    except InsufficientFundsException as e:
        print(f"Ошибка: {e}")
    except HotelFullyBookedException as e:
        print(f"Ошибка отеля: {e}")

    print("\n--- Проверка гида ---")
    try:
        print(guide.work())
        guide.is_available = False
        print(guide.work())
    except GuideNotAvailableException as e:
        print(f"Ошибка: {e}")
