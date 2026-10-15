# Вспомогательные функции для работы с FASTQ файлами
# Нормализует границы интервала. Если передано одно число, делает его верхней границей, а нижнюю ставит по умолчанию.

def normalize_bounds(bounds, default_min, default_max):
    if isinstance(bounds, (int, float)):
        return (default_min, bounds)
    else:
        return bounds
def calculate_gc_percent(sequence):
    """
    Считает процент GC-состава в последовательности.
    Формула: (количество G + количество C) / длина × 100%
    """
    seq_upper = sequence.upper()
    gc_count = seq_upper.count('G') + seq_upper.count('C')
    if len(sequence) == 0:
        return 0.0
    return (gc_count / len(sequence)) * 100
# Качество нуклеотида = ASCII-код символа − 33
def calculate_avg_quality(quality_string):
    if not quality_string:
        return 0.0
    total_quality = 0
    for char in quality_string:
        ascii_code = ord(char)
        quality_score = ascii_code - 33
        total_quality = total_quality + quality_score
    avg_quality = total_quality / len(quality_string)
    return avg_quality
# Проверяет, попадает ли длина последовательности в заданный интервал.
def check_length(sequence, length_bounds):
    length = len(sequence)
    min_length = length_bounds[0]  
    max_length = length_bounds[1] 
    if length >= min_length and length <= max_length:
        return True
    else:
        return False

# Проверяет, попадает ли GC-состав в заданный интервал.
def check_gc(sequence, gc_bounds):
    gc_percent = calculate_gc_percent(sequence)
    min_gc = gc_bounds[0]
    max_gc = gc_bounds[1]
    if gc_percent >= min_gc and gc_percent <= max_gc:
        return True
    else:
        return False

# Проверяет, выше ли среднее качество ридов порогового значения.
def check_quality(quality_string, quality_threshold):
    avg_quality = calculate_avg_quality(quality_string)
    return avg_quality >= quality_threshold
