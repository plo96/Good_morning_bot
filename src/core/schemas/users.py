from dataclasses import dataclass



@dataclass
class UserDTO:
    _id: int
    name: str
    lat: float
    lon: float
    sex: str
    wake_up_time: str
    job_id: str
