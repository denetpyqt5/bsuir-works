from abc import ABC, abstractmethod
from enum import Enum
import datetime


class ComputerException(Exception):
    pass

class ComponentNotFoundError(ComputerException):
    pass

class InsufficientPowerError(ComputerException):
    pass

class OverheatingError(ComputerException):
    pass

class IncompatibleSocketError(ComputerException):
    pass

class MemoryOverflowError(ComputerException):
    pass

class DiskSpaceError(ComputerException):
    pass

class InvalidOSError(ComputerException):
    pass

class VirusDetectedError(ComputerException):
    pass

class NetworkConnectionError(ComputerException):
    pass

class PermissionDeniedError(ComputerException):
    pass

class InvalidHardwareConfigError(ComputerException):
    pass

class DriverNotFoundError(ComputerException):
    pass


class ComponentType(Enum):
    CPU = "Процессор"
    GPU = "Видеокарта"
    RAM = "Оперативная память"
    STORAGE = "Накопитель"
    PSU = "Блок питания"

class OSFamily(Enum):
    WINDOWS = "Windows"
    LINUX = "Linux"
    MACOS = "macOS"

class PortType(Enum):
    USB = "USB"
    HDMI = "HDMI"
    ETHERNET = "Ethernet"
    AUDIO = "Audio"


class Component(ABC):
    def __init__(self, name: str, manufacturer: str, power_draw: int):
        self._name = name
        self._manufacturer = manufacturer
        self._power_draw = power_draw
        self._temperature = 30.0

    def get_info(self) -> str:
        return f"{self._manufacturer} {self._name}"

    def heat_up(self, degrees: float):
        self._temperature += degrees
        if self._temperature > 90.0:
            raise OverheatingError(f"{self._name} перегрелся! Текущая температура: {self._temperature}°C")

    @abstractmethod
    def connect(self) -> str:
        pass


class CPU(Component):
    def __init__(self, name: str, manufacturer: str, cores: int, frequency: float, socket: str, power_draw: int):
        super().__init__(name, manufacturer, power_draw)
        self._cores = cores
        self._frequency = frequency
        self._socket = socket

    def connect(self) -> str:
        return f"Процессор {self._name} установлен в сокет {self._socket}."

    def compute(self, task_complexity: int) -> float:
        return task_complexity / (self._cores * self._frequency)


class GPU(Component):
    def __init__(self, name: str, manufacturer: str, vram: int, power_draw: int):
        super().__init__(name, manufacturer, power_draw)
        self._vram = vram

    def connect(self) -> str:
        return f"Видеокарта {self._name} установлена в слот PCIe."

    def render_frame(self, resolution: str) -> str:
        if self._vram < 4 and resolution == "4K":
            raise MemoryOverflowError("Недостаточно видеопамяти для 4K.")
        return f"Кадр {resolution} отрендерен на {self._name}."


class RAM(Component):
    def __init__(self, name: str, manufacturer: str, capacity_gb: int, speed_mhz: int, power_draw: int):
        super().__init__(name, manufacturer, power_draw)
        self._capacity_gb = capacity_gb
        self._speed_mhz = speed_mhz
        self._used_gb = 0

    def connect(self) -> str:
        return f"Планка памяти {self._name} ({self._capacity_gb}GB) установлена."

    def allocate_memory(self, size_gb: int):
        if self._used_gb + size_gb > self._capacity_gb:
            raise MemoryOverflowError("Не хватает оперативной памяти.")
        self._used_gb += size_gb

    def free_memory(self, size_gb: int):
        self._used_gb = max(0, self._used_gb - size_gb)


class Storage(Component):
    def __init__(self, name: str, manufacturer: str, capacity_gb: int, is_ssd: bool, power_draw: int):
        super().__init__(name, manufacturer, power_draw)
        self._capacity_gb = capacity_gb
        self._is_ssd = is_ssd
        self._used_space_gb = 0

    def connect(self) -> str:
        return f"Накопитель {self._name} ({'SSD' if self._is_ssd else 'HDD'}) подключен."

    def save_file(self, size_gb: int):
        if self._used_space_gb + size_gb > self._capacity_gb:
            raise DiskSpaceError(f"Недостаточно места на {self._name}.")
        self._used_space_gb += size_gb


