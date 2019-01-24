import xlwt


class Output:
    def __init__(self):
        self.book = xlwt.Workbook()
        self.sheet = self.book.add_sheet("Preprocessing")
        self.sheet.write(0, 0, "Preprocessing")

        self.sheet1 = self.book.add_sheet("Term Weighting")
        self.sheet1.write(0, 0, "TermWeighting")

        # self.sheet2 = self.book.add_sheet("Information Retrieval")
        # self.sheet2.write(0, 0, "Information Retrieval")

        self.column_number = 0
        self.row_number = 2

    def write_pre(self, documents, title):
        self.row_number = 2
        self.sheet.write(self.row_number, self.column_number, title)
        self.row_number += 1

        start_row = self.row_number
        for i in range(0, len(documents)):
            self.row_number = start_row
            self.sheet.write(self.row_number, self.column_number, i+1)
            self.row_number += 1
            for row_number, word in enumerate(documents[i], self.row_number):
                self.sheet.write(self.row_number, self.column_number, word)
                self.row_number += 1
            self.column_number += 1

        self.column_number += 1
        self.row_number = start_row

    def write_term_weight(self, terms, term_weight, title):
        self.row_number = 2
        self.sheet2.write(self.row_number, self.column_number, title)
        self.row_number += 1

        start_row = self.row_number
        self.sheet2.write(self.row_number, self.column_number, "Terms")
        self.row_number += 1
        for term in terms:
            self.sheet2.write(self.row_number, self.column_number, term)
            self.row_number += 1
        self.column_number +=1

        self.row_number = start_row
        for i in range(0, len(term_weight)):
            self.row_number = start_row
            self.sheet2.write(self.row_number, self.column_number, i + 1)
            self.row_number += 1
            for row_number, word_weight in enumerate(term_weight[i], self.row_number):
                self.sheet2.write(self.row_number, self.column_number, word_weight)
                self.row_number += 1
            self.column_number += 1

        self.column_number += 1
        self.row_number = start_row

    def write_doc_frequency(self, frequencies, title):
        self.row_number = 3

        self.sheet2.write(self.row_number, self.column_number, title)

        self.row_number += 1
        for word_frequency in frequencies:
            self.sheet2.write(self.row_number, self.column_number, word_frequency)
            self.row_number += 1

        self.column_number += 2

    def save(self, filename):
        self.book.save(filename)
