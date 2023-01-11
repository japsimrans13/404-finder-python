import sys
from os.path import expanduser
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
from bot import Bot

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('PyQt5 Input Example')
        
        # Create widgets
        self.label = QLabel('Hello')
        self.label1 = QLabel('Paste Url Here')
        self.input1 = QLineEdit()
        self.label2 = QLabel('Enter csv file name')
        self.input2 = QLineEdit()
        self.button = QPushButton('Submit')
        
        # Connect button to function
        self.button.clicked.connect(self.submit)
        
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        layout.addWidget(self.button)
        self.setLayout(layout)
        

    def choose_directory(self):
        print("Choose Location")
        input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        return input_dir

    def submit(self):
        dir = self.choose_directory()
        input1_data = self.input1.text()
        input2_data = self.input2.text()
        file_path = dir + '/' + input2_data
        print(f'Input 1: {input1_data}\nInput 2: {input2_data}')
        self.label.setText('Running.....')
        bot = Bot(input1_data, file_path)
        bot.run()
        self.label.setText('Done!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
