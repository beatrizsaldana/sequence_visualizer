import dataclasses
from typing import List, Literal
from get_sequences_functions import (
    get_fibonacci_sequence,
    get_mod_of_sequence
)
from find_repeating_sequence import find_repeating_sequence

Num = Union[int, float]


@dataclass
class Series:
    squence = List[Num]
    name = Literal["base", "fibonacci", "square"]

    @classmethod
    def from_known_sequence(cls, name: str, length: int = 16):
        if name == "fibonacci":
            return cls(
                squence=get_fibonacci_sequence(length=length),
                name=name
            )
        else:
            return cls(
                sequence=[0,1,2,3,4,5,6,7,8,9,10,11,16]
                name="base"
            )
    
    @property
    def get_mod_sequence(self, divisor) -> List[int]:
        mod_sequence = get_mod_of_sequence(input_sequence=self.sequence, divisor=divisor)
        return find_repeating_sequence(mod_sequence)
