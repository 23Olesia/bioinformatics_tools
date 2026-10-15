import os
from helpers.fastq import (
    normalize_bounds,
    check_length,
    check_gc,
    check_quality
)


def filter_fastq(input_fastq, output_fastq,
                 gc_bounds=(0, 100),
                 length_bounds = (0, 2**32),
                 quality_threshold=0):
    # 1. Нормализуем границы
    gc_bounds = normalize_bounds(gc_bounds, 0, 100)
    length_bounds = normalize_bounds(length_bounds, 0, 2**32)

    # 2. Создаём папку filtered/, если её ещё нет
    if not os.path.exists('filtered'):
       os.makedirs('filtered',exist_ok=True)
    # 3. Формируем полный путь к выходному файлу
    output_path = os.path.join('filtered', output_fastq)
    # 4. Открываем входной и выходной файлы
    # 'r' — чтение, 'w' — запись
    # Конструкция with гарантирует, что файлы закроются автоматически

    with open(input_fastq, 'r') as input_file, open(output_path, 'w') as output_file:
        while True:

            header = input_file.readline().strip()
            if not header:
                break
            sequence = input_file.readline().strip()
            plus = input_file.readline().strip()
            quality = input_file.readline().strip()
            if (check_length(sequence, length_bounds) and
                check_gc(sequence, gc_bounds) and
                check_quality(quality, quality_threshold)):
                # 5. Записываем рид в выходной файл
                output_file.write(f"{header}\n{sequence}\n{plus}\n{quality}\n")


# Этот блок запускается, только если файл запущен напрямую
if __name__ == "__main__":
    # Пример использования:
    filter_fastq(
        input_fastq="data/input.fastq",
        output_fastq="output.fastq",
        gc_bounds=(20, 80),
        length_bounds=(20, 80),
        quality_threshold=0
    )
