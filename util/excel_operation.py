import xlrd


class OperationExcel:
    def __init__(self, path, sheet_name):
        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    def get_nrow(self):
        return self.sheet.nrows

    def get_ncol(self):
        return self.sheet.ncols

    def get_cell(self, row, col):
        return self.sheet.cell_value(row, col)
