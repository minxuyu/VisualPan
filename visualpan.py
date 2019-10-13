import sys
from VisualPan.App import VisualPan
from PySide2.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)

    instance = VisualPan.instance()
    if instance is not None:
        app.setActiveWindow(instance)
        instance.show()

        try:
            sys.exit(app.exec_())
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
