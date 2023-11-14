class NeedlemanWunsch:
    """Метод Нидлмана Вунша."""

    def __init__(self, start_string, end_string):
        self.start_string = start_string
        self.end_string = end_string

    def get_matrix(self):
        matrix = [
            [
                0 for j in range(len(self.end_string)+1)
            ]
            for i in range(len(self.start_string)+1)
        ]
        return matrix

    def get_result_matrix(self):
        matrix = self.get_matrix()

        for i in range(len(self.start_string) + 1):
            for j in range(len(self.end_string) + 1):
                if i == 0 or j == 0:
                    matrix[i][j] = 0
                elif self.start_string[i - 1] == self.end_string[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

        return matrix

    def get_lcs(self):
        m = len(self.start_string)
        n = len(self.end_string)
        L = self.get_result_matrix()

        index = L[m][n]
        lcs = [""] * (index + 1)
        lcs[index] = ""

        i = m
        j = n
        while i > 0 and j > 0:
            if self.start_string[i - 1] == self.end_string[j - 1]:
                lcs[index - 1] = self.start_string[i - 1]
                i -= 1
                j -= 1
                index -= 1
            elif L[i - 1][j] > L[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return "".join(lcs)
