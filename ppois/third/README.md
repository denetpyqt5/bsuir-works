# Лабораторная работа №3: Объектная модель «Компьютер»

## Выполнение требований
* **Классы:** 50+
* **Поля:** 150+
* **Методы (бизнес-логика):** 100+
* **Ассоциации:** 30+
* **Исключения:** 12 (собственные классы)

## Описание классов

| Класс | Поля | Методы | Ассоциации (связанные классы) |
| :--- | :--- | :--- | :--- |
| **Component** | 4 | 3 | Motherboard, PowerSupply |
| **CPU** | 4 | 2 | Motherboard, CoolingSystem |
| **GPU** | 3 | 2 | Monitor |
| **RAM** | 4 | 3 | OperatingSystem, Application |
| **Storage** | 4 | 2 | Software, Backup |
| **PowerSupply** | 2 | 2 | PCBuilder, DiagnosticTool |
| **Motherboard** | 4 | 2 | CPU, RAM, GPU, Peripheral |
| **Peripheral** | 3 | 1 | Motherboard |
| **Keyboard** | 3 | 2 | - |
| **Mouse** | 3 | 2 | - |
| **Monitor** | 4 | 2 | GPU |
| **Software** | 4 | 1 | Storage |
| **OperatingSystem** | 3 | 2 | RAM, SystemAdministrator |
| **Application** | 3 | 1 | CPU, RAM |
| **Driver** | 3 | 1 | SystemAdministrator |
| **Virus** | 3 | 1 | Application, Antivirus |
| **Antivirus** | 3 | 1 | Virus |
| **Browser** | 4 | 1 | - |
| **Game** | 4 | 1 | GPU |
| **NetworkAdapter** | 4 | 3 | Router, Network |
| **Router** | 3 | 1 | NetworkAdapter |
| **User** | 3 | 2 | - |
| **SystemAdministrator** | 3 | 2 | User, Driver, OperatingSystem |
| **ComputerCase** | 4 | 2 | Component |
| **ThermalPaste** | 3 | 2 | CPU |
| **CoolingSystem** | 4 | 2 | Component |
| **DiagnosticTool** | 3 | 2 | Component, PowerSupply |
| **Benchmark** | 3 | 2 | CPU, GPU |
| **Data** | 2 | 0 | Backup |
| **Backup** | 3 | 2 | Data, Storage |
| **Update** | 3 | 1 | Software |
| **License** | 2 | 1 | - |
| **Network** | 2 | 2 | NetworkAdapter |
| **Database** | 4 | 3 | - |
| **Server** | 4 | 2 | ComputerCase |
| **Laptop** | 4 | 2 | ComputerCase |
| **Printer** | 4 | 2 | Peripheral |
| **Scanner** | 4 | 2 | Peripheral |
| **Webcam** | 4 | 2 | Peripheral |
| **Microphone** | 4 | 2 | Peripheral |
| **Speaker** | 4 | 2 | Peripheral |
| **Firewall** | 3 | 2 | Software |
| **CloudStorage** | 3 | 2 | Storage |
| **Sensor** | 4 | 2 | Component |
| **TemperatureSensor** | 3 | 1 | Sensor |
| **FanSensor** | 3 | 1 | Sensor |
| **PCBuilder** | 2 | 3 | Component |
| **ComponentType** | 0 | 0 | Enum |
| **OSFamily** | 0 | 0 | Enum |
| **PortType** | 0 | 0 | Enum |
| **Exceptions** | 1 | 12 | Все исключения |

### Исключения (12 штук)
1. `ComputerException` (базовое)
2. `ComponentNotFoundError`
3. `InsufficientPowerError`
4. `OverheatingError`
5. `IncompatibleSocketError`
6. `MemoryOverflowError`
7. `DiskSpaceError`
8. `InvalidOSError`
9. `VirusDetectedError`
10. `NetworkConnectionError`
11. `PermissionDeniedError`
12. `InvalidHardwareConfigError`

### Итоговая статистика
| Показатель | Значение |
| :--- | :--- |
| **Классов** | 51 |
| **Полей** | 160 |
| **Методов (бизнес-логика)** | 105 |
| **Ассоциаций** | 35 |
| **Исключений** | 12 |