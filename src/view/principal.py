from principal_ui import *
import model

class Principal(QtWidgets.QMainWindow, Ui_Root):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        #Conectando clicks
        #self.btnAyuda.clicked.connect(self.)
        self.btnLimpiar.clicked.connect(self.limpiarCampos)
        self.btnResolver.clicked.connect(self.resolver)
        
    def limpiarCampos(self):
        self.tfGramatica.setText("")
        
    def resolver(self):
        c = model.Chomsky
        c.init("")
        #print(f" {model.Chomsky.init(self.tfGramatica.getText())}")
        #self.tfFNC.setText()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Principal()
    window.show()
    app.exec_()