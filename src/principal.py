import os
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
        self.btnAyuda.clicked.connect(self.ayuda)
        
        self.tfGramatica.setText("Terminales:\n\nVariables:\n\nProducciones:\n")
        
    def ayuda(self):
        if self.tfFNC.toPlainText()=="":
            self.tfFNC.setText('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;"><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">Esta aplicación permite generar de una gramática independiente de contexto (GIC) </span><span style=" font-size:9pt; font-style:italic;">G</span><span style=" font-size:9pt;"> a una GIC </span><span style=" font-size:9pt; font-style:italic;">G\'</span><span style=" font-size:9pt;"> en forma normal de Chomsky (FNC) equivalente a </span><span style=" font-size:9pt; font-style:italic;">G</span><span style=" font-size:9pt;">.</span></p><p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;"><br /></p><p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">Para usar, solo debe poner los símbolos terminales (debe especificar lambda %), variables y las producciones en el lado izquierdo (En las producciones se pone un punto y coma al final de cada una excepto en la última). </span><span style=" font-size:9pt; text-decoration: underline;">NO borrar el texto</span><span style=" font-size:9pt;"> que ya hay, escribir lo que se pide debajo del texto y separando por un solo espacio. El símbolo para denotar lambda λ en este programa es %. </span></p><p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;"><br /></p><p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">Una vez puesto todos los valores y de forma correcta, se debe dar clic en el botón &quot;Resolver&quot; de la parte de abajo y de esta manera aparecera en el lado derecho la gramática en FNC, de haber un error (como símbolos mal puestos o no acordes) aparecera un mensaje en esta misma parte informando que no se pudo generar la GIC </span><span style=" font-size:9pt; font-style:italic;">G\'</span></p><p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-style:italic;"><br /></p><p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">Existen otros botones para realizar otras acciones, estan en la parte de abajo.</span></p><p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;"><br /></p><p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; color:#005500;">Ejemplo de entrada:</span></p><p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;"><br /></p><p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">Terminales:</span></p><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">a b %</span></p><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">Variables:</span></p><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">S A B</span></p><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">Producciones:</span></p><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">S -&gt; A B A;</span></p><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">A -&gt; % | a;</span></p><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt;">B -&gt; % | b</span></p></body></html>')
        else:
            self.tfFNC.clear()
        
    def limpiarCampos(self):
        self.tfGramatica.setText("Terminales:\n\nVariables:\n\nProducciones:\n")
        self.tfFNC.clear()
        
    def resolver(self):
        # c = Chomsky()
        try:
            data = self.tfGramatica.toPlainText()
            open('model.txt', 'w').write(data)
            path = os.path.abspath("model/dist/Chomsky.exe")
            # print(path)
            os.system(path)
            file = open("out.txt").read()
            self.tfFNC.setText(file)
        except Exception as e:
            self.tfFNC.setText("Error, vuelva a intentar")
            return
    
    def cargarArchivo(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Principal()
    window.show()
    app.exec_()