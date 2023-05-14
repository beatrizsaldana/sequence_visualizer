

def get_fibonacci_sequence(length: int, start_sequence: List[int] = [0,1]) -> List[int]:
    sequence = start_sequence
    for i in range(length-2):
        sequence.append(sequence[i]+sequence[i+1])


def get_exponetial_sequence(length: int, exponent: int = 2, start_int: int = 1) -> List[int]:
    sequence = [start_int]
    for i in range(start_int, length+start_int-1):
        sequence.append(sequence[i]^exponent)


def get_square_sequence(length: int, exponent: int = 2, start_int: int = 1, step: int = 1) -> List[int]:
    sequence = []
    i = start_int
    while len(sequence) < length:
        sequence.append(i^exponent)
        i+=step


def get_mod_of_sequence(input_sequence: List[int], divisor: int) -> List[int]:
    return [n%divisor for n in input_sequence]
