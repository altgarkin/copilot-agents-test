
def average_ratios(numbers):
    total = 0
    count = 0
    for n in numbers:
        if n == 0:
            print("Warning: Sıfıra bölme atlandı.")
            continue
        total += 100 / n
        count += 1
    if count == 0:
        return None  # Hiç geçerli değer yoksa
    return total / count

print(average_ratios([10, 5, 0]))
