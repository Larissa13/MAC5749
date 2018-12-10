import unittest
from sarpy.visualization import get_examples, build_mosaic_header, mosaic, hist_components
import numpy as np

class VisualizationTest(unittest.TestCase):

    def setUp(self):
        self.classes_sets = [['-1', '1'], [10, -10], [0]]
        self.classes_names = [[(-1, 'minus one'), (1, 'one')], [(10, 'TEN'), (-10, 'MINUS TEN')], [(0, '0')]]
        ten_labels = np.ones((195,))*10
        ten_labels[-95:] *= -1
        self.labels_sets = [np.array(['-1', '1', '-1', '1']), ten_labels, np.zeros((125,))]
        np.random.seed(13)

        ones_3x3 = np.zeros((3,3))
        ones_3x3[:, 1] = 1
        ten_5x5 = np.zeros((5, 5))
        ten_5x5[:, 1] = 1
        ten_5x5[:, 3] = 1
        ten_5x5[:, 4] = 1

        self.images_sets = [[ones_3x3, -1*ones_3x3, -2*ones_3x3, 2*ones_3x3],
                            [ten_5x5]*100 + [-ten_5x5]*95,
                            [np.zeros((10, 10))]*125]

    def test_get_examples(self):

        rows_ns = [None, 50, 75]
        answers = [[['-1', '-1'], ['1', '1']], [[10]*50, [-10]*50], [[0]*75]]


        for cls, label, ans, rows_n in zip(self.classes_sets, self.labels_sets, answers, rows_ns):
            self.assertEqual(ans, [label[sample].tolist() for sample in get_examples(label, cls, rows_n, True)])


    def test_build_mosaic_header(self):
        true_headers = [[[[0], [0], [255], [255], [255], [0]],
                         [[0], [0], [255], [255], [255], [0]],
                         [[0], [0], [0], [255], [0], [0]]],
                        [[[0], [0], [0], [0], [0], [255], [255], [255], [255], [255]],
                         [[0], [0], [0], [0], [0], [255], [255], [255], [255], [255]],
                         [[0], [0], [0], [0], [0], [255], [255], [255], [255], [255]],
                         [[0], [0], [0], [0], [0], [0], [255], [0], [255], [0]],
                         [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]],
                        [[[0], [0], [255], [255], [255], [0], [0], [0], [0], [0]],
                         [[0], [0], [255], [255], [255], [0], [0], [0], [0], [0]],
                         [[0], [0], [255], [255], [255], [255], [0], [0], [0], [0]],
                         [[0], [0], [0], [255], [255], [255], [0], [0], [0], [0]],
                         [[0], [0], [0], [255], [255], [255], [255], [255], [255], [255]],
                         [[0], [0], [0], [0], [255], [255], [255], [255], [255], [255]],
                         [[0], [0], [0], [0], [0], [0], [255], [255], [255], [255]],
                         [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                         [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                         [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]]]

        for names, images, true_head in zip(self.classes_names, self.images_sets, true_headers):
            header = build_mosaic_header(names, (*images[0].shape, 1))
            self.assertEqual(header.tolist(), true_head)


    def test_mosaic(self):
        shapes_n_sums = [((300, 200), 1132540), ((700, 200), 4757400), ((700, 100), 36210)]

        for images, labels, names, shape_sum in zip(self.images_sets, self.labels_sets, self.classes_names, shapes_n_sums):
            m = mosaic(np.array(images), np.array(labels), class_names=names, at_random=True)

            self.assertEqual(shape_sum, (m.shape, np.sum(m)))


    def test_hist_components(self):
        true_hists = [[1]*4, [2]*195, [0]*125]
        for imgs, true_hist in zip(self.images_sets, true_hists):
            hist = hist_components(imgs, "text", show=False)
            self.assertEqual(hist, true_hist)
