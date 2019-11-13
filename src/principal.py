from view.principal_ui import *
from model import Chomsky

class Principal(QtWidgets.QMainWindow, Ui_Root):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        #Conectando clicks
        #self.btnAyuda.clicked.connect(self.)
        self.btnLimpiar.clicked.connect(self.limpiarCampos)
        self.btnResolver.clicked.connect(self.resolver)
        self.btnCargarDatos.clicked.connect(self.cargarArchivo)
        
    def limpiarCampos(self):
        self.tfGramatica.clear()
        self.tfFNC.clear()
        
    def resolver(self):
        c = Chomsky
        try:
            data = self.tfGramatica.toPlainText()
            self.tfFNC.setText(c.init(data,"string"))
        except Exception as e:
            return
    
    def cargarArchivo(self):
        pass
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Principal()
    window.show()
    app.exec_()