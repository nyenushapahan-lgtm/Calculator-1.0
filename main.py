from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
import sys
import re
import os

def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and PyInstaller
    """
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Calculator:
    def __init__(self):
        self.loader = QUiLoader()

        self.app = QtWidgets.QApplication(sys.argv)

        ui_path = resource_path("calculator.ui")
        self.calculator_window = self.loader.load(ui_path, None)

        if not self.calculator_window:
            QtWidgets.QMessageBox.critical(None, "Error", "Failed to load UI file")
            sys.exit(1)

        self.calculator_window.show()
        #--------------------------------------------------------------------------------------------

        try:
            self.button_0 = self.calculator_window.button_0
            self.button_1 = self.calculator_window.button_1
            self.button_2 = self.calculator_window.button_2
            self.button_3 = self.calculator_window.button_3
            self.button_4 = self.calculator_window.button_4
            self.button_5 = self.calculator_window.button_5
            self.button_6 = self.calculator_window.button_6
            self.button_7 = self.calculator_window.button_7
            self.button_8 = self.calculator_window.button_8
            self.button_9 = self.calculator_window.button_9

            self.button_add = self.calculator_window.button_add
            self.button_sub = self.calculator_window.button_sub
            self.button_mul = self.calculator_window.button_mul
            self.button_div = self.calculator_window.button_div

            self.button_clear = self.calculator_window.button_clear
            self.button_dcp = self.calculator_window.button_decimal_point
            self.button_enter = self.calculator_window.button_enter

            self.calculator_display = self.calculator_window.calculator_display
        
        except Exception as e:
            QtWidgets.QMessageBox.warning(self.calculator_window,"Error",f"{e}")
        
        #add numbers
        self.button_0.clicked.connect(lambda : self.addValuesToDisplay("0"))
        self.button_1.clicked.connect(lambda : self.addValuesToDisplay("1"))
        self.button_2.clicked.connect(lambda : self.addValuesToDisplay("2"))
        self.button_3.clicked.connect(lambda : self.addValuesToDisplay("3"))
        self.button_4.clicked.connect(lambda : self.addValuesToDisplay("4"))
        self.button_5.clicked.connect(lambda : self.addValuesToDisplay("5"))
        self.button_6.clicked.connect(lambda : self.addValuesToDisplay("6"))
        self.button_7.clicked.connect(lambda : self.addValuesToDisplay("7"))
        self.button_8.clicked.connect(lambda : self.addValuesToDisplay("8"))
        self.button_9.clicked.connect(lambda : self.addValuesToDisplay("9"))

        #add arithmetic operations
        self.button_add.clicked.connect(lambda : self.addValuesToDisplay("+"))
        self.button_sub.clicked.connect(lambda : self.addValuesToDisplay("-"))
        self.button_div.clicked.connect(lambda : self.addValuesToDisplay("/"))
        self.button_mul.clicked.connect(lambda : self.addValuesToDisplay("*"))

        #assign a functionality for enter
        self.button_enter.clicked.connect(lambda : self.enterFunction(self.calculator_display.text()))
        #adding function for all clear
        self.button_clear.clicked.connect(self.allClear)


        #screen number
        self.screen_number = ""
        #--------------------------------------------------------------------------------------------
        self.app.exec()
    
    def addValuesToDisplay(self,number):
        self.screen_number += number
        
        #add text to the screen
        self.calculator_display.setText("")

        self.calculator_display.setText(self.screen_number)

    def allClear(self):
        self.screen_number = ""
        self.calculator_display.setText("")
    
    def enterFunction(self,cal_expression):
        #clear the calculator display
        self.calculator_display.setText("")

        self.numbers = re.split("\W",cal_expression)


        self.operations = re.findall("\W",cal_expression)
        
        #define the functionalities
        def addition(num1,num2):
            return num1+num2
        
        def subtraction(num1,num2):
            return num1-num2
        
        def multification(num1,num2):
            return num1*num2
        
        def divition(num1,num2):
            if num2 != 0:
                return num1/num2
            
            else:
                return "Zero devition Error!"
        
        operation_count = 0
        total = int(self.numbers[0])
        for numberCount in range(1,len(self.numbers)):
            number = int(self.numbers[numberCount])
            operation = self.operations[operation_count]

            if operation == "+":
                total = addition(total,number)

            elif operation == "-":
                total = subtraction(total,number)

            elif operation == "*":
                total = multification(total,number)

            elif operation == "/":
                total = divition(total,number)
            
            else:
                raise ValueError(f"Invalid operation: {operation}")

            operation_count += 1
            
        #set the calculator display
        self.calculator_display.setText(str(total))


        

#create an object
if __name__ == "__main__":
    Calculator()
