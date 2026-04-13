from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from typing import ClassVar

from app.services.util import (generate_unique_id, date_lower_than_today_error,
                               reservation_not_found_error, guest_not_found_error, room_not_available_error,
                               room_not_found_error, room_already_exists_error)


from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from typing import ClassVar

from app.services.util import (generate_unique_id, date_lower_than_today_error,
                               reservation_not_found_error, guest_not_found_error, room_not_available_error,
                               room_not_found_error, room_already_exists_error)


# TODO: Implement Guest class here
@dataclass
class Guest:
    RESULTADO: ClassVar[str] = "resultado"
    VIP: ClassVar[str] =  "vip"
    name: str
    email: str
    type_: str

    def __str__(self) -> str:
        pass

    # TODO: Implement Reservation class here


@dataclass
class Reservation:
    guest_name: str
    description: str
    check_in: date
    check_out: date
    id: str
    guests: list[Guest]


    def add_guest(self, name: str, email: str, type_: str) -> str:
        pass

    def delete_guest(self, guest_index) -> int:
        pass

    def __str__(self) -> str:
        pass

    def __len__(self) -> int:
        pass

# TODO: Implement Room class here

class Room :

    def __init__(self, number :  int, type_ : str, price_per_night : float):
        self.number = number
        self.type: = type_
        self.price_per_night = price_per_night
        self.availanility : dict = {}
        self._init_availability()


    def _init_availability(self): pass
    def book(self, reservation_id, check_in, check_out): pass




# TODO: Implement Hotel class here

