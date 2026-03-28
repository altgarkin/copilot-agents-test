
def calculate_totals(data, rate=1.15):
    """Verilen verileri oranla çarpar ve yeni liste döndürür."""
    return [d * rate for d in data]

def print_totals(totals):
    """Her toplamı ekrana yazdırır."""
    for val in totals:
        print(f"Total: {val:.2f}")

def write_totals_to_file(totals, filename="log.txt"):
    """Toplamları dosyaya yazar."""
    with open(filename, "a") as f:
        f.write(str(totals) + "\n")

def process_data(data):
    """Veriyi işler: hesaplar, ekrana ve dosyaya yazar."""
    totals = calculate_totals(data)
    print_totals(totals)
    write_totals_to_file(totals)
    return totals