class PowerSupply(Component):
    def __init__(self, name: str, manufacturer: str, max_wattage: int):
        super().__init__(name, manufacturer, 0)
        self._max_wattage = max_wattage

    def connect(self) -> str:
        return f"Блок питания {self._name} ({self._max_wattage}W) подключен к сети."

    def check_power(self, total_draw: int):
        if total_draw > self._max_wattage:
            raise InsufficientPowerError(f"БП не справляется. Нужно {total_draw}W, максимум {self._max_wattage}W.")


class Motherboard(Component):
    def __init__(self, name: str, manufacturer: str, socket: str, power_draw: int):
        super().__init__(name, manufacturer, power_draw)
        self._socket = socket
        self._installed_components = []
        self._ports = []

    def connect(self) -> str:
        return f"Материнская плата {self._name} установлена в корпус."

    def install_component(self, component: Component):
        if isinstance(component, CPU) and component._socket != self._socket:
            raise IncompatibleSocketError(f"Сокет процессора ({component._socket}) не подходит к плате ({self._socket}).")
        self._installed_components.append(component)

    def add_port(self, port_type: PortType):
        self._ports.append(port_type)


class Peripheral(ABC):
    def __init__(self, name: str, interface: PortType):
        self._name = name
        self._interface = interface
        self._is_connected = False

    @abstractmethod
    def plug_in(self):
        pass


class Keyboard(Peripheral):
    def plug_in(self):
        self._is_connected = True
        return f"Клавиатура {self._name} подключена через {self._interface.value}."

    def type_text(self, text: str) -> str:
        if not self._is_connected:
            raise NetworkConnectionError("Клавиатура не подключена.")
        return f"Введен текст: {text}"


class Mouse(Peripheral):
    def plug_in(self):
        self._is_connected = True
        return f"Мышь {self._name} подключена."

    def click(self) -> str:
        if not self._is_connected:
            raise NetworkConnectionError("Мышь не подключена.")
        return "Клик!"


class Monitor(Peripheral):
    def __init__(self, name: str, interface: PortType, resolution: str):
        super().__init__(name, interface)
        self._resolution = resolution

    def plug_in(self):
        self._is_connected = True
        return f"Монитор {self._name} ({self._resolution}) подключен."

    def display_image(self, image_data: str):
        if not self._is_connected:
            raise NetworkConnectionError("Монитор не подключен.")
        return f"Отображение: {image_data}"


class Software:
    def __init__(self, name: str, version: str, size_gb: float):
        self._name = name
        self._version = version
        self._size_gb = size_gb
        self._is_installed = False

    def install(self, storage: Storage):
        if self._is_installed:
            return f"{self._name} уже установлен."
        storage.save_file(self._size_gb)
        self._is_installed = True
        return f"{self._name} v{self._version} установлен."


class OperatingSystem(Software):
    def __init__(self, name: str, version: str, size_gb: float, family: OSFamily):
        super().__init__(name, version, size_gb)
        self._family = family
        self._running_processes = []

    def boot(self, ram: RAM) -> str:
        ram.allocate_memory(2)
        return f"Загрузка {self._family.value} {self._name}..."

    def run_process(self, process_name: str, ram_needed: int, ram: RAM):
        ram.allocate_memory(ram_needed)
        self._running_processes.append(process_name)
        return f"Процесс {process_name} запущен."


class Application(Software):
    def __init__(self, name: str, version: str, size_gb: float, is_heavy: bool):
        super().__init__(name, version, size_gb)
        self._is_heavy = is_heavy

    def execute(self, cpu: CPU, ram: RAM) -> str:
        ram_needed = 8 if self._is_heavy else 2
        ram.allocate_memory(ram_needed)
        cpu.compute(1000 if self._is_heavy else 100)
        return f"Приложение {self._name} выполняется."


class Driver(Software):
    def __init__(self, name: str, version: str, size_gb: float, target_device: str):
        super().__init__(name, version, size_gb)
        self._target_device = target_device

    def load(self) -> str:
        return f"Драйвер {self._name} для {self._target_device} загружен в ядро."


