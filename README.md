# PROJECT-001

Libraries Imported
FPDF, PANDAS and MATPLOTLIB


FPDF
PyFPDF is a library for PDF document generation under Python, ported from PHP (see FPDF: "Free"-PDF, a well-known PDFlib-extension replacement with many examples, scripts and derivatives).

Latest Released Version: 1.7 (August 15th, 2012) - Current Development Version: 1.7.1

Main features
Easy to use (and easy to extend)
Many simple examples and scripts available in many languages
No external dependencies or extensions (optionally PIL for GIF support)
No installation, no compilation or other libraries (DLLs) required
Small and compact code, useful for testing new features and teaching
This repository is a fork of the library's original port by Max Pat, with the following enhancements:

Python 2.5 to 3.4+ support (see Python3 support)
Unicode (UTF-8) TrueType font subset embedding (Central European, Cyrillic, Greek, Baltic, Thai, Chinese, Japanese, Korean, Hindi and almost any other language in the world) New! based on sFPDF LGPL3 PHP version from Ian Back
Improved installers (setup.py, py2exe, PyPI) support
Barcode I2of5 and code39, QR code coming soon ...
PNG, GIF and JPG support (including transparency and alpha channel) New!
Exceptions support, other minor fixes, improvements and PEP8 code cleanups
Port of the Tutorial and ReferenceManual (Spanish translation available)
FPDF original features:

Choice of measurement unit, page format and margins
Page header and footer management
Automatic page break
Automatic line break and text justification
Image, colors and links support
Page compression
Extensive Tutorial and complete online documentation
Installation
Using PyPI
Using EasyInstall c:\python27\Scripts\easy_install.exe fpdf
From source:
Download and unpack source package (zip) or pull from the repository
Run python setup.py install
Using MSI or Windows Installers
For your convenience, some installers include the optional "Free Unicode TrueType Font Pack" (96 TTF files, 16MB compressed). Please note that copyright restrictions may apply when embedding fonts.
