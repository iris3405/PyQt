from PyQt5.QtChart import QLineSeries, QChart, QValueAxis, QDateTimeAxis
from PyQt5.QtCore import Qt, QDateTime
from PyQt5 import uic
from PyQt5.QtGui import QPaintEngine
from PyQt5.QtWidgets import QWidget
 
class ChartWidget(QWidget):
    def __init__(self, parent=None, ticker="BTC"):
        super().__init__(parent)
        uic.loadUi("0511/chart.ui", self)
        self.ticker = ticker
        self.viewLimit = 128

        self.priceData = QLineSeries()
        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)
        self.priceChart.legend().hide()

     
        axisX = QDateTimeAxis()
        axisX.setFormat("hh:mm:ss")
        axisX.setTickCount(4)
        dt = QDateTime.currentDateTime()
        axisX.setRange(dt, dt.addSecs(self.viewLimit))

        axisY = QValueAxis()
        axisY.setVisible(False)         
 
        self.priceChart.addAxis(axisX, Qt.AlignBottom)
        self.priceChart.addAxis(axisY, Qt.AlignRight)
        self.priceData.attachAxis(axisX)
        self.priceData.attachAxis(axisY)
        self.priceChart.layout().setContentsMargins(0, 0, 0, 0)
         # ------------------------------------------

        self.priceView.setChart(self.priceChart)
        self.priceView.setRenderHints(QPaintEngine.Antialiasing)