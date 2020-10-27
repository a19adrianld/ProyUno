from ventana import *
import sys
import var
import events

class Main(QtWidgets.QMainWindow):
        def __init__(self):
            super(Main, self).__init__()
            var.ui = Ui_MaiPrincipal()
            var.ui.setupUi()
            '''
            conexion de eventos con los objetos
            '''
            var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
            var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

if __name__ == '__main__':
        app = QtWidgets.QApplication([])
        window = Main()
        window.show()
        sys.exit(app.exec())