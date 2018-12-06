import unittest
from sarpy.visualization import get_examples, build_mosaic_header, mosaic


class VisualizationTest(unittest.TestCase):

    def setUp(self):
        self.classes_sets = [['-1', '1'], [10, -10], [0]]

        ten_labels = np.ones((195,))*10
        ten_labels[-95:] *= -1
        self.labels_sets = [np.array('-1', '1', '-1', '1'), ten_labels, np.zeros((125,))]
        np.random.seed(13)

    def test_get_examples(self):

        rows_ns = [None, 50, 75]
        answers = [['-1', '1'], [10], [0]]


        for cls, label, ans, rows_n in zip(self.classes_set, self.labels_set, answers, rows_ns):
            self.assetEqual(ans, get_examples(label, cls, rows_n, True))


    def test_build_mosaic_header(self):
        pass #TODO use self.classes_sets and self.labels_sets


    def test_mosaic(self):
        pass
