import os
import shutil
import codecs

# Read each file
def read_bin_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return data

def is_shift_jis(byte1, byte2):
    return (0x81 <= byte1 <= 0x9F or 0xE0 <= byte1 <= 0xFC) and (0x40 <= byte2 <= 0x7E or 0x80 <= byte2 <= 0xFC)

def extract_strings(data):
    blocks = []
    i = 0
    while i < len(data) - 1:
        if is_shift_jis(data[i], data[i + 1]):
            length = data[i - 1]  
            start_offset = i - 1
            end_offset = i + length
            string_data = data[i:i + length]

            if blocks and blocks[-1][0] + sum(blocks[-1][1]) + len(blocks[-1][1]) == start_offset:
                last_block = blocks.pop()
                combined_lengths = last_block[1] + [length]
                combined_data = last_block[2] + data[last_block[0] + sum(last_block[1]) + len(last_block[1]):start_offset] + string_data
                blocks.append((last_block[0], combined_lengths, combined_data))
            else:
                blocks.append((start_offset, [length], string_data))
            i = end_offset
        else:
            i += 1
    return blocks

def convert_to_shift_jis(blocks):
    sjis_strings = []
    for start_offset, lengths, string_data in blocks:
        decoded_strings = []
        current_offset = 0
        for length in lengths:
            try:
                sjis_string = codecs.decode(string_data[current_offset:current_offset + length], 'shift_jis')
                decoded_strings.append((length, sjis_string))
            except Exception as e:
                decoded_strings.append((length, f'Error decoding string: {e}'))
            current_offset += length
        sjis_strings.append((start_offset, decoded_strings))
    return sjis_strings

def write_to_file(blocks, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for block_index, (start_offset, strings) in enumerate(blocks):
            f.write(f'Block{block_index + 1} 0x{start_offset:X}\n')
            for length, string in strings:
                f.write(f'({length:02X}){string}\n')
            f.write('\n')

def process_file(file_path):
    dump_file_path = f"{file_path.split('.')[0]}_jap.txt"
    data = read_bin_file(file_path)
    blocks = extract_strings(data)
    sjis_strings = convert_to_shift_jis(blocks)
    write_to_file(sjis_strings, dump_file_path)
    
    # Define the folders
    inserter_folder = "Inserter"
    eng_folder = os.path.join(inserter_folder, "Eng")
    
    # Create folders if they don't exist
    if not os.path.exists(inserter_folder):
        os.makedirs(inserter_folder)
    if not os.path.exists(eng_folder):
        os.makedirs(eng_folder)
    
    # Move files to respective folders
    if os.path.exists(dump_file_path):
        shutil.move(dump_file_path, os.path.join(inserter_folder, os.path.basename(dump_file_path)))
    
    if os.path.exists(file_path):
        shutil.move(file_path, os.path.join(eng_folder, os.path.basename(file_path)))

def main():
    files = [
        '01_00.dat',
        '01_01.dat',
        '02_00.dat',
        '02_01.dat', 
        '02_02.dat',
        '03_00.dat',
        '03_01.dat', 
        '04_00.dat',
        '04_01.dat',
        '05_00.dat',
        '05_01.dat',
        'afterboss_02.dat',
        'afterboss_03.dat',
        'afterboss_04.dat',
        'epilogue.dat',
        'prologue.dat',
        'ScriptName.bin'
    ]
    
    for file in files:
        process_file(file)
    
    print("Process successfully completed.")

if __name__ == '__main__':
    main()
