class Printer:
    def print_document(self):
        print("Printing document")

class PDFPrinter:
    def print_document(self):
        print("Printing PDF document")

class ReportPrinter:
    def print_document(self):
        print("Printing report")

def print_file(printer):
    printer.print_document()

print_file(Printer())
print_file(PDFPrinter())
print_file(ReportPrinter())