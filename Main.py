# -*- coding: utf-8 -*-
import sys
from __future__ import unicode_literals
from PySide import QtGui
from GUI import MIS_GUI


class FirstPyGUI(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(FirstPyGUI, self).__init__(parent)
    self.ui = MIS_GUI()
    self.ui.setupUi(self)

def main():

  main = QtGui.QApplication(sys.argv)
  app = FirstPyGUI()
  app.show()
  sys.exit(main.exec_())
  #xingzhi = MIS('studentID','password')
  #xingzhi.prepareSelect()
  #xingzhi.savetargetCourses()
  #xingzhi.multiThreading()
  #xingzhi.testing()
  # xingzhi.displayAllCourses()
  
  #
  # xingzhi.printTargetCourses()
  #xingzhi.testing()
  
  # xingzhi.findCourse()
  # xingzhi.printqueryResult()
  #xingzhi.prepareSelect("Music")
  #xingzhi.select()

if __name__ == "__main__":
    main()