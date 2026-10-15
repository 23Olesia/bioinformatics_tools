import os
def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None):
    if output_fasta is None:
        name, ext = os.path.splitext(input_fasta)
        output_fasta = f"{name}_oneline{ext}"

    with open(input_fasta, 'r') as in_file, open(output_fasta, 'w') as out_file:
        current_header = None
        current_seq = []

        for line in in_file:
            line = line.rstrip('\n')
            if line.startswith('>'):
                if current_header is not None:
                    out_file.write(current_header + '\n')
                    out_file.write(''.join(current_seq) + '\n')
                current_header = line
                current_seq = []
            else:
                current_seq.append(line)

        if current_header is not None:
            out_file.write(current_header + '\n')
            out_file.write(''.join(current_seq) + '\n')

    return output_fasta
def parse_blast_output(input_file, output_file):
#Парсит BLAST output файл, извлекает первое описание из секции 
#"Sequences producing significant alignments:" для каждого QUERY,
#сортирует по алфавиту и сохраняет в выходной файл.
    descriptions = []
    with open(input_file, 'r') as file:
        lines = file.readlines()
    found_section = False
    skip_header_lines = False      

    for line in all_lines:
        clean = line.strip()

    #1.Ищем начало нужной секции
    if clean == "Sequences producing significant alignments:":
        found_section = True
        skip_header_lines = True
        continue
    if not found_section:
        continue

    # 2.Пропускаем пустые строки и строку с "Bit Score", пока они идут подряд
    if skip_header_lines:
        if clean == "" or "Bit Score" in clean:
            continue
        else:
            descriptions.append(clean)
            skip_header_lines = False
    descriptions.sort()
    with open(output_file, 'w') as f:
        for desc in descriptions:
            f.write(desc + '\n')
