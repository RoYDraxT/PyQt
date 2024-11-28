# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 600)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.head = QtWidgets.QFrame(self.frame)
        self.head.setMinimumSize(QtCore.QSize(0, 42))
        self.head.setStyleSheet("QFrame{\n"
"background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #000000ff;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(222,222,222);\n"
"border-radius:20px;\n"
"}")
        self.head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.head.setObjectName("head")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.head)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uni = QtWidgets.QPlainTextEdit(self.head)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.uni.setFont(font)
        self.uni.setFocusPolicy(QtCore.Qt.NoFocus)
        self.uni.setAcceptDrops(False)
        self.uni.setStyleSheet("QPlainTextEdit {\n"
"    border: 0px; /* Sin borde */\n"
"    font-size: 12pt; /* Tamaño de letra aumentado */\n"
"    text-align: center; /* Centrar el texto */\n"
"    padding: 5px; /* Añadir un poco de espacio alrededor del texto */\n"
"}\n"
"")
        self.uni.setObjectName("uni")
        self.horizontalLayout.addWidget(self.uni)
        self.bt_min = QtWidgets.QPushButton(self.head)
        self.bt_min.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_min.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/min3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_min.setIcon(icon)
        self.bt_min.setIconSize(QtCore.QSize(20, 20))
        self.bt_min.setObjectName("bt_min")
        self.horizontalLayout.addWidget(self.bt_min)
        self.bt_cont = QtWidgets.QPushButton(self.head)
        self.bt_cont.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_cont.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagenes/cont.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cont.setIcon(icon1)
        self.bt_cont.setIconSize(QtCore.QSize(20, 20))
        self.bt_cont.setObjectName("bt_cont")
        self.horizontalLayout.addWidget(self.bt_cont)
        self.bt_exp = QtWidgets.QPushButton(self.head)
        self.bt_exp.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_exp.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagenes/exp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_exp.setIcon(icon2)
        self.bt_exp.setIconSize(QtCore.QSize(20, 20))
        self.bt_exp.setObjectName("bt_exp")
        self.horizontalLayout.addWidget(self.bt_exp)
        self.bt_cerrar = QtWidgets.QPushButton(self.head)
        self.bt_cerrar.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_cerrar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagenes/x-cf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cerrar.setIcon(icon3)
        self.bt_cerrar.setIconSize(QtCore.QSize(20, 20))
        self.bt_cerrar.setObjectName("bt_cerrar")
        self.horizontalLayout.addWidget(self.bt_cerrar)
        self.verticalLayout_2.addWidget(self.head)
        self.body = QtWidgets.QFrame(self.frame)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_res = QtWidgets.QFrame(self.body)
        self.frame_res.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_res.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_res.setObjectName("frame_res")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_res)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_res)
        self.stackedWidget.setStyleSheet("QFrame {\n"
"    background-color: transparent; /* Fondo gris claro */\n"
"    border: 1px solid #dcdcdc; /* Borde gris claro */\n"
"    padding: 10px; /* Espaciado interno */;\n"
"    border: 0px; /* Sin bordes */;\n"
"}\n"
"\n"
"QLabel {\n"
"    font: 87 12pt \"Arial Black\"; /* Fuente gruesa y tamaño moderado */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: rgb(0,0,0); /* Texto oscuro */\n"
"    border: 0px; /* Sin bordes */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 0px; /* Sin borde externo */\n"
"    color: rgb(255,255,255); /* Texto blanco */\n"
"    border-bottom: 2px solid rgb(61,61,61); /* Línea inferior en gris oscuro */\n"
"    font: 75 12pt \"Times New Roman\"; /* Fuente clásica */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(222,222,222); /* Color inicial del botón */\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    color: rgb(61,61,61); /* Texto oscuro */\n"
"    font: 22 10pt \"Arial Black\"; /* Fuente corregida */\n"
"    border-radius: 15px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200,200,200); /* Color ligeramente más oscuro al pasar el mouse */\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    color: rgb(61,61,61); /* Mismo color de texto */\n"
"    font: 22 10pt \"Arial Black\";\n"
"    border-radius: 15px; /* Esquinas redondeadas */\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255,255,255); /* Fondo blanco */\n"
"    color: rgb(0,0,0); /* Texto negro */\n"
"    gridline-color: rgb(0,0,0); /* Color de líneas de la cuadrícula */\n"
"    font-size: 12pt;\n"
"    border: 0px; /* Sin borde */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(222,222,222); /* Fondo verde brillante */\n"
"    border: 0px; /* Sin borde */\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: rgb(200,200,200); /* Fondo gris oscuro */\n"
"    border: 0px; /* Sin borde */\n"
"}\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.title = QtWidgets.QLabel(self.page)
        self.title.setGeometry(QtCore.QRect(0, -10, 351, 41))
        self.title.setObjectName("title")
        self.text1 = QtWidgets.QPlainTextEdit(self.page)
        self.text1.setGeometry(QtCore.QRect(0, 30, 711, 81))
        self.text1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text1.setObjectName("text1")
        self.text2 = QtWidgets.QPlainTextEdit(self.page)
        self.text2.setGeometry(QtCore.QRect(0, 120, 711, 101))
        self.text2.setObjectName("text2")
        self.text3 = QtWidgets.QPlainTextEdit(self.page)
        self.text3.setGeometry(QtCore.QRect(0, 230, 711, 121))
        self.text3.setObjectName("text3")
        self.text4 = QtWidgets.QPlainTextEdit(self.page)
        self.text4.setGeometry(QtCore.QRect(0, 360, 711, 61))
        self.text4.setObjectName("text4")
        self.bt_ana = QtWidgets.QPushButton(self.page)
        self.bt_ana.setGeometry(QtCore.QRect(580, 430, 131, 31))
        self.bt_ana.setObjectName("bt_ana")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_filtro = QtWidgets.QFrame(self.page_2)
        self.frame_filtro.setGeometry(QtCore.QRect(-10, -20, 250, 491))
        self.frame_filtro.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_filtro.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_filtro.setStyleSheet("QFrame {\n"
"    background-color: rgb(255,255,255);\n"
"    border-radius: 15px; /* Para esquinas redondeadas */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(222,222,222); /* Color inicial del botón */\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    color: rgb(61,61,61); /* Texto oscuro */\n"
"    font: 22 10pt \"Arial Black\"; /* Fuente corregida (font en lugar de front) */\n"
"    border-radius: 15px; /* Para esquinas redondeadas */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200,200,200); /* Color ligeramente más oscuro al pasar el mouse */\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    color: rgb(61,61,61); /* Mismo color de texto */\n"
"    font: 22 10pt \"Arial Black\";\n"
"    border-radius: 15px; /* Para esquinas redondeadas */\n"
"\n"
"}\n"
"")
        self.frame_filtro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_filtro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_filtro.setObjectName("frame_filtro")
        self.bt_view = QtWidgets.QPushButton(self.frame_filtro)
        self.bt_view.setGeometry(QtCore.QRect(50, 30, 141, 31))
        self.bt_view.setObjectName("bt_view")
        self.bt_limpiar = QtWidgets.QPushButton(self.frame_filtro)
        self.bt_limpiar.setGeometry(QtCore.QRect(20, 250, 120, 30))
        self.bt_limpiar.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_limpiar.setObjectName("bt_limpiar")
        self.region = QtWidgets.QPlainTextEdit(self.frame_filtro)
        self.region.setGeometry(QtCore.QRect(10, 60, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.region.setFont(font)
        self.region.setObjectName("region")
        self.bt_ejecutar = QtWidgets.QPushButton(self.frame_filtro)
        self.bt_ejecutar.setGeometry(QtCore.QRect(120, 450, 120, 30))
        self.bt_ejecutar.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_ejecutar.setObjectName("bt_ejecutar")
        self.anio = QtWidgets.QPlainTextEdit(self.frame_filtro)
        self.anio.setGeometry(QtCore.QRect(10, 200, 91, 49))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.anio.setFont(font)
        self.anio.setObjectName("anio")
        self.anio_box = QtWidgets.QComboBox(self.frame_filtro)
        self.anio_box.setGeometry(QtCore.QRect(80, 210, 81, 20))
        self.anio_box.setObjectName("anio_box")
        self.anio_box.addItem("")
        self.anio_box.addItem("")
        self.anio_box.addItem("")
        self.anio_box.addItem("")
        self.anio_box.addItem("")
        self.anio_box.addItem("")
        self.anio_box.addItem("")
        self.anio_box.addItem("")
        self.anio_box.addItem("")
        self.costa = QtWidgets.QCheckBox(self.frame_filtro)
        self.costa.setGeometry(QtCore.QRect(30, 100, 80, 17))
        self.costa.setObjectName("costa")
        self.sierra = QtWidgets.QCheckBox(self.frame_filtro)
        self.sierra.setGeometry(QtCore.QRect(30, 120, 80, 17))
        self.sierra.setObjectName("sierra")
        self.selva = QtWidgets.QCheckBox(self.frame_filtro)
        self.selva.setGeometry(QtCore.QRect(30, 140, 80, 17))
        self.selva.setObjectName("selva")
        self.departamento = QtWidgets.QPlainTextEdit(self.frame_filtro)
        self.departamento.setGeometry(QtCore.QRect(10, 160, 141, 49))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.departamento.setFont(font)
        self.departamento.setObjectName("departamento")
        self.departamento_box = QtWidgets.QComboBox(self.frame_filtro)
        self.departamento_box.setGeometry(QtCore.QRect(130, 170, 111, 20))
        self.departamento_box.setObjectName("departamento_box")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.departamento_box.addItem("")
        self.frame_grafc = QtWidgets.QFrame(self.page_2)
        self.frame_grafc.setGeometry(QtCore.QRect(260, 250, 211, 191))
        self.frame_grafc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grafc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grafc.setObjectName("frame_grafc")
        self.grafica = QtWidgets.QLabel(self.frame_grafc)
        self.grafica.setGeometry(QtCore.QRect(10, 0, 101, 41))
        self.grafica.setObjectName("grafica")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_grafc)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 191, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.grafica_box = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.grafica_box.setContentsMargins(0, 0, 0, 0)
        self.grafica_box.setObjectName("grafica_box")
        self.resultado = QtWidgets.QPlainTextEdit(self.page_2)
        self.resultado.setGeometry(QtCore.QRect(270, 0, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resultado.setFont(font)
        self.resultado.setObjectName("resultado")
        self.frame_res_2 = QtWidgets.QFrame(self.page_2)
        self.frame_res_2.setGeometry(QtCore.QRect(270, 40, 461, 201))
        self.frame_res_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_res_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_res_2.setObjectName("frame_res_2")
        self.text_res = QtWidgets.QPlainTextEdit(self.frame_res_2)
        self.text_res.setGeometry(QtCore.QRect(10, 10, 441, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_res.setFont(font)
        self.text_res.setStyleSheet("QFrame {\n"
"    background-color: rgb(255,255,255);\n"
"    border-radius: 15px; /* Para esquinas redondeadas */\n"
"}")
        self.text_res.setPlainText("")
        self.text_res.setObjectName("text_res")
        self.bt_regresar1 = QtWidgets.QPushButton(self.page_2)
        self.bt_regresar1.setGeometry(QtCore.QRect(610, 440, 120, 30))
        self.bt_regresar1.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_regresar1.setObjectName("bt_regresar1")
        self.stackedWidget.addWidget(self.page_2)
        self.view = QtWidgets.QWidget()
        self.view.setObjectName("view")
        self.gridLayout = QtWidgets.QGridLayout(self.view)
        self.gridLayout.setObjectName("gridLayout")
        self.bt_regresar2 = QtWidgets.QPushButton(self.view)
        self.bt_regresar2.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_regresar2.setObjectName("bt_regresar2")
        self.gridLayout.addWidget(self.bt_regresar2, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(587, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.tabla_datos = QtWidgets.QTableWidget(self.view)
        self.tabla_datos.setObjectName("tabla_datos")
        self.tabla_datos.setColumnCount(0)
        self.tabla_datos.setRowCount(0)
        self.gridLayout.addWidget(self.tabla_datos, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.view)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.view)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_res)
        self.verticalLayout_2.addWidget(self.body)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trabajo Final"))
        self.uni.setPlainText(_translate("MainWindow", "Universidad San Ignacio de Loyola"))
        self.title.setText(_translate("MainWindow", "Gestión de Residuos Sólidos en Perú"))
        self.text1.setPlainText(_translate("MainWindow", "La gestión de residuos sólidos es uno de los mayores desafíos ambientales en Perú. A pesar de los esfuerzos actuales, una gran parte de los residuos no se maneja adecuadamente, lo que genera problemas de contaminación en suelos, agua y aire. Este proyecto propone el uso de tecnologías emergentes como Big Data, Machine Learning, Power BI y Python para optimizar la recolección, disposición y tratamiento de residuos sólidos."))
        self.text2.setPlainText(_translate("MainWindow", "Objetivos Clave:\n"
"\n"
"- Fortalecer la gestión de residuos sólidos con un enfoque metodológico, promoviendo la adecuada disposición y reciclaje.\n"
"\n"
"- Implementar un sistema integral de análisis de datos para identificar áreas prioritarias y mejorar la eficiencia de los rellenos sanitarios."))
        self.text3.setPlainText(_translate("MainWindow", "Soluciones Propuestas:\n"
"\n"
"- Recolección y disposición adecuada: Sistemas eficientes que aseguren la disposición final segura de residuos.\n"
"\n"
"- Monitoreo en tiempo real: Uso de sensores y tecnologías para optimizar rutas y reducir costos operativos.\n"
"\n"
"- Visualización de datos: Herramientas como PyQt5 para apoyar la toma de decisiones informadas."))
        self.text4.setPlainText(_translate("MainWindow", "Una gestión adecuada de residuos no solo reduce la contaminación y los riesgos para la salud pública, sino que también fomenta el desarrollo sostenible y puede crear empleos e ingresos adicionales."))
        self.bt_ana.setText(_translate("MainWindow", "Realizar Análisis"))
        self.bt_view.setText(_translate("MainWindow", "View Data"))
        self.bt_limpiar.setText(_translate("MainWindow", "Limpiar"))
        self.region.setPlainText(_translate("MainWindow", "Región:"))
        self.bt_ejecutar.setText(_translate("MainWindow", "Ejecutar"))
        self.anio.setPlainText(_translate("MainWindow", "Año:"))
        self.anio_box.setItemText(0, _translate("MainWindow", "---"))
        self.anio_box.setItemText(1, _translate("MainWindow", "2014"))
        self.anio_box.setItemText(2, _translate("MainWindow", "2015"))
        self.anio_box.setItemText(3, _translate("MainWindow", "2016"))
        self.anio_box.setItemText(4, _translate("MainWindow", "2017"))
        self.anio_box.setItemText(5, _translate("MainWindow", "2018"))
        self.anio_box.setItemText(6, _translate("MainWindow", "2019"))
        self.anio_box.setItemText(7, _translate("MainWindow", "2020"))
        self.anio_box.setItemText(8, _translate("MainWindow", "2021"))
        self.costa.setText(_translate("MainWindow", "Costa"))
        self.sierra.setText(_translate("MainWindow", "Cierra"))
        self.selva.setText(_translate("MainWindow", "Selva"))
        self.departamento.setPlainText(_translate("MainWindow", "Departamento:"))
        self.departamento_box.setItemText(0, _translate("MainWindow", "---"))
        self.departamento_box.setItemText(1, _translate("MainWindow", "Amazonas"))
        self.departamento_box.setItemText(2, _translate("MainWindow", "Ancash"))
        self.departamento_box.setItemText(3, _translate("MainWindow", "Apurimac"))
        self.departamento_box.setItemText(4, _translate("MainWindow", "Arequipa"))
        self.departamento_box.setItemText(5, _translate("MainWindow", "Ayacucho"))
        self.departamento_box.setItemText(6, _translate("MainWindow", "Cajamarca"))
        self.departamento_box.setItemText(7, _translate("MainWindow", "Callao"))
        self.departamento_box.setItemText(8, _translate("MainWindow", "Cusco"))
        self.departamento_box.setItemText(9, _translate("MainWindow", "Huancavelica"))
        self.departamento_box.setItemText(10, _translate("MainWindow", "Huanuco"))
        self.departamento_box.setItemText(11, _translate("MainWindow", "Ica"))
        self.departamento_box.setItemText(12, _translate("MainWindow", "Junin"))
        self.departamento_box.setItemText(13, _translate("MainWindow", "La Libertad"))
        self.departamento_box.setItemText(14, _translate("MainWindow", "Lambayeque"))
        self.departamento_box.setItemText(15, _translate("MainWindow", "Lima"))
        self.departamento_box.setItemText(16, _translate("MainWindow", "Loreto"))
        self.departamento_box.setItemText(17, _translate("MainWindow", "Madre De Dios"))
        self.departamento_box.setItemText(18, _translate("MainWindow", "Moquegua"))
        self.departamento_box.setItemText(19, _translate("MainWindow", "Pasco"))
        self.departamento_box.setItemText(20, _translate("MainWindow", "Piura"))
        self.departamento_box.setItemText(21, _translate("MainWindow", "Puno"))
        self.departamento_box.setItemText(22, _translate("MainWindow", "San Martin"))
        self.departamento_box.setItemText(23, _translate("MainWindow", "Tacna"))
        self.departamento_box.setItemText(24, _translate("MainWindow", "Tumbes"))
        self.departamento_box.setItemText(25, _translate("MainWindow", "Ucayali"))
        self.grafica.setText(_translate("MainWindow", "Gráfica"))
        self.resultado.setPlainText(_translate("MainWindow", "Resultado"))
        self.bt_regresar1.setText(_translate("MainWindow", "Regresar"))
        self.bt_regresar2.setText(_translate("MainWindow", "Regresar"))
        self.label.setText(_translate("MainWindow", "DATOS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
