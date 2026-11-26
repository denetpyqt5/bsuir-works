import pytest

from ppois.second.src.second.main import (
    Airplane,
    Booking,
    Bus,
    City,
    Client,
    Country,
    Employee,
    GuideNotAvailableException,
    Hotel,
    HotelFullyBookedException,
    InsufficientFundsException,
    Manager,
    MultiRoleEmployee,
    Person,
    Resort,
    Room,
    RoomType,
    Tour,
    TourGuide,
    TourGuideManager,
    TransferTour,
    Transport,
    VehicleOverloadException,
)


class TestPerson:
    def test_get_name(self):
        person = Person("Иван")
        assert person.get_name() == "Иван"

    def test_private_attribute_inaccessible(self):
        person = Person("Иван")
        with pytest.raises(AttributeError):
            _ = person.__name

    def test_introduce(self):
        person = Person("Мария")
        assert person.introduce() == "Меня зовут Мария."


class TestEmployee:
    def test_initialization(self):
        emp = Employee("Петр", 50000)
        assert emp.get_name() == "Петр"
        assert emp.salary == 50000

    def test_calculate_bonus(self):
        emp = Employee("Петр", 50000)
        assert emp._calculate_bonus() == 5000.0

    def test_get_info(self):
        emp = Employee("Петр", 50000)
        assert emp.get_info() == "Сотрудник: Петр, ЗП: 50000"


class TestClient:
    def test_initialization(self):
        client = Client("Ольга", 100000)
        assert client.get_name() == "Ольга"
        assert client.budget == 100000

    def test_pay_success(self):
        client = Client("Ольга", 100000)
        client.pay(50000)
        assert client.budget == 50000

    def test_pay_insufficient_funds(self):
        client = Client("Ольга", 1000)
        with pytest.raises(InsufficientFundsException):
            client.pay(5000)


class TestVirtualMethods:
    def test_tour_guide_work(self):
        guide = TourGuide("Анна", 50000, ["EN", "FR"])
        assert guide.work() == "Гид Анна проводит экскурсию."

    def test_manager_work(self):
        manager = Manager("Олег", 80000, "Туры")
        assert manager.work() == "Менеджер Олег управляет отделом Туры."

    def test_polymorphism(self):
        employees = [
            TourGuide("Анна", 50000, ["EN"]),
            Manager("Олег", 80000, "Туры"),
        ]
        results = [emp.work() for emp in employees]
        assert results[0] == "Гид Анна проводит экскурсию."
        assert results[1] == "Менеджер Олег управляет отделом Туры."

    def test_guide_not_available(self):
        guide = TourGuide("Анна", 50000, ["EN", "FR"])
        guide.is_available = False
        with pytest.raises(GuideNotAvailableException):
            guide.work()


class TestMultipleInheritance:
    def test_initialization(self):
        tgm = TourGuideManager("Елена", 100000, ["DE"], "Экскурсии")
        assert tgm.get_name() == "Елена"
        assert tgm.salary == 100000
        assert tgm.languages == ["DE"]
        assert tgm.department == "Экскурсии"

    def test_work_override(self):
        tgm = TourGuideManager("Елена", 100000, ["DE"], "Экскурсии")
        assert tgm.work() == "Старший гид-менеджер Елена совмещает роли."

    def test_is_subclass_of_both(self):
        tgm = TourGuideManager("Елена", 100000, ["DE"], "Экскурсии")
        assert isinstance(tgm, TourGuide)
        assert isinstance(tgm, Manager)
        assert isinstance(tgm, Employee)


class TestVirtualInheritance:
    def test_transfer_tour_initialization(self):
        tour = TransferTour(50, "Москва-Сочи", "Аэрофлот")
        assert tour.capacity == 50
        assert tour.route == "Москва-Сочи"
        assert tour.airline == "Аэрофлот"

    def test_transport_base_class_single_init(self):
        tour = TransferTour(50, "Москва-Сочи", "Аэрофлот")
        assert TransferTour.__mro__[0] == TransferTour
        assert TransferTour.__mro__[1] == Bus
        assert TransferTour.__mro__[2] == Airplane
        assert TransferTour.__mro__[3] == Transport
        assert tour.capacity == 50

    def test_is_subclass_of_transport(self):
        tour = TransferTour(50, "Москва-Сочи", "Аэрофлот")
        assert isinstance(tour, Transport)
        assert isinstance(tour, Bus)
        assert isinstance(tour, Airplane)


class TestNameResolution:
    def test_explicit_method_resolution(self):
        multi = MultiRoleEmployee("Сергей", 70000, ["ES"], "Продажи")
        expected = (
            "Гид Сергей проводит экскурсию. И "
            "Менеджер Сергей управляет отделом Продажи."
        )
        assert multi.work() == expected

    def test_attributes_from_both_parents(self):
        multi = MultiRoleEmployee("Сергей", 70000, ["ES"], "Продажи")
        assert multi.languages == ["ES"]
        assert multi.department == "Продажи"

    def test_is_subclass_of_both(self):
        multi = MultiRoleEmployee("Сергей", 70000, ["ES"], "Продажи")
        assert isinstance(multi, TourGuide)
        assert isinstance(multi, Manager)


class TestTransport:
    def test_book_seat_success(self):
        bus = Bus(50, "Москва-Сочи")
        bus.book_seat(5)
        assert bus.seats[5] is False

    def test_book_seat_overload(self):
        bus = Bus(50, "Москва-Сочи")
        bus.book_seat(5)
        with pytest.raises(VehicleOverloadException):
            bus.book_seat(5)


class TestHotel:
    def test_room_booking(self):
        hotel = Hotel("Rixos", City("Анталья", Country("Турция", False)), 5)
        room = Room("101", RoomType.LUXURY, 15000)
        hotel.add_room(room)

        room.book()
        assert room.is_booked is True

    def test_room_double_booking(self):
        hotel = Hotel("Rixos", City("Анталья", Country("Турция", False)), 5)
        room = Room("101", RoomType.LUXURY, 15000)
        hotel.add_room(room)

        room.book()
        with pytest.raises(HotelFullyBookedException):
            room.book()


class TestBooking:
    def test_confirm_booking(self):
        client = Client("Иван", 150000)
        manager = Manager("Олег", 80000, "Продажи")
        country = Country("Турция", False)
        city = City("Анталья", country)
        resort = Resort("Belek", city, 4.8)
        tour = Tour("Летний Тур", 50000, 7, resort)

        booking = Booking(client, tour, manager)
        transaction = booking.confirm()

        assert booking.status == "Оплачена"
        assert client.budget == 100000
        assert transaction.status == "Успешно"
