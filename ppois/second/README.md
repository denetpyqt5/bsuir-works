# Проект: Объектная модель «Туристическая компания»

Данный репозиторий содержит реализацию объектной модели для предметной области «Туристическая компания» на языке Python. 
Проект выполнен в рамках задания по ООП и удовлетворяет количественным требованиям.

## Выполнение требований
* **Классы:** более 50
* **Поля:** более 150
* **Методы (бизнес-логика):** более 100
* **Ассоциации:** более 30
* **Исключения:** 12

---

## 1. Описание классов и их структура

Ниже представлена таблица с основными классами домена, их полями, методами и ассоциациями.

| Класс | Поля | Методы (бизнес-логика) | Ассоциации (связанные классы) |
| :--- | :--- | :--- | :--- |
| **Person** | 1 (`__name`) | `get_name()`, `introduce()` | — |
| **Client** | 3 (`budget`, `bookings`, `reviews`) | `pay()`, `add_review()`, `get_booking_history()` | `Booking`, `Review`, `Tour` |
| **Employee** | 2 (`salary`, `is_available`) | `calculate_bonus()`, `get_info()` | — |
| **TourGuide** | 3 (`languages`, `is_available`, `_rating`) | `work()`, `conduct_excursion()`, `add_language()` | `Excursion`, `Tour` |
| **Manager** | 2 (`department`, `subordinates`) | `work()`, `process_booking()`, `approve_discount()` | `Booking`, `Employee` |
| **TourGuideManager** | 4 (`languages`, `department`, ...) | `work()` (переопределен) | `TourGuide`, `Manager` |
| **MultiRoleEmployee** | 4 | `work()` (явный вызов родителей) | `TourGuide`, `Manager` |
| **Transport** | 3 (`capacity`, `seats`, `type`) | `book_seat()`, `get_free_seats_count()` | `Route`, `Ticket` |
| **Bus** | 2 (`route`, `capacity`) | `drive()`, `open_doors()` | `Route` |
| **Airplane** | 2 (`airline`, `capacity`) | `fly()`, `board_passengers()` | `Airline` |
| **Train** | 2 (`train_number`, `capacity`) | `depart()`, `check_tickets()` | `Route` |
| **Ship** | 2 (`ship_name`, `capacity`) | `sail()`, `drop_anchor()` | `Route` |
| **TransferTour** | 3 (ромбовидное наследование) | — | `Bus`, `Airplane` |
| **Hotel** | 4 (`name`, `city`, `stars`, `rooms`) | `add_room()`, `get_available_rooms()`, `book_room()` | `City`, `Room`, `Tour` |
| **Hostel** | 4 | `get_dorm_capacity()` | `Hotel` |
| **Apartment** | 4 | `contact_owner()` | `Hotel` |
| **Room** | 4 (`room_number`, `type`, `price`, `is_booked`) | `book()`, `cancel_booking()`, `get_price()` | `Hotel`, `RoomType` |
| **Tour** | 5 (`name`, `price`, `duration`, `resort`, `hotels`) | `calculate_total_price()`, `add_transport()`, `add_hotel()` | `Resort`, `Hotel`, `Transport`, `Excursion` |
| **Excursion** | 3 (`name`, `price`, `attraction`) | `start_excursion()`, `get_duration()` | `Attraction`, `TourGuide` |
| **Booking** | 5 (`client`, `tour`, `manager`, `status`, `created_at`) | `confirm()`, `cancel()`, `get_status()` | `Client`, `Tour`, `Manager`, `Payment` |
| **Payment** | 3 (`amount`, `method`, `date`) | `process_payment()`, `refund()` | `Booking`, `Transaction` |
| **Transaction** | 2 (`payment`, `status`) | `complete()`, `fail()` | `Payment` |
| **Invoice** | 3 (`amount`, `tax`, `issued_date`) | `get_total()`, `print_invoice()` | `Booking` |
| **Passport** | 3 (`number`, `issue_date`, `expiry_date`) | `is_valid()`, `get_expiry_days()` | `Client` |
| **Visa** | 3 (`country`, `expiry_date`, `type`) | `check_validity()`, `renew()` | `Country`, `Client` |
| **Country** | 2 (`name`, `visa_required`) | `is_visa_needed()` | `City`, `Visa` |
| **City** | 2 (`name`, `country`) | `get_country()` | `Country`, `Hotel`, `Branch` |
| **Resort** | 3 (`name`, `city`, `rating`) | `get_popularity()` | `City`, `Tour` |
| **Attraction** | 3 (`name`, `location`, `ticket_price`) | `buy_ticket()` | `City`, `Excursion` |
| **Review** | 4 (`client`, `tour`, `rating`, `text`) | `publish()`, `edit()` | `Client`, `Tour` |
| **Complaint** | 3 (`client`, `booking`, `reason`) | `resolve()`, `escalate()` | `Client`, `Booking` |
| **Agency** | 3 (`name`, `branches`, `tours`) | `add_branch()`, `add_tour()` | `Branch`, `Tour` |
| **Branch** | 3 (`city`, `address`, `employees`) | `hire_employee()`, `fire_employee()` | `City`, `Employee` |
| **Department** | 2 (`name`, `manager`) | `assign_manager()` | `Manager`, `Employee` |
| **Exceptions** | — | 12 собственных классов исключений | `TransportException`, `InsufficientFundsException` и др. |

---

## 2. Собственные классы исключений (12 штук)

В проекте реализована собственная иерархия исключений, наследуемая от базового `TourCompanyException`:

1. `TransportException` — проблемы с транспортом.
2. `InsufficientFundsException` — недостаточно средств у клиента.
3. `InvalidClientDataException` — некорректные данные клиента.
4. `BookingNotFoundException` — бронь не найдена.
5. `InvalidBookingDataException` — неверные данные брони.
6. `InvalidBaggageDataException` — проблемы с данными багажа.
7. `BaggageOverweightException` — превышен вес багажа.
8. `VehicleOverloadException` — перегрузка транспорта.
9. `VehicleNotAvailableException` — транспорт недоступен.
10. `GuideNotAvailableException` — гид недоступен.
11. `InvalidVisaException` — проблемы с визой.
12. `HotelFullyBookedException` — отель полностью занят.

---

## 3. Архитектурные особенности

* **Множественное наследование:** Реализовано в классах `TourGuideManager` и `MultiRoleEmployee`.
* **Виртуальное наследование (Ромб):** Реализовано в классе `TransferTour` (наследует `Bus` и `Airplane`). В Python проблема дублирования базового класса `Transport` решается через алгоритм MRO (Method Resolution Order).
* **Разрешение имен:** В классе `MultiRoleEmployee` метод `work()` явно вызывает методы обоих родителей, имитируя `using`-директиву из C++.
* **Инкапсуляция:** Приватные поля (например, `__name` в `Person`) защищены от прямого доступа.