class Virus(Software):
    def __init__(self, name: str, version: str, size_gb: float, danger_level: int):
        super().__init__(name, version, size_gb)
        self._danger_level = danger_level

    def infect(self, application: Application) -> str:
        if self._danger_level > 5:
            raise VirusDetectedError(f"Вирус {self._name} повредил {application._name}!")
        return f"Вирус {self._name} заразил {application._name}."


class Antivirus(Software):
    def __init__(self, name: str, version: str, size_gb: float, virus_database_date: datetime.date):
        super().__init__(name, version, size_gb)
        self._virus_database_date = virus_database_date

    def scan(self, virus: Virus) -> str:
        if virus._danger_level > 0:
            return f"Антивирус {self._name} обнаружил {virus._name} и удалил его."
        return "Угроз не найдено."


class Browser(Application):
    def __init__(self, name: str, version: str, size_gb: float, engine: str):
        super().__init__(name, version, size_gb, is_heavy=True)
        self._engine = engine
        self._open_tabs = 0

    def open_tab(self, url: str) -> str:
        self._open_tabs += 1
        return f"Вкладка {url} открыта в {self._name}. Всего вкладок: {self._open_tabs}"


class Game(Application):
    def __init__(self, name: str, version: str, size_gb: float, min_gpu_vram: int):
        super().__init__(name, version, size_gb, is_heavy=True)
        self._min_gpu_vram = min_gpu_vram

    def launch(self, gpu: GPU) -> str:
        if gpu._vram < self._min_gpu_vram:
            raise MemoryOverflowError(f"Игре {self._name} нужно минимум {self._min_gpu_vram}GB видеопамяти.")
        return f"Игра {self._name} запущена на {gpu._name}."


class NetworkAdapter(Component):
    def __init__(self, name: str, manufacturer: str, mac_address: str, speed_mbps: int, power_draw: int):
        super().__init__(name, manufacturer, power_draw)
        self._mac_address = mac_address
        self._speed_mbps = speed_mbps
        self._is_connected_to_network = False

    def connect(self) -> str:
        return f"Сетевой адаптер {self._name} установлен."

    def establish_connection(self):
        self._is_connected_to_network = True

    def send_packet(self, data_size_mb: int) -> str:
        if not self._is_connected_to_network:
            raise NetworkConnectionError("Нет подключения к сети.")
        return f"Отправлено {data_size_mb}MB данных со скоростью {self._speed_mbps}Mbps."


class Router:
    def __init__(self, name: str, ip_address: str):
        self._name = name
        self._ip_address = ip_address
        self._connected_devices = []

    def connect_device(self, adapter: NetworkAdapter):
        adapter.establish_connection()
        self._connected_devices.append(adapter)


class User:
    def __init__(self, username: str, password_hash: str, is_admin: bool):
        self._username = username
        self._password_hash = password_hash
        self._is_admin = is_admin

    def login(self, password_hash: str) -> str:
        if self._password_hash != password_hash:
            raise PermissionDeniedError("Неверный пароль.")
        return f"Пользователь {self._username} вошел в систему."

    def request_admin_rights(self) -> str:
        if not self._is_admin:
            raise PermissionDeniedError("У вас нет прав администратора.")
        return "Права администратора подтверждены."


class SystemAdministrator(User):
    def __init__(self, username: str, password_hash: str, root_level: int):
        super().__init__(username, password_hash, is_admin=True)
        self._root_level = root_level

    def install_driver(self, driver: Driver) -> str:
        return f"Администратор {self._username} установил {driver.load()}"

    def kill_process(self, process_name: str, os: OperatingSystem) -> str:
        if process_name in os._running_processes:
            os._running_processes.remove(process_name)
            return f"Процесс {process_name} принудительно завершен."
        return f"Процесс {process_name} не найден."


class ComputerCase(Component):
    def __init__(self, name: str, manufacturer: str, form_factor: str):
        super().__init__(name, manufacturer, 0)
        self._form_factor = form_factor
        self._installed_parts = []

    def connect(self) -> str:
        return f"Корпус {self._name} ({self._form_factor}) готов к сборке."

    def add_part(self, component: Component):
        if len(self._installed_parts) > 10:
            raise InvalidHardwareConfigError("В корпусе закончилось место.")
        self._installed_parts.append(component)


