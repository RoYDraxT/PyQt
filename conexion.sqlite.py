import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQtUI import Ui_MainWindow  # Importa la clase generada

# Importar el archivo de lectura
from lectura import cargar_datos

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Establecer la página inicial a la página 'page'
        self.ui.stackedWidget.setCurrentIndex(0)  # Asegura que la página inicial sea 'page'
        
        # Conectar los botones
        self.ui.bt_view.clicked.connect(self.mostrar_datos)
        self.ui.bt_regresar.clicked.connect(self.regresar_a_page)
        self.ui.bt_cerrar.clicked.connect(self.close)
        self.ui.bt_exp.clicked.connect(self.toggle_fullscreen)
        self.ui.bt_min.clicked.connect(self.showMinimized)
        
        # Ocultar el botón `bt_cont`
        self.ui.bt_cont.setVisible(False)
    
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
        """Regresar a la página principal"""
        self.ui.stackedWidget.setCurrentIndex(0)  # El índice 0 corresponde a la página 'page'
    
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
