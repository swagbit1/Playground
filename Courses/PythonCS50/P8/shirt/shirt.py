from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 SHIRTIFICATE", align="C")
        # Performing a line break:
        self.ln(20)

    def body(self,name):
        # centering the image position to center as it origanially goes to 0,0 but width is from 0 to some k amount
        # then the aviablibe width of the pdf becomes pdf.w - some k amount. to center it find the avalibale width and divid by 2 to get same space on both sides of the image
        #hence centered. Do same for height. eg 210 - x is the new width of pdf that is now filled
        self.image("shirtificate.png", x=(self.w - 150)/2, y= (self.h - 150)/2, w=150, h=150)
        self.cell(200,200, f"{name} took CS50", align="C")

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", style="I", size=8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# Instantiation of inherited class
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.set_font("Times", size=50)
pdf.add_page()
pdf.set_font("Times", size=20) # change size so when calling the bodu you can set it customized 
pdf.set_text_color(255,255,255)

name = input("Enter Name:")
pdf.body(name) # must call this function because add_page calls header and footer by default

pdf.output("shirtificate.pdf")
