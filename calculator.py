"""
This application is a simple calculator. The purpose of making this software is to get acquainted
with the pyqt 5 library.
In the following, I will introduce you to all the details. Learning to send a signal to a function 
was difficult and complicated for me. But now I have learned it.
The new thing about this software is that it is not geometrically measured, but like React, the size of 
the buttons changes with the size of the window.
coded by: Omid Hajavi

Date :  Monday - 2022 14 March 

"""
# Imports
import sys
import PyQt5.QtWidgets as qtw

# Classes
class F(qtw.QWidget):
    
    
    def __init__(self):
        # Initialization is done automatically from the QtWdiget library.
        super().__init__()
        self.setUI()  # The name of this function is optionally selected
     
        
    def setUI(self):
        self.setWindowTitle("Calculator") # Title of Windows
        self.setLayout(qtw.QVBoxLayout(self)) # Use QVBoxLayout Moudle
        self.keypad() # calculator keys 
        self.temp_nums = [] # setText Numbers Buttons example: 1 2 3 4
        self.fin_nums  = [] # setText Operators Buttons example : - + / *     
                
        self.show() # Show window

    def keypad(self):
        """ All these calculator keys are displayed with the help of this function. """
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        
        # first creat Buttons then Fix it in Grids
        self.result_field = qtw.QLineEdit() # Show Result Of Calc in this Area
        btn_result   = qtw.QPushButton("Enter", clicked = self.func_result) # Enter for Show Result
        btn_clear    = qtw.QPushButton("Clear", clicked = self.clear_calc)  # Enter for Clear Result
        # Numbers and Operators GUI
        btn_9         = qtw.QPushButton("9",    clicked = lambda: self.num_press('9'))
        btn_8         = qtw.QPushButton("8",    clicked = lambda: self.num_press('8'))
        btn_7         = qtw.QPushButton("7",    clicked = lambda: self.num_press('7'))
        btn_6         = qtw.QPushButton("6",    clicked = lambda: self.num_press('6'))
        btn_5         = qtw.QPushButton("5",    clicked = lambda: self.num_press('5'))
        btn_4         = qtw.QPushButton("4",    clicked = lambda: self.num_press('4'))
        btn_3         = qtw.QPushButton("3",    clicked = lambda: self.num_press('3'))
        btn_2         = qtw.QPushButton("2",    clicked = lambda: self.num_press('2'))
        btn_1         = qtw.QPushButton("1",    clicked = lambda: self.num_press('1'))
        btn_0         = qtw.QPushButton("0",    clicked = lambda: self.num_press('0'))
        btn_plus      = qtw.QPushButton("+",    clicked = lambda: self.func_press('+'))
        btn_mins      = qtw.QPushButton("-",    clicked = lambda: self.func_press('-'))
        btn_mult      = qtw.QPushButton("*",    clicked = lambda: self.func_press('*'))
        btn_dvid      = qtw.QPushButton("/",    clicked = lambda: self.func_press('/'))
        
        
        # After making the buttons, we arrange them on the grid 
        # houses in the standard order of the calculator
        container.layout().addWidget(self.result_field,0,0,1,4)
        container.layout().addWidget(btn_result,1,0,1,2)
        container.layout().addWidget(btn_clear,1,2,1,2)
        container.layout().addWidget(btn_9,2,0)
        container.layout().addWidget(btn_8,2,1)
        container.layout().addWidget(btn_7,2,2)
        container.layout().addWidget(btn_plus,2,3)
        container.layout().addWidget(btn_6,3,0)
        container.layout().addWidget(btn_5,3,1)
        container.layout().addWidget(btn_4,3,2)
        container.layout().addWidget(btn_mins,3,3)
        container.layout().addWidget(btn_3,4,0)
        container.layout().addWidget(btn_2,4,1)
        container.layout().addWidget(btn_1,4,2)
        container.layout().addWidget(btn_mult,4,3)
        container.layout().addWidget(btn_0,5,0,1,3)
        container.layout().addWidget(btn_dvid,5,3)
        self.layout().addWidget(container)
    
    
    def num_press(self, key_number):
        """This signal function picks up all the buttons and converts them to a string,
        and if the operators also have a value, it converts them to a string next to it."""
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums)+temp_string)
        else:
            self.result_field.setText(temp_string)            

    def func_press(self,operator):
        """ This function converts pre-generated strings to a new string with its own operator value."""
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))
        
    def func_result(self):
        """
        The numbers are already displayed, then the opera tour and again the number is displayed.
        Now it is time to perform mathematical calculation operations on the obtained values.
        """
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_field.setText(fin_string)
        
        
    def clear_calc(self):
        """
        After performing the mathematical calculations, all displayed values are cleared so 
        that the substrate is ready for new operations
        """
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []  





if __name__ == "__main__":
    print(__name__)        
app = qtw.QApplication(sys.argv)
app.setStyle(qtw.QStyleFactory.create('Fusion')) # Fusion is Modern Style fo PyQt Gui
ex = F()
sys.exit(app.exec_())