import time
import serial
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread, SIGNAL
import PyQt4.Qwt5 as Qwt
import sys
import design
import os
import numpy

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.Values_To_Montior = {
            "FCTEMP1" : 0,
            "FCTEMP2" : 0,
            "AMTEMP1" : 0,
            "AMTEMP2" : 0,
            "ERROR" : 0,
            "FCVOLT" : 0,
            "FCCURR" : 0,
            "CAPCURR" : 0,
            "TANKPRES" : 0,
            "FCPRES" : 0
        }
        self.ser = None
        self.listen = False
        self.btnListen.clicked.connect(self.setupSerial)
        self.btnShutdown.clicked.connect(self.teardownSerial)
        self.c = Qwt.QwtPlotCurve()
        self.c.attach(self.qwtPlot)
        self.qwtPlot.timer = QtCore.QTimer()
        self.qwtPlot.timer.start(1000.0)
        self.centralwidget.connect(self.qwtPlot.timer, QtCore.SIGNAL('timeout()'), self.plotSomething)

        self.x=[0]
        self.y=[0]

#        self.x=[1,2,3,4,5,6,7,8,9,10]
#        self.y=[1,2,3,4,5,6,7,8,9,10]

        
    def plotSomething(self):
        print("called")
        self.c.setData(self.x, self.y)
        self.x.append(self.x[-1] + 1)
        if len(self.x) is not len(self.y):
            self.y.append(int(self.Values_To_Montior["FCTEMP2"]))
#        self.y.append(self.y[-1])
        self.qwtPlot.replot()   

    def setupSerial(self):
        # https://pyserial.readthedocs.org/en/latest/shortintro.html
        self.ser = serial.Serial()
        self.ser.baudrate = int(self.baudRate.text())
        self.ser.port = str(self.portName.text())
        self.ser.open()

        self.get_thread = getSerialMessages(self.ser, self.Values_To_Montior)
        self.connect(self.get_thread, SIGNAL('updateValue(QString, QString)'), self.updateValue)

        self.get_thread.start()
        print("thread started")
        #self.btnShutdown.clicked.connect(self.get_thread.terminate)

    def teardownSerial(self):
        self.get_thread.terminate()
        self.ser.close()
        print("thread terminated")

    def updateValue(self, ID, value):
        print("Updating value")
        print("ID " + str(ID) + " Value " + str(value))
        if (self.Values_To_Montior.get(str(ID), None) is not None): 
            self.Values_To_Montior[str(ID)] = value 
            self.displayValues()

    def displayValues(self):
        print("displaying!!!")
        pass
        #self.
        # self.fieldDisplay.clear()
        # for ID, value  in self.Values_To_Montior.iteritems():
        #     formatted_string = str(ID) + " : " + str(value)
        #     print("adding item " + formatted_string)
        #     self.fieldDisplay.addItem(formatted_string)

class getSerialMessages(QThread):    
    def __init__(self, ser, Values_To_Montior):
        QThread.__init__(self)
        self.Values_To_Montior = Values_To_Montior
        self.ser = ser

    def __del__(self):
        self.wait()            
        
        
    def run(self):
        while True:
            line = self.ser.readline() # read line
            print("from thread...")
            print("line is " + line)
            if len(line) > 0:
                try:
                    (ID, value) = line.split() # get id and value
                    self.emit(SIGNAL('updateValue(QString,QString)'), ID, value)
                except:
                    pass

    


def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

    
#### Arduino Code
#### http://electronics.stackexchange.com/questions/87868/data-lost-writing-on-arduino-serial-port-overflow
# void setup(){
#   Serial.begin(9600);
# }
# void loop(){
#   Serial.println("FCTEMP2 20");   
#   Serial.flush();
#   delay(1000);
# }

# Ref:
# http://www.swharden.com/blog/2013-05-08-realtime-data-plotting-in-python/
# http://stackoverflow.com/questions/14494747/add-images-to-readme-md-on-github
