import os

# Path to the original .nds file
nds_file_path = 'All Kamen Rider - Rider Generation.nds'
# Path to the output .nds file
output_nds_file_path = 'All Kamen Rider - Rider Generation_eng.nds'

# Definition of the files to be inserted and their offsets
files_to_insert = {
##    '01_00_eng.dat': (0x53e200, 8914),
##    '01_01_eng.dat': (0x540600, 9856),
##    '02_00_eng.dat': (0x542e00, 2457),
##    '02_01_eng.dat': (0x543800, 8031),
##    '02_02_eng.dat': (0x545800, 9611),
##    '03_00_eng.dat': (0x547e00, 10624),
##    '03_01_eng.dat': (0x54a800, 18042),
##    '04_00_eng.dat': (0x54F000, 13687),
##    '04_01_eng.dat': (0x552600, 11831),
##    '05_00_eng.dat': (0x555600, 34296),
##    '05_01_eng.dat': (0x55DC00, 9832),
##    'afterboss_02_eng.dat': (0x560600, 291),
##    'afterboss_03_eng.dat': (0x560800, 350),
##    'afterboss_04_eng.dat': (0x560A00, 345),
##    'epilogue_eng.dat': (0x560C00, 1429),
##    'prologue_eng.dat': (0x561200, 1324),
##    'ScriptName_eng.bin': (0x560400, 362),
    'New_Font.NFTR': (0x305C600, 22660)
}

# Copy original .nds file to new file
with open(nds_file_path, 'rb') as nds_file:
    with open(output_nds_file_path, 'wb') as output_nds_file:
        output_nds_file.write(nds_file.read())

# Insert modified files
with open(output_nds_file_path, 'r+b') as output_nds_file:
    for file_name, (offset, length) in files_to_insert.items():
        with open(file_name, 'rb') as input_file:
            data = input_file.read()
            if len(data) != length:
                print(f"Error: The file {file_name} has an incorrect size.")
                continue
            output_nds_file.seek(offset)
            output_nds_file.write(data)

print("Insertion completed.")
