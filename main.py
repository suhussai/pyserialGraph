import time
import serial
from PyQt4 import QtGui
import sys
import design
import os




class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.Values_To_Montior = {
            "FCTEMP1" : -1,
            "FCTEMP2" : -1,
            "AMTEMP1" : -1,
            "AMTEMP2" : -1,
            "ERROR" : -1,
            "FCVOLT" : -1,
            "FCCURR" : -1,
            "CAPCURR" : -1,
            "TANKPRES" : -1,
            "FCPRES" : -1
        }
        self.ser = None
        self.listen = False
        self.btnListen.clicked.connect(self.setupSerial)
        self.btnShutdown.clicked.connect(self.teardownSerial)


    def setupSerial(self):
        # https://pyserial.readthedocs.org/en/latest/shortintro.html
        self.ser = serial.Serial()
        self.ser.baudrate = int(self.baudRate.text())
        self.ser.port = str(self.portName.text())
        self.ser.open()
        self.listen = True
        
        while self.listen:
            self.updateValues()
            self.displayValues()
            #time.sleep(1)

        self.ser.close()


    def teardownSerial(self):
        self.listen = False

    def displayValues(self):
        self.fieldDisplay.clear()
        for ID, value  in self.Values_To_Montior.iteritems():
            formatted_string = str(ID) + " : " + str(value)
            self.fieldDisplay.addItem(formatted_string)

    def updateValues(self):
        line = self.ser.readline() # read line
        print("line is " + line)
        if len(line) > 0:
            try:
                (ID, value) = line.split() # get id and value
                if (self.Values_To_Montior.get(ID, None) is not None): 
                    self.Values_To_Montior[ID] = value # update dict if necessary
            except:
                pass

    def setupFileHandler(fileName):
        #http://www.tutorialspoint.com/python/python_files_io.htm
        fileHandler = open(fileName, "w+")
        # FCTEMP2:-1, TANKPRES:-1, FCTEMP1:-1, AMTEMP2:-1, AMTEMP1:-1, ERROR:-1, FCPRES:-1, FCVOLT:-1, FCCURR:-1, CAPCURR:-1
        fileHandler.write("Time, FCTEMP2, TANKPRES, FCTEMP1, AMTEMP2, AMTEMP1, ERROR, FCPRES, FCVOLT, FCCURR, CAPCURR\n")
        return fileHandler

    def teardownFileHandler(fileHandler):
        fileHandler.close()

    def writeToLog(fileHandler, Values_To_Montior):
        #http://www.tutorialspoint.com/python/python_date_time.htm
        message = str(time.asctime(time.localtime(time.time()))) + " "
        for ID, value in Values_To_Montior.iteritems():
            message +=  "%d, " % (int(value))
            
        message += "\n"
        fileHandler.write(message)
        


        
    
    


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
