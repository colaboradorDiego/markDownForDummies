# markDownForDummies
Standarize docs with markdown and full text search in pyhton

# Introduccion
Partiendo de una carpeta llena de subcarpetas y documentos markdown deseamos meterlos en una db habilitada con full text search y asi indexar todo para que posteriormente sea muy facil buscarlo.
El programa va a producin un archivo sql con las instrucciones para crear la database y los insert correspondiendes.


Pero para que los datos sean facil de buscalos debemos crear reglas para organizar en primer lugar los datos y luego organizarlos en la database.

## Datos en carpetas y con el formato markdown

### Reglas para los nombres de carpetas y archivos

La estructura de folders tiene las siguientes caracteristicas:
1. el nombre de la carpeta define la categoria, ejemplo: si tenemos una carpeta "linux" todo su contenido es sobre el tema "linux"
2. las subcaretas afinan la busquesa sobre la carpeta de mayor gerarquia, ejemplo, la carpeta "linux/firewall" indica que todo su contenido esta relacionado con temas de firewall pero solo de linux.
3. asi podemos tener varios niveles que afinan la busqueda cada vez mas.
4. los nombres de archivos finalmente terminan de afinar aun mas el contenido, ejemplo, "linux/firewall/ufw.txt" indica que los datos hablan sobre "ufw" que es un "firewall" para "linux"


Teniendo esto en cuenta, cuando vamos a volcar los datos a la database cada nombre de carpeta se transforma en un tag de busqueda, asi tambien el nombre del archivo (sin la extension) tambien se transforma en otro tag de busqueda.
De esta manera todo el texto del archivo tendra todos esos tag que haran que el resultado de la busqueda aparezca por delante de otros en caso de que la busqueda conicida con alguno de estos tags.



# System Setup
Database
tag - texto






## Para una segunda etapa si es necesario podemos analizar el markdown para afinar aun mas las busquedas.

Docs [PyPandoc](https://pypi.org/project/pypandoc/)

mdSimpleParser.py



cuando convertimos md to json obtenemos una estructura de la sigueinte:
"blocks": [
	{},
	{},
	{}
]

tipos de bloques:
TITULO:

	{
		"t": "Header",
		"c": [
			1,
			[
				"what-is-markdown",
				[],
				[]
			],
			[]
		]
	}
	
	#   -> 1
	##  -> 2
	### -> 3
 
LINK:
    {
      "t": "Para",
      "c": [
        {
          "t": "Str",
          "c": "Docs"
        },
        {
          "t": "Space"
        },
        {
          "t": "Link",
          "c": [
            [
              "",
              [],
              []
            ],
            [
              {
                "t": "Str",
                "c": "Referencia"
              },
              {
                "t": "Space"
              },
              {
                "t": "Str",
                "c": "basica"
              }
            ],
            [
              "https://www.markdownguide.org/getting-started/",
              ""
            ]
          ]
        }
      ]
    },