class ThermalPaste(Component):
    def __init__(self, name: str, manufacturer: str, conductivity: float):
        super().__init__(name, manufacturer, 0)
        self._conductivity = conductivity

    def connect(self) -> str:
        return f"Термопаста {self._name} нанесена."

    def apply_to(self, cpu: CPU):
        cpu.heat_up(-10.0)


class CoolingSystem(Component):
    def __init__(self, name: str, manufacturer: str, fan_count: int, power_draw: int):
        super().__init__(name, manufacturer, power_draw)
        self._fan_count = fan_count
        self._is_running = False

    def connect(self) -> str:
        return f"Кулер {self._name} с {self._fan_count} вентиляторами установлен."

    def start_cooling(self, component: Component) -> str:
        self._is_running = True
        component.heat_up(-15.0)
        return f"Охлаждение {self._name} активно. Температура снижена."


class DiagnosticTool(Software):
    def __init__(self, name: str, version: str, size_gb: float):
        super().__init__(name, version, size_gb)

    def check_temperature(self, component: Component) -> str:
        if component._temperature > 80:
            return f"ВНИМАНИЕ: {component._name} перегрет ({component._temperature}°C)!"
        return f"{component._name}: температура в норме ({component._temperature}°C)."

    def check_power(self, psu: PowerSupply, components: list) -> str:
        total_draw = sum(c._power_draw for c in components)
        try:
            psu.check_power(total_draw)
            return "Питания достаточно."
        except InsufficientPowerError as e:
            return str(e)


class Benchmark(Software):
    def __init__(self, name: str, version: str, size_gb: float):
        super().__init__(name, version, size_gb)

    def test_cpu(self, cpu: CPU) -> float:
        return cpu.compute(10000)

    def test_gpu(self, gpu: GPU) -> str:
        return gpu.render_frame("4K")


class Data:
    def __init__(self, file_name: str, size_gb: float):
        self._file_name = file_name
        self._size_gb = size_gb


class Backup:
    def __init__(self, id: int, source_data: Data):
        self._id = id
        self._source_data = source_data
        self._backup_data = None

    def create_copy(self, storage: Storage):
        storage.save_file(self._source_data._size_gb)
        self._backup_data = self._source_data

    def restore(self) -> Data:
        if not self._backup_data:
            raise ComponentNotFoundError("Резервная копия не найдена.")
        return self._backup_data


class Update(Software):
    def __init__(self, name: str, version: str, size_gb: float):
        super().__init__(name, version, size_gb)

    def apply(self, software: Software) -> str:
        software._version = self._version
        return f"Обновление {self._name} до версии {self._version} успешно применено."


class License:
    def __init__(self, license_key: str, expiration_date: datetime.date):
        self._license_key = license_key
        self._expiration_date = expiration_date

    def is_valid(self) -> bool:
        if self._expiration_date < datetime.date.today():
            raise PermissionDeniedError("Лицензия истекла.")
        return True


class Network:
    def __init__(self, subnet: str):
        self._subnet = subnet
        self._connected_adapters = []

    def add_adapter(self, adapter: NetworkAdapter):
        self._connected_adapters.append(adapter)

    def ping(self, ip: str) -> str:
        for adapter in self._connected_adapters:
            if adapter._is_connected_to_network:
                return f"Ответ от {ip}: время=1мс"
        raise NetworkConnectionError("Сеть недоступна.")


class Database(Software):
    def __init__(self, name: str, version: str, size_gb: float):
        super().__init__(name, version, size_gb)
        self._tables = {}

    def create_table(self, table_name: str):
        self._tables[table_name] = []

    def insert_data(self, table_name: str, data: str):
        if table_name not in self._tables:
            raise ComponentNotFoundError("Таблица не найдена.")
        self._tables[table_name].append(data)

class Server(ComputerCase):
    def __init__(self, name: str, manufacturer: str, form_factor: str, rack_units: int):
        super().__init__(name, manufacturer, form_factor)
        self._rack_units = rack_units
        self._is_online = False

    def power_on(self):
        self._is_online = True
        return f"Сервер {self._name} запущен."

    def handle_request(self, request: str) -> str:
        if not self._is_online:
            raise NetworkConnectionError("Сервер выключен.")
        return f"Запрос '{request}' обработан сервером {self._name}."


