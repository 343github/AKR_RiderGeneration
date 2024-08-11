# AKR_RiderGeneration
Tools for extracting and inserting text into the game
All Kamen Rider: Rider Generation.

You will need a copy of your .nds rom "All Kamen Rider: Rider Generation.nds" and python 3

1-Place the rom in the All_Kamen_Rider_Rider_Generation folder.  
2-Run the file File_Extractor.py (Extract the files containing the text of the game)  
3-Run the file Text_Extractor.py (Extract the Japanese texts of the game to the Inserter folder and move the original files to the Eng folder)  
4-Translate the .txt files from the Inserter folder (When you finish translating just move the file to the Eng folder)  
5-With the translated texts in the Eng folder, run the file Text_Inserter.py (It will create the new translated files of the game)  
6-Run the Rom_Maker.py file to create a "_eng.nds" version of the game.  

Notes
The Rom_Maker.py file only inserts the new_font for the game.
To insert the files you just have to remove the comments from lines
10 to 27.
you can try inserting file by file if you prefer.


# AKR_RiderGeneration
Herramientas para extraer e insertar texto en el juego
All Kamen Rider: Rider Generation.

Necesitarás una copia de tu rom .nds "All Kamen Rider: Rider Generation.nds" y python 3

1-Coloca el rom en la carpeta All_Kamen_Rider_Rider_Generation  
2-Ejecuta el archivo File_Extractor.py (Extrae los archivos que contienen el texto del juego)  
3-Ejecuta el archivo Text_Extractor.py (Extrae los textos Japoneses del juego a la carpeta Inserter y mueve los archivos originales a la carpeta Eng)  
4-Traduce los archivos .txt de la carpeta Inserter (Cuando termines de traducir solo mueve el archivo a la carpeta Eng)  
5-Con los textos traducidos en la carpeta Eng, ejecuta el archivo Text_Inserter.py (Creará los nuevos archivos traducidos del juego)  
6-Ejecuta el archivo Rom_Maker.py para crear una version "_eng.nds" del juego.  

Notas:
El archivo Rom_Maker.py solo inserta la nueva fuente para el juego.  
para insertar los archivos solo debes remover los comentarios de las lineas  
10 a la 27.  
puedes probar insertando archivo por archivo si asi lo prefieres.  
