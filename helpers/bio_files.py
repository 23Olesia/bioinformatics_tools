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