class Laptop(ComputerCase):
    def __init__(self, name: str, manufacturer: str, battery_capacity_wh: int):
        super().__init__(name, manufacturer, "Laptop")
        self._battery_capacity_wh = battery_capacity_wh
        self._battery_level = 100

    def discharge(self, hours: int):
        self._battery_level -= hours * 10
        if self._battery_level <= 0:
            raise InsufficientPowerError("Ноутбук разрядился.")

    def charge(self):
        self._battery_level = 100


class Printer(Peripheral):
    def __init__(self, name: str, interface: PortType, ink_level: int):
        super().__init__(name, interface)
        self._ink_level = ink_level

    def plug_in(self):
        self._is_connected = True
        return f"Принтер {self._name} подключен."

    def print_document(self, document_name: str):
        if self._ink_level <= 0:
            raise InvalidHardwareConfigError("Закончились чернила.")
        self._ink_level -= 10
        return f"Документ {document_name} распечатан."


class Scanner(Peripheral):
    def __init__(self, name: str, interface: PortType, resolution_dpi: int):
        super().__init__(name, interface)
        self._resolution_dpi = resolution_dpi

    def plug_in(self):
        self._is_connected = True
        return f"Сканер {self._name} подключен."

    def scan_document(self) -> str:
        if not self._is_connected:
            raise NetworkConnectionError("Сканер не подключен.")
        return f"Документ отсканирован в {self._resolution_dpi} dpi."


class Webcam(Peripheral):
    def __init__(self, name: str, interface: PortType, has_microphone: bool):
        super().__init__(name, interface)
        self._has_microphone = has_microphone

    def plug_in(self):
        self._is_connected = True
        return f"Веб-камера {self._name} подключена."

    def record_video(self, duration_sec: int) -> str:
        if not self._is_connected:
            raise NetworkConnectionError("Веб-камера не подключена.")
        return f"Записано {duration_sec} секунд видео."


class Microphone(Peripheral):
    def __init__(self, name: str, interface: PortType, sensitivity_db: int):
        super().__init__(name, interface)
        self._sensitivity_db = sensitivity_db

    def plug_in(self):
        self._is_connected = True
        return f"Микрофон {self._name} подключен."

    def record_audio(self) -> str:
        if not self._is_connected:
            raise NetworkConnectionError("Микрофон не подключен.")
        return f"Аудио записано с чувствительностью {self._sensitivity_db} dB."


class Speaker(Peripheral):
    def __init__(self, name: str, interface: PortType, power_watts: int):
        super().__init__(name, interface)
        self._power_watts = power_watts

    def plug_in(self):
        self._is_connected = True
        return f"Колонки {self._name} подключены."

    def play_sound(self, sound_name: str) -> str:
        if not self._is_connected:
            raise NetworkConnectionError("Колонки не подключены.")
        return f"Воспроизведение: {sound_name}"


class Firewall(Software):
    def __init__(self, name: str, version: str, size_gb: float):
        super().__init__(name, version, size_gb)
        self._blocked_ips = set()

    def block_ip(self, ip: str):
        self._blocked_ips.add(ip)

    def check_ip(self, ip: str):
        if ip in self._blocked_ips:
            raise NetworkConnectionError(f"Доступ с IP {ip} заблокирован.")


class CloudStorage(Storage):
    def __init__(self, name: str, provider: str, capacity_gb: int):
        super().__init__(name, provider, capacity_gb, is_ssd=True, power_draw=0)
        self._provider = provider

    def connect(self) -> str:
        return f"Облачное хранилище {self._provider} доступно."

    def sync(self) -> str:
        return f"Синхронизация с {self._provider} завершена."


class Sensor(Component):
    def __init__(self, name: str, manufacturer: str, sensor_type: str, power_draw: int):
        super().__init__(name, manufacturer, power_draw)
        self._sensor_type = sensor_type

    def connect(self) -> str:
        return f"Датчик {self._name} ({self._sensor_type}) активирован."

    def read_data(self) -> float:
        return 25.0


class TemperatureSensor(Sensor):
    def __init__(self, name: str, manufacturer: str, power_draw: int):
        super().__init__(name, manufacturer, "Temperature", power_draw)

    def read_data(self) -> float:
        return 45.5


class FanSensor(Sensor):
    def __init__(self, name: str, manufacturer: str, power_draw: int):
        super().__init__(name, manufacturer, "Fan Speed", power_draw)

    def read_data(self) -> float:
        return 1200.0


