class Person:
    """
    Base class representing a human.

    Demonstrates encapsulation using a private (mangled) attribute.
    """

    def __init__(self, name: str):
        """
        Initialize a Person instance.

        :param name: The full name of the person.
        :type name: str
        """
        self.__name = name

    def get_name(self) -> str:
        """
        Retrieve the person's name.

        :return: The name of the person.
        :rtype: str
        """
        return self.__name

    def introduce(self) -> str:
        """
        Generate an introduction string.

        :return: A formatted introduction string.
        :rtype: str
        """
        return f"Меня зовут {self.__name}."


class Employee(Person):
    """
    Class representing an employee, inheriting from Person.

    Demonstrates public inheritance and a protected method.
    """

    def __init__(self, name: str, salary: float, **kwargs):
        """
        Initialize an Employee instance.

        :param name: The full name of the employee.
        :type name: str
        :param salary: The monthly salary of the employee.
        :type salary: float
        """
        super().__init__(name, **kwargs)
        self.salary = salary

    def _calculate_bonus(self) -> float:
        """
        Calculate the employee's bonus (protected method).

        :return: The calculated bonus amount.
        :rtype: float
        """
        return self.salary * 0.1

    def get_info(self) -> str:
        """
        Retrieve employee information.

        :return: A formatted string with employee details.
        :rtype: str
        """
        return f"Сотрудник: {self.get_name()}, ЗП: {self.salary}"


class Client(Person):
    """
    Class representing a client, inheriting from Person.
    """

    def __init__(self, name: str, budget: float):
        """
        Initialize a Client instance.

        :param name: The full name of the client.
        :type name: str
        :param budget: The client's available budget.
        :type budget: float
        """
        super().__init__(name)
        self.budget = budget


class TourGuide(Employee):
    """
    Class representing a tour guide.

    Demonstrates method overriding (equivalent to virtual methods in C++).
    """

    def __init__(self, name: str, salary: float, languages: list, **kwargs):
        """
        Initialize a TourGuide instance.

        :param name: The full name of the guide.
        :type name: str
        :param salary: The monthly salary of the guide.
        :type salary: float
        :param languages: A list of languages spoken by the guide.
        :type languages: list
        """
        super().__init__(name, salary, **kwargs)
        self.languages = languages

    def work(self) -> str:
        """
        Simulate the guide performing their work.

        :return: A description of the guide's activity.
        :rtype: str
        """
        return f"Гид {self.get_name()} проводит экскурсию."


class Manager(Employee):
    """
    Class representing a manager.

    Demonstrates method overriding.
    """

    def __init__(self, name: str, salary: float, department: str, **kwargs):
        """
        Initialize a Manager instance.

        :param name: The full name of the manager.
        :type name: str
        :param salary: The monthly salary of the manager.
        :type salary: float
        :param department: The department managed by this manager.
        :type department: str
        """
        super().__init__(name, salary, **kwargs)
        self.department = department

    def work(self) -> str:
        """
        Simulate the manager performing their work.

        :return: A description of the manager's activity.
        :rtype: str
        """
        return f"Менеджер {self.get_name()} управляет отделом {self.department}."


class TourGuideManager(TourGuide, Manager):
    """
    Class combining the roles of a tour guide and a manager.

    Demonstrates multiple inheritance.
    """

    def __init__(self, name: str, salary: float, languages: list, department: str):
        """
        Initialize a TourGuideManager instance.

        :param name: The full name of the employee.
        :type name: str
        :param salary: The monthly salary of the employee.
        :type salary: float
        :param languages: A list of languages spoken by the employee.
        :type languages: list
        :param department: The department managed by the employee.
        :type department: str
        """
        super().__init__(name=name, salary=salary, languages=languages, department=department)

    def work(self) -> str:
        """
        Simulate the combined work of a guide and a manager.

        :return: A description of the combined activity.
        :rtype: str
        """
        return f"Старший гид-менеджер {self.get_name()} совмещает роли."


class Transport:
    """
    Base class representing a transport vehicle.

    Participates in the diamond inheritance structure.
    """

    def __init__(self, capacity: int):
        """
        Initialize a Transport instance.

        :param capacity: The maximum passenger capacity.
        :type capacity: int
        """
        self.capacity = capacity


class Bus(Transport):
    """
    Class representing a bus, inheriting from Transport.
    """

    def __init__(self, capacity: int, route: str, **kwargs):
        """
        Initialize a Bus instance.

        :param capacity: The maximum passenger capacity.
        :type capacity: int
        :param route: The bus route description.
        :type route: str
        """
        super().__init__(capacity, **kwargs)
        self.route = route


class Airplane(Transport):
    """
    Class representing an airplane, inheriting from Transport.
    """

    def __init__(self, capacity: int, airline: str, **kwargs):
        """
        Initialize an Airplane instance.

        :param capacity: The maximum passenger capacity.
        :type capacity: int
        :param airline: The name of the airline.
        :type airline: str
        """
        super().__init__(capacity, **kwargs)
        self.airline = airline


class TransferTour(Bus, Airplane):
    """
    Class representing a combined tour (bus + airplane).

    Demonstrates diamond inheritance. Python resolves the duplicate base class
    issue automatically via MRO (Method Resolution Order), mimicking C++ virtual inheritance.
    """

    def __init__(self, capacity: int, route: str, airline: str):
        """
        Initialize a TransferTour instance.

        :param capacity: The maximum passenger capacity.
        :type capacity: int
        :param route: The bus route description.
        :type route: str
        :param airline: The name of the airline.
        :type airline: str
        """
        super().__init__(capacity=capacity, route=route, airline=airline)
        self.route = route
        self.airline = airline


class MultiRoleEmployee(TourGuide, Manager):
    """
    Class representing an employee with two distinct roles.

    Demonstrates explicit name resolution, analogous to the C++ using-declaration.
    """

    def __init__(self, name: str, salary: float, languages: list, department: str):
        """
        Initialize a MultiRoleEmployee instance.

        :param name: The full name of the employee.
        :type name: str
        :param salary: The monthly salary of the employee.
        :type salary: float
        :param languages: A list of languages spoken by the employee.
        :type languages: list
        :param department: The department managed by the employee.
        :type department: str
        """
        super().__init__(name=name, salary=salary, languages=languages, department=department)

    def work(self) -> str:
        """
        Explicitly call methods from both parent classes.

        :return: A combined description of both roles.
        :rtype: str
        """
        return TourGuide.work(self) + " И " + Manager.work(self)


if __name__ == "__main__":
    print("--- Тест 1: Базовые классы и закрытое поле ---")
    person = Person("Иван")
    print(person.introduce())

    print("\n--- Тест 2: Виртуальные методы (Полиморфизм) ---")
    guide = TourGuide("Анна", 50000, ["EN", "FR"])
    manager = Manager("Олег", 80000, "Туры")
    print(guide.work())
    print(manager.work())

    print("\n--- Тест 3: Множественное наследование ---")
    tgm = TourGuideManager("Елена", 100000, ["DE"], "Экскурсии")
    print(tgm.work())
    print(f"Языки: {tgm.languages}, Отдел: {tgm.department}")

    print("\n--- Тест 4: Виртуальное наследование (Ромб) ---")
    transfer = TransferTour(50, "Москва-Сочи", "Аэрофлот")
    print(
        f"Вместимость: {transfer.capacity}, Маршрут: {transfer.route}, Авиакомпания: {transfer.airline}"
    )

    print("\n--- Тест 5: Разрешение имен (using-директива) ---")
    multi = MultiRoleEmployee("Сергей", 70000, ["ES"], "Продажи")
    print(multi.work())