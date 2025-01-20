from dataclasses import dataclass, field


@dataclass
class HttpResponseDto:
    response_code: int = field(default=0)
    status: str = field(default="")
    message: str = field(default="")
    data: [] = field(default="")

