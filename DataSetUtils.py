import csv


def to_number(x):
    try:
        return float(x)
    except:
        return None


def clear_dataset(input_path, output_path):
    data = []

    # ler csv manualmente
    with open(input_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            # substituir ? por None e converter
            row = [to_number(x if x != "?" else None) for x in row]
            data.append(row)

    # remover linhas com None
    data = [row for row in data if None not in row]

    # substituir classe (coluna 10)
    for row in data:
        if row[10] == 2:
            row[10] = 0
        elif row[10] == 4:
            row[10] = 1

    # remover coluna 0
    for row in data:
        del row[0]

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def get_data(input_path) -> list[float]:
    data: list[float] = []

    # ler csv manualmente
    with open(input_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            # substituir ? por None e converter
            row = [to_number(x if x != "?" else None) for x in row]
            data.append(row)

    # remover linhas com None
    data = [row for row in data if None not in row]

    return data
