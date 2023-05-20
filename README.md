# TrashCity
Descripcion: 
El código de la empresa "TrashCity" representa un sistema de recolección y acopio de residuos.
El código aqui expuesto muestra dos zonas:
1. una primera en la que se declaran las clases y metodos necesarios para cumplir con el requerimiento principal, que supone mostrar el cálculo de la cantidad de vidrio
que se recogió en todas las rutas de un día en específico. 
El sistema funciona con una clase turno que tiene toda la informacion para llevar un registro de los residuos que se recogieron, en que parte, cuanta cantidad y finalmente un metodo para devolver la cantidad de vidrio en ese turno.
Posteriormente nos encontramos con la clase centro de acopio que cuenta con el metodo para obtener la cantidad de vidrio que se recolecto durante un dia, tomando la cantidad recolectada de todos los turnos que se dieron en un mismo dia.
2. la segunda zona es una  tipo prueba de intregración en la que se asignan valores y se instancian clases necesarias para el funcionamiento del codigo. En este caso se le asignan cantidades fijas de vidrio a los dos puntos por donde se le asigna pasar al camión, 
 y con esto se realiza una prueba unittest del metodo getGlassTotal y despues se hace la prueba de manera mas basica para dar ejemplo de uso del codigo. 

Instrucciones de instalación: El codigo solo requiere ser descargado como zip, descomprimido y ejecutado como hoja de codigo en el IDE de preferencia, como referencia se uso PyCharm de JetBrains.

Intrucciones de uso: Para usar el codigo se encuentra como referencia la "prueba de integración", ya que en este apartado del codigo se instancian las clases necesarias y se define que se esta instanciando en cada caso, el usuario puede tomar estos valores de referencia y editarlos a gusto para obtener los calculos que necesite. 
