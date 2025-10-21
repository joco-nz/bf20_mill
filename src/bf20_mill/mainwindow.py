from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.plugins import getPlugin
from qtpyvcp.actions.machine_actions import jog
from qtpyvcp.actions.coolant_actions import flood, mist
### Supports the @Slot decorator to solve property type issues.
from qtpy.QtCore import Slot
from qtpy.QtWidgets import QAbstractButton
### mdi GCODE text created by JT from linuxcnc
import bf20_mill.mdi_text as mdiText


# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)


class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        # setup some widgets
        self.btnPlotRollPan.clicked.connect(self.toggleRollPan)
        self.vtk.enable_panning(True)
        self.mdi_vtk.enable_panning(True)
        self.monitor_vtk.enable_panning(True)
        self.vtk.setViewP()
        self.mdi_vtk.setViewP()
        self.monitor_vtk.setViewP()
        jog.set_jog_continuous(True)
        
        # signal connections
        self.btnG5xBackSpace.clicked.connect(self.btnG5xBackSpace_clicked)
        self.btnParams.clicked.connect(self.btnParams_clicked)
        self.btnMdiBksp.clicked.connect(self.mdiBackSpace_clicked)
        self.btnMdiSpace.clicked.connect(self.mdiSpace_clicked)
        self.btn_air.toggled.connect(self.air_mist_toggle)
        self.btn_mist.toggled.connect(self.air_mist_toggle)


    # add any custom methods here

    def on_btnExit_clicked(self):
        self.app.quit()

    def on_set_wco_offset_Btn_clicked(self):
        if self.set_wco_offset_Btn.isChecked():
            self.wco_rotation.setText('1')
        else:
            self.wco_rotation.setText('0')

    def air_mist_toggle(self, state):
        sender = self.sender()
        name = sender.objectName()
        if name == 'btn_mist':
            if state:
                self.btn_mist.setChecked(True)
                self.btn_air.setChecked(False)
                flood.off()
                mist.on()
            else:
                self.btn_mist.setChecked(False)
                mist.off()
                
        if name == 'btn_air':
            if state:
                self.btn_air.setChecked(True)
                self.btn_mist.setChecked(False)
                mist.off()
                flood.on()
            else:
                self.btn_air.setChecked(False)
                flood.off()

    @Slot(QAbstractButton)
    def on_btngrpLeftNav_buttonClicked(self, button):
        self.stwLeft.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_btngrpRightNav_buttonClicked(self, button):
        self.stwRight.setCurrentIndex(button.property('page'))

    #
    # Plot panel
    #
    def toggleRollPan(self):
      if self.btnPlotRollPan.isChecked():
        self.btnPlotRollPan.setText('Pan')
      else:
        self.btnPlotRollPan.setText('Roll')

    #
    # G5x Offset Panel
    #
    @Slot(QAbstractButton)
    def on_btngrpG5x_buttonClicked(self, button):
        char = str(button.text())
        text = self.g5xOffsetLbl.text() or 'null'
        if text != 'null':
            text += char
        else:
            text = char
        self.g5xOffsetLbl.setText(text)

    def btnG5xBackSpace_clicked(self):
        if len(self.g5xOffsetLbl.text()) > 0:
            text = self.g5xOffsetLbl.text()[:-1]
            self.g5xOffsetLbl.setText(text)

    #
    # MDI Panel
    #
    @Slot(QAbstractButton)
    def on_btngrpMdi_buttonClicked(self, button):
        char = str(button.text())
        text = self.mdiEntry.text() or 'null'
        if text != 'null':
            text += char
        else:
            text = char
        self.mdiEntry.setText(text)

    def btnParams_clicked(self):
        # get mdi entry
        text = self.mdiEntry.text() or 'null'
        print(text)
        if text != 'null':
            # we have something to check so get the gcode words
            words = mdiText.gcode_words()
            if text in words:
                # clear the mdi line
                self.mdiClear()
                for index, value in enumerate(words[text], start=1):
                    # search and populate the params available for that gcode word
                    print(value)
                    getattr(self, 'btnGcodeP' + str(index)).setText(value)
            else:
                self.mdiClear()
            titles = mdiText.gcode_titles()
            if text in titles:
                self.lblGcodeHelp.setText(titles[text])
            else:
                self.mdiClear()
            self.lblGcodeHelp.setText(mdiText.gcode_descriptions(text))
        else:
            self.mdiClear()
            print('No Match')

    def mdiClear(self):
        for index in range(1,11):
            getattr(self, 'btnGcodeP' + str(index)).setText('')
        self.lblGcodeHelp.setText('')

    def mdiBackSpace_clicked(parent):
        if len(parent.mdiEntry.text()) > 0:
            text = parent.mdiEntry.text()[:-1]
            parent.mdiEntry.setText(text)

    def mdiSpace_clicked(parent):
        text = parent.mdiEntry.text() or 'null'
        # if no text then do not add a space
        if text != 'null':
            text += ' '
            parent.mdiEntry.setText(text)
