import sys
from tkinter import filedialog
from pytube import YouTube
from ui_interface import *
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the button's clicked signal to the custom function
        self.ui.btn_download.clicked.connect(self.download_button_clicked)

        self.show()

    def download_button_clicked(self):
        # Get the text from the lineEdit_link_input
        self.link_text = self.ui.lineEdit_link_input.text()

        # Check if the link_text is not empty
        if self.link_text:
            # Add your download logic here using the link_text
            self.start_download()
            self.ui.lineEdit_link_input.clear()
        else:
            # If the input is empty, show a warning
            self.ui.lineEdit_link_input.clear()
            QMessageBox.warning(self, "Warning", "Please enter a YouTube link.")

    def start_download(self):
        self.link = self.link_text

        self.video = YouTube(self.link)

      #   print("Title: ", self.video.title)
      #   print("Views: ", self.video.views)

        # Get the stream with the highest resolution
        self.stream = self.video.streams.get_highest_resolution()

        # Prompt the user to choose the download location
        self.download_location = self.get_download_location()

        if self.download_location:
            # Determine the file extension based on combo box selection
            file_extension = ".mp4" if self.ui.cmbox_type.currentIndex() == 1 else ".mp3"

            # Set the file name with the appropriate extension
            file_name = f"{self.video.title}{file_extension}"

            # Download the video to the specified location
            self.stream.download(output_path=self.download_location, filename=file_name)

            print("Download completed.")
            self.ui.lineEdit_link_input.clear()
            QMessageBox.information(self, "Download", f"Download Successfully!")
        else:
            print("Download canceled.")
            self.ui.lineEdit_link_input.clear()
            QMessageBox.warning(self, "Warning", "Download canceled or no location selected.")

    def get_download_location(self):
        download_location = filedialog.askdirectory(title="Select Download Location")
        return download_location

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
