import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QListWidget, QVBoxLayout, QPushButton, QDialog, QDialogButtonBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQtUI import Ui_MainWindow  # Importa la clase generada
from procesos import transformar_datos, calcular_residuos_por_ano_seleccionado, calcular_residuos_por_region

# Importar el archivo de lectura
from procesos import cargar_datos

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Establecer la página inicial a la página 'page'
        self.ui.stackedWidget.setCurrentIndex(0)  # Asegura que la página inicial sea 'page'
        
        # Conectar los botones
        self.ui.bt_ana.clicked.connect(self.ir_a_page2)
        self.ui.bt_view.clicked.connect(self.mostrar_datos)
        self.ui.bt_regresar1.clicked.connect(self.regresar_a_page)
        self.ui.bt_regresar2.clicked.connect(self.regresar_a_page2)
        self.ui.bt_cerrar.clicked.connect(self.close)
        self.ui.bt_exp.clicked.connect(self.toggle_fullscreen)
        self.ui.bt_min.clicked.connect(self.showMinimized)
        self.ui.bt_ejecutar.clicked.connect(self.ejecutar_funcion)
        self.ui.bt_limpiar.clicked.connect(self.limpiar_filtros)

        # Ocultar el botón `bt_cont`
        self.ui.bt_cont.setVisible(False) 

    def limpiar_filtros(self):
        """
        Restablece los filtros y limpia el cuadro de resultados.
        """        
        # Restablecer valores de ComboBox
        self.ui.anio_box.setCurrentIndex(0)  # Selecciona la opción "Todos" en 'anio_box'
        self.ui.departamento_box.setCurrentIndex(0)  # Selecciona la opción "Todos" en 'anio_box'

        # Desmarcar todos los checkboxes (incluyendo Sierra)
        self.ui.costa.setChecked(False)
        self.ui.selva.setChecked(False)
        self.ui.sierra.setChecked(False)

        # Limpiar el cuadro de resultados
        self.ui.text_res.setPlainText("")  # Limpiar el resultado

    def ejecutar_funcion(self):
        """
        Maneja la funcionalidad del botón ejecutar en la interfaz.
        """
        datos = cargar_datos()

        if datos:
            # Transformar los datos
            datos_transformados = transformar_datos(datos)

            # Obtener el departamento seleccionado de la interfaz y convertirlo a mayúsculas
            departamento_seleccionado = self.ui.departamento_box.currentText().upper()  # Convertir a mayúsculas

            # Obtener el estado de los QCheckBox de las regiones
            region_costa = self.ui.costa.isChecked()  # Verifica si Costa está seleccionada
            region_sierra = self.ui.sierra.isChecked()  # Verifica si Sierra está seleccionada
            region_selva = self.ui.selva.isChecked()  # Verifica si Selva está seleccionada

            # Crear una lista de las regiones seleccionadas
            regiones_seleccionadas = []
            if region_costa:
                regiones_seleccionadas.append("COSTA")
            if region_sierra:
                regiones_seleccionadas.append("SIERRA")
            if region_selva:
                regiones_seleccionadas.append("SELVA")

            # Obtener el año seleccionado de la interfaz y convertirlo a mayúsculas
            año_seleccionado = self.ui.anio_box.currentText().upper()  # Convertir a mayúsculas

            mensaje = ""  # Inicializar el mensaje

            # Verificar si no se seleccionó ningún checkbox de región
            if len(regiones_seleccionadas) > 0:
                # Verificar si se ha seleccionado un departamento
                if departamento_seleccionado != "---":
                    mensaje = "No puedes seleccionar un departamento cuando estás analizando por regiones. Por favor, selecciona solo regiones o solo un departamento."
                elif año_seleccionado == "---":
                    mensaje = "Por favor seleccione un año válido."
                else:
                    # Filtrar los datos por las regiones seleccionadas
                    datos_por_region = datos_transformados[datos_transformados['REG_NAT'].isin(regiones_seleccionadas)]

                    # Filtrar los datos por el año seleccionado si es necesario
                    if año_seleccionado != "---":
                        datos_por_region = datos_por_region[datos_por_region['PERIODO'] == int(año_seleccionado)]

                    # Calcular los residuos totales de las regiones seleccionadas
                    residuos_totales = datos_por_region['QRESIDUOS_DOM'].sum()

                    mensaje = f"Residuos Totales para las Regiones {', '.join(regiones_seleccionadas)}: {residuos_totales} toneladas.\n"

                    # Calcular los residuos urbanos y rurales
                    residuos_urbanos = datos_por_region['QRESIDUOS_DOM'].sum() * (datos_por_region['POB_URBANA'].sum() / datos_por_region['POB_TOTAL'].sum())
                    residuos_rurales = datos_por_region['QRESIDUOS_DOM'].sum() * (datos_por_region['POB_RURAL'].sum() / datos_por_region['POB_TOTAL'].sum())

                    # Calcular los porcentajes
                    if residuos_totales > 0:
                        porcentaje_urbano = (residuos_urbanos / residuos_totales) * 100
                        porcentaje_rural = (residuos_rurales / residuos_totales) * 100
                    else:
                        porcentaje_urbano = 0
                        porcentaje_rural = 0

                    # Agregar los porcentajes al mensaje
                    mensaje += f"\nÁreas urbanas: {porcentaje_urbano:.2f}%."
                    mensaje += f"\nÁreas rurales: {porcentaje_rural:.2f}%. "
            else:
                # Si no se seleccionaron regiones, continuar con el filtro por departamento
                if (departamento_seleccionado == "---" or departamento_seleccionado == "TODOS") and año_seleccionado == "---":
                    mensaje = "No se establecieron correctamente los parámetros. Por favor seleccione un año y un departamento o región válidos."
                else:
                    if departamento_seleccionado == "TODOS" and año_seleccionado != "---":
                        residuos_totales = calcular_residuos_por_ano_seleccionado(datos_transformados, int(año_seleccionado))
                        if residuos_totales is not None:
                            mensaje = f"Residuos Totales para el Año {año_seleccionado}: {residuos_totales} toneladas."
                            if residuos_totales > 1500000:
                                mensaje += "\nSe necesitan acciones para la implementación de un relleno sanitario, ya que el total de residuos se encuentran en estado crítico.\n"
                            else:
                                mensaje += "\nLa cantidad de residuos generados se encuentra dentro de los límites de salubridad adecuados.\n"
                        else:
                            mensaje = "Error al calcular los residuos para el año seleccionado."
                    elif departamento_seleccionado != "---":
                        if año_seleccionado == "TODOS":
                            residuos_por_departamento = datos_transformados[datos_transformados['DEPARTAMENTO'] == departamento_seleccionado]
                            residuos_totales = residuos_por_departamento['QRESIDUOS_DOM'].sum()
                            mensaje = f"Residuos Totales para el Departamento {departamento_seleccionado}: {residuos_totales} toneladas.\n"
                            if residuos_totales > 1500000:
                                mensaje += "\nSe necesitan acciones para la implementación de un relleno sanitario, ya que el total de residuos se encuentran en estado crítico.\n"
                            else:
                                mensaje += "\nLa cantidad de residuos generados se encuentra dentro de los límites de salubridad adecuados.\n"
                            
                            # Calcular los porcentajes de residuos urbanos y rurales
                            residuos_urbanos = residuos_por_departamento['QRESIDUOS_DOM'].sum() * (residuos_por_departamento['POB_URBANA'].sum() / residuos_por_departamento['POB_TOTAL'].sum())
                            residuos_rurales = residuos_por_departamento['QRESIDUOS_DOM'].sum() * (residuos_por_departamento['POB_RURAL'].sum() / residuos_por_departamento['POB_TOTAL'].sum())
                            
                            # Calcular los porcentajes
                            porcentaje_urbano = (residuos_urbanos / residuos_totales) * 100
                            porcentaje_rural = (residuos_rurales / residuos_totales) * 100
                            
                            # Agregar los porcentajes al mensaje
                            mensaje += f"\nÁreas urbanas: {porcentaje_urbano:.2f}%."
                            mensaje += f"\nÁreas rurales: {porcentaje_rural:.2f}%. "
                        else:
                            datos_filtrados = datos_transformados[(datos_transformados['DEPARTAMENTO'] == departamento_seleccionado) & 
                                                                (datos_transformados['PERIODO'] == int(año_seleccionado))]
                            residuos_totales = datos_filtrados['QRESIDUOS_DOM'].sum()
                            mensaje = f"Residuos Totales para el Año {año_seleccionado} y el Departamento {departamento_seleccionado}: {residuos_totales} toneladas.\n"
                            if residuos_totales > 1500000:
                                mensaje += "\nSe necesitan acciones para la implementación de un relleno sanitario, ya que el total de residuos se encuentran en estado crítico.\n"
                            else:
                                mensaje += "\nLa cantidad de residuos generados se encuentra dentro de los límites de salubridad adecuados.\n"

                            # Calcular los porcentajes de residuos urbanos y rurales
                            residuos_urbanos = datos_filtrados['QRESIDUOS_DOM'].sum() * (datos_filtrados['POB_URBANA'].sum() / datos_filtrados['POB_TOTAL'].sum())
                            residuos_rurales = datos_filtrados['QRESIDUOS_DOM'].sum() * (datos_filtrados['POB_RURAL'].sum() / datos_filtrados['POB_TOTAL'].sum())
                            
                            # Calcular los porcentajes
                            porcentaje_urbano = (residuos_urbanos / residuos_totales) * 100
                            porcentaje_rural = (residuos_rurales / residuos_totales) * 100
                            
                            # Agregar los porcentajes al mensaje
                            mensaje += f"\nÁreas urbanas: {porcentaje_urbano:.2f}%."
                            mensaje += f"\nÁreas rurales: {porcentaje_rural:.2f}%. "
                    
            # Mostrar el mensaje final
            self.ui.text_res.setPlainText(mensaje)

    def ir_a_page2(self):
        """Cambiar a la página 'page2'"""
        self.ui.stackedWidget.setCurrentIndex(1)  # El índice 1 corresponde a la página 'page2'
    
    def mostrar_datos(self):
        """Carga y muestra los datos en la tabla y cambia a la página 'view'"""
        datos = cargar_datos()  # Llama la función del archivo `lectura.py`
        self.ui.tabla_datos.setRowCount(len(datos))
        self.ui.tabla_datos.setColumnCount(len(datos[0]))
        
        for i, fila in enumerate(datos):
            for j, valor in enumerate(fila):
                self.ui.tabla_datos.setItem(i, j, QTableWidgetItem(str(valor)))
        
        # Cambiar a la página 'view'
        self.ui.stackedWidget.setCurrentIndex(2)  # El índice 2 corresponde a la página 'view'
    
    def regresar_a_page(self):
        """Regresar a la página 'page'"""
        self.ui.stackedWidget.setCurrentIndex(0)  # El índice 0 corresponde a la página 'page'
    
    def regresar_a_page2(self):
        """Regresar a la página 'page2'"""
        self.ui.stackedWidget.setCurrentIndex(1)  # El índice 1 corresponde a la página 'page2'
    
    def toggle_fullscreen(self):
        """Alternar pantalla completa"""
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def toggle_expand_collapse(self):
        """Alternar entre expandir y contraer la ventana"""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
