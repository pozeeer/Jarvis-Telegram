import platform

import psutil
import pythoncom
import wmi
from GPUtil import GPUtil


class ComputerCharacteristics:
    operating_system: str | None = None
    operating_system_version: str | None = None
    processor_name: str | None = None
    RAM_memory: str | None = None
    name_video_card: str | None = None

    def get_operating_system(self):
        self.operating_system = platform.system()
        return self.operating_system

    def get_operating_system_version(self):
        self.operating_system_version = platform.version()
        return self.operating_system_version

    def get_processor_name(self):
        pythoncom.CoInitialize()
        computer = wmi.WMI()
        info_about_processor = computer.Win32_Processor()[0]
        self.processor_name = info_about_processor.Name.rstrip()
        return self.processor_name

    def get_ram_memory(self):
        info_about_ram = psutil.virtual_memory().total
        correct_info_about_ram = (str(round(info_about_ram / (1024.0 ** 3))) + " GB")
        self.RAM_memory = correct_info_about_ram
        return self.RAM_memory

    def get_name_video_card(self):
        self.name_video_card = GPUtil.getGPUs()[0].name
        return self.name_video_card
