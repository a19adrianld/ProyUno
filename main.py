from ventana import *
import sys, var, events, clients

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MaiPrincipal()
        var.ui.setupUi(self)

        '''
        conexion de eventos con los objetos
        '''
        var.ui.BtnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.ActionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.EditDNI.editingFinished.connect(clients.Clientes)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show
    sys.exit(app.exec())