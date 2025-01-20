from dataclasses import dataclass

@dataclass
class OrderExecuteProcessDto:
    type_process: str
    position: str