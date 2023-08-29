from qgis.gui import QgsMapToolEmitPoint
from qgis.utils import iface

class PrintClickedPoint(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)

    def canvasPressEvent( self, e ):
        point = self.toMapCoordinates(self.canvas.mouseLastXY())
        point = list(point)
        print (point)
        self.punto = point
    def canvasReleaseEvent( self, e ):
        iface.mapCanvas().unsetMapTool( self )

