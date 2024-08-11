import os

# Path to the .nds file
nds_file_path = 'All Kamen Rider - Rider Generation.nds'

# Definition of the files to be extracted and their offsets
files_to_extract = {
    '01_00.dat': (0x53e200, 8914),
    '01_01.dat': (0x540600, 9856),
    '02_00.dat': (0x542e00, 2457),
    '02_01.dat': (0x543800, 8031),
    '02_02.dat': (0x545800, 9611),
    '03_00.dat': (0x547e00, 10624),
    '03_01.dat': (0x54a800, 18042),
    '04_00.dat': (0x54F000, 13687),
    '04_01.dat': (0x552600, 11831),
    '05_00.dat': (0x555600, 34296),
    '05_01.dat': (0x55DC00, 9832),
    'afterboss_02.dat': (0x560600, 291),
    'afterboss_03.dat': (0x560800, 350),
    'afterboss_04.dat': (0x560A00, 345),
    'epilogue.dat': (0x560C00, 1429),
    'prologue.dat': (0x561200, 1324),
    'ScriptName.bin': (0x560400, 362),
    #'Font1212R_Base14Lite.NFTR': (0x305C600, 22660)
}

# Extract the files
with open(nds_file_path, 'rb') as nds_file:
    for file_name, (offset, length) in files_to_extract.items():
        nds_file.seek(offset)
        data = nds_file.read(length)
        with open(file_name, 'wb') as output_file:
            output_file.write(data)

print("Extraction completed.")