class PCBuilder:
    def __init__(self):
        self._components = []

    def add_component(self, component: Component):
        self._components.append(component)

    def calculate_total_power(self) -> int:
        return sum(c._power_draw for c in self._components)

    def build(self) -> str:
        return f"Сборка завершена. Компонентов: {len(self._components)}."


if __name__ == "__main__":
    print("=" * 50)
    print("ЗАПУСК ТЕСТОВОГО СЦЕНАРИЯ СБОРКИ КОМПЬЮТЕРА")
    print("=" * 50)

    print("\n--- 1. Создание комплектующих ---")
    cpu = CPU(name="Core i9", manufacturer="Intel", cores=8, frequency=3.5, socket="LGA1700", power_draw=125)
    gpu = GPU(name="RTX 4090", manufacturer="NVIDIA", vram=24, power_draw=450)
    ram = RAM(name="DDR5", manufacturer="Kingston", capacity_gb=16, speed_mhz=6000, power_draw=10)
    storage = Storage(name="NVMe SSD", manufacturer="Samsung", capacity_gb=1000, is_ssd=True, power_draw=5)
    psu = PowerSupply(name="SuperNOVA", manufacturer="EVGA", max_wattage=850)
    motherboard = Motherboard(name="Z790", manufacturer="ASUS", socket="LGA1700", power_draw=50)
    case = ComputerCase(name="Dark Base", manufacturer="be quiet!", form_factor="ATX")

    print(f"Создан процессор: {cpu.get_info()}")
    print(f"Создана видеокарта: {gpu.get_info()}")

    print("\n--- 2. Сборка компьютера ---")
    try:
        motherboard.install_component(cpu)
        motherboard.install_component(ram)
        motherboard.install_component(gpu)
        print(motherboard.connect())
        case.add_part(motherboard)
        print(case.connect())
    except IncompatibleSocketError as e:
        print(f"Ошибка сборки: {e}")

    print("\n--- 3. Проверка блока питания ---")
    total_power = cpu._power_draw + gpu._power_draw + ram._power_draw + storage._power_draw + motherboard._power_draw
    try:
        psu.check_power(total_power)
        print(f"Питания достаточно. Потребление: {total_power}W из {psu._max_wattage}W")
    except InsufficientPowerError as e:
        print(f"Ошибка питания: {e}")

    print("\n--- 4. Установка ОС и софта ---")
    windows = OperatingSystem(name="Windows 11", version="23H2", size_gb=40.0, family=OSFamily.WINDOWS)
    windows.install(storage)
    print(windows.boot(ram))

    driver = Driver(name="NVIDIA Drivers", version="550.09", size_gb=1.5, target_device="RTX 4090")
    driver.install(storage)
    print(driver.load())

    print("\n--- 5. Запуск игры и перегрев ---")
    cyberpunk = Game(name="Cyberpunk 2077", version="2.0", size_gb=70.0, min_gpu_vram=8)
    try:
        print(cyberpunk.launch(gpu))
        print(cyberpunk.execute(cpu, ram))
    except MemoryOverflowError as e:
        print(f"Ошибка памяти: {e}")

    print("\n--- 6. Тест системы охлаждения ---")
    cooler = CoolingSystem(name="NH-D15", manufacturer="Noctua", fan_count=2, power_draw=5)
    print(cooler.connect())

    print(f"Текущая температура CPU: {cpu._temperature}°C")
    try:
        cpu.heat_up(50.0)
        cpu.heat_up(20.0)
    except OverheatingError as e:
        print(f"КРИТИЧЕСКАЯ ОШИБКА: {e}")
        print("Запуск аварийного охлаждения...")
        cooler.start_cooling(cpu)
        print(f"Температура после охлаждения: {cpu._temperature}°C")

    print("\n--- 7. Действия администратора ---")
    admin = SystemAdministrator(username="root", password_hash="super_secret_hash", root_level=10)
    try:
        admin.login("wrong_password")
    except PermissionDeniedError as e:
        print(f"Отказ в доступе: {e}")

    print(admin.login("super_secret_hash"))
    print(admin.kill_process("Cyberpunk 2077", windows))

    print("\n" + "=" * 50)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО")
    print("=" * 50)

