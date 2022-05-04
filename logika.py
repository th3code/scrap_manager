import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = QWidget()
        loader = QUiLoader()
        self.window = loader.load("wyglad.ui", self)
        self.setWindowTitle('SCRAP MANAGER ')
        self.setWindowIcon(QIcon('robot.ico'))
        self.window.lineEdit.textEdited.connect(self.oblicz)
        self.window.lineEdit_2.textEdited.connect(self.oblicz)
        self.window.lineEdit_3.textEdited.connect(self.oblicz)
        self.window.lineEdit_4.textEdited.connect(self.oblicz)
        self.window.lineEdit_5.textEdited.connect(self.oblicz)
        self.window.lineEdit_6.textEdited.connect(self.oblicz)
        self.window.lineEdit_7.textEdited.connect(self.oblicz)
        self.window.lineEdit_8.textEdited.connect(self.oblicz)
        self.window.lineEdit_9.textEdited.connect(self.oblicz)
        self.window.lineEdit_10.textEdited.connect(self.oblicz)
        self.window.lineEdit.setText('90')
        self.window.lineEdit_2.setText('300')
        self.window.lineEdit_3.setText('5')
        self.window.lineEdit_4.setText('300')
        self.window.lineEdit_5.setText('10')
        self.window.lineEdit_6.setText('1')
        self.window.lineEdit_7.setText('1')
        self.window.lineEdit_8.setText('3000.00')
        self.window.lineEdit_9.setText('10.00')
        self.window.lineEdit_10.setText('10.00')
        self.window.label_5.setText('5.09')
        self.window.label_9.setText('11.11')
        self.window.label_12.setText('22.22')
        self.window.label_18.setText('3.33')
        self.window.label_28.setText('4.00')
        self.window.label_32.setText('2.75')
        self.window.label_35.setText('4.25')
        self.window.label_38.setText('10.00')
        self.window.label_41.setText('3000.00')
        self.window.label_45.setText('42.50')
        self.window.label_49.setText('28.00')
        self.window.label_52.setText('12.00')
        self.window.label_55.setText('50.00')
        self.window.label_58.setText('10.00')

        self.show()

    @Slot()
    def oblicz(self):

        #POBIERANIE WARTOSCI SEKCJA PIERWSZA
        srednica = self.window.lineEdit.text()
        srednica_float = float(srednica)
        promien = srednica_float / 2
        RPM = self.window.lineEdit_2.text()
        RPM_float = float(RPM)
        moment = self.window.lineEdit_3.text()
        moment_float = float(moment)

        #POBIERANIE WARTOSCI SEKCJA DRUGA
        moment_widly = self.window.lineEdit_5.text()
        moment_widly_float = float(moment_widly)
        dlugosc_widly = self.window.lineEdit_4.text()
        dlugosc_widly_float = float(dlugosc_widly)

        #POBIERANIE WARTOSCI SEKCJA TRZECIA
        iloscogniw_s = self.window.lineEdit_6.text()
        iloscogniw_s_float = float(iloscogniw_s)

        iloscogniw_p = self.window.lineEdit_7.text()
        iloscogniw_p_float = float(iloscogniw_p)

        pojemnosc_ogniwa = self.window.lineEdit_8.text()
        pojemnosc_ogniwa_float = float(pojemnosc_ogniwa)

        prad_ogniwa = self.window.lineEdit_9.text()
        prad_ogniwa_float = float(prad_ogniwa)

        cena_ogniwa = self.window.lineEdit_10.text()
        cena_ogniwa_float = float(cena_ogniwa)

        # PIERWSZA SEKCJA OBLICZEN
        predkosc = ((3.14 * 2 * promien) / 1000 * (RPM_float)) * 60 / 1000
        sila = (moment_float / promien) * 1000 / 10

        # DRUGA SEKCJA OBLICZEN
        udzwig = moment_widly_float / (dlugosc_widly_float / 1000) / 10

        # TRZECIA SEKCJA OBLICZEN
        Unominalne = 4
        Uminimalne = 2.75
        Umaksymalne = 4.25
        i_pakietu = iloscogniw_p_float * prad_ogniwa_float
        pojemnosc_pakietu = iloscogniw_p_float * pojemnosc_ogniwa_float
        napiecie_nominalne = Unominalne * iloscogniw_s_float
        napiecie_minimalne = Uminimalne * iloscogniw_s_float
        napiecie_maksymalne = Umaksymalne * iloscogniw_s_float
        moc_maksymalna = napiecie_maksymalne * i_pakietu
        moc_nominalna = napiecie_nominalne * i_pakietu
        pojemnosc_bezwzgledna = napiecie_nominalne * pojemnosc_pakietu / 1000
        masa_ogniw = iloscogniw_p_float * iloscogniw_s_float * 50
        koszt_ogniw = iloscogniw_p_float * iloscogniw_s_float * cena_ogniwa_float

        #AKTUALIZACJA ZAWARTOSCI SEKCJI PIERWSZEJ
        self.window.label_5.setText(str(round(predkosc, 2)))
        self.window.label_9.setText(str(round(sila, 2)))
        self.window.label_12.setText(str(round(sila * 2, 2)))

        #AKTUALIZACJA ZAWARTOSCI SEKCJI DRUGIEJ
        self.window.label_18.setText(str(round(udzwig, 2)))

        #AKTUALIZACJA ZAWARTOSCI SEKCJI TRZECIEJ
        self.window.label_38.setText(str(round(i_pakietu, 2)))
        self.window.label_41.setText(str(round(pojemnosc_pakietu, 2)))
        self.window.label_52.setText(str(round(pojemnosc_bezwzgledna, 2)))
        self.window.label_28.setText(str(round(napiecie_nominalne, 2)))
        self.window.label_32.setText(str(round(napiecie_minimalne, 2)))
        self.window.label_35.setText(str(round(napiecie_maksymalne, 2)))
        self.window.label_45.setText(str(round(moc_maksymalna, 2)))
        self.window.label_49.setText(str(round(moc_nominalna, 2)))
        self.window.label_55.setText(str(round(masa_ogniw, 2)))
        self.window.label_58.setText(str(round(koszt_ogniw, 2)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())
