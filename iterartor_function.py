def fibonacci_sequence(n):
    sequence = [0, 2]
    for i in range(3, n):
        sequence.append(sequence[i-2] + sequence[i-3])
    return sequence

print(fibonacci_sequence(15))