import shutil
import os

def read_dump_file(file_path):
    strings = []
    start_offset = None
    end_offset = None
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('Block'):
                if start_offset is not None and strings:
                    end_offset = start_offset + sum(len(s.encode('shift_jis')) + 1 for _, s in strings) - 1
                    yield start_offset, end_offset, strings
                block_info = line.split()
                start_offset = int(block_info[1], 16)
                strings = []
            elif line.strip() and line.startswith('('):
                length_hex = line.strip()[1:3]
                text = line.strip()[4:]
                length = int(length_hex, 16)
                strings.append((length, text))
        if start_offset is not None and strings:
            end_offset = start_offset + sum(len(s.encode('shift_jis')) + 1 for _, s in strings) - 1
            yield start_offset, end_offset, strings

def convert_to_shift_jis(strings):
    replacements = {
        "'": b'\x81\x4A',
    }
    shift_jis_strings = []
    for length, string in strings:
        shift_jis_encoded = string.encode('shift_jis', errors='replace')
        for char, replacement in replacements.items():
            shift_jis_encoded = shift_jis_encoded.replace(char.encode('shift_jis'), replacement)
        shift_jis_strings.append((length, shift_jis_encoded))
    return shift_jis_strings

def update_lengths(shift_jis_strings):
    updated_strings = []
    for _, string in shift_jis_strings:
        actual_length = len(string)
        updated_strings.append((actual_length, string))
    return updated_strings

def write_to_bin_file(bin_file_path, binary_strings, start_offset, end_offset):
    max_length = end_offset - start_offset + 1
    total_length = sum(len(data) + 1 for _, data in binary_strings)

    if total_length > max_length:
        raise ValueError("Too much text")

    with open(bin_file_path, 'r+b') as f:
        f.seek(start_offset)
        for length, binary_data in binary_strings:
            f.write(bytes([length]))
            f.write(binary_data)
        remaining_space = max_length - total_length
        f.write(bytes([0] * remaining_space))

def process_file(bin_file_name):
    dump_file_name = bin_file_name.replace('.dat', '_jap.txt')
    # Mantener la misma extensión para el archivo sobrescrito
    new_bin_file_name = bin_file_name.replace('.dat', '_eng.dat').replace('.bin', '_eng.bin')

    if not os.path.exists(dump_file_name):
        print(f"Archivo dump no encontrado: {dump_file_name}")
        return

    # Copiar el archivo original a uno nuevo con la misma extensión
    shutil.copyfile(bin_file_name, new_bin_file_name)

    for start_offset, end_offset, strings in read_dump_file(dump_file_name):
        shift_jis_strings = convert_to_shift_jis(strings)
        updated_shift_jis_strings = update_lengths(shift_jis_strings)
        write_to_bin_file(new_bin_file_name, updated_shift_jis_strings, start_offset, end_offset)

    print(f"Proceso completado para {bin_file_name} con éxito.")

def main():
    files = [
        '01_00.dat', '01_01.dat', '02_00.dat', '02_01.dat', 
        '02_02.dat', '03_00.dat', '03_01.dat', '04_00.dat', 
        '04_01.dat', '05_00.dat', '05_01.dat', 'afterboss_02.dat', 
        'afterboss_03.dat', 'afterboss_04.dat', 'epilogue.dat', 
        'prologue.dat', 'ScriptName.bin'
    ]

    for file_name in files:
        process_file(file_name)

if __name__ == '__main__':
    main()
