"""
Methods for visualizing dataset content and analisys performance
"""


def mosaic(images,
           labels,
           classes = None,
           class_names = None,
           image_size = (100, 100),
           num_rows = 6,
           at_random = False,
           display = False):

    if len(images) != len(labels):
        raise Exception('Mismatch between number of images and labels')

    if classes is None:
        classes = np.unique(labels)

    samples = []
    
    for cls in classes:
        cls_rows = np.where(labels == cls)[0]

        if num_rows is None:
            num_cls_samples = len(cls_rows)
        else:
            num_cls_samples = min(num_rows, len(cls_rows))

        if at_random:
            cls_rows = np.random.permutation(cls_rows)[:num_cls_samples]
        else:
            cls_rows = cls_rows[:num_cls_samples]

        samples.append(cls_rows)

    max_num_images = max([len(cls_samples) for cls_samples in samples])
    image_height, image_width = image_size

    channels = 3 if len(images[0].shape) == 3 else 1
    mosaic = np.zeros((max_num_images*image_height, len(classes)*image_width, channels), dtype=np.uint8)

    for column, cls_samples in enumerate(samples):
        image_samples = [cv.resize(img, (image_width, image_height)) for img in images[cls_samples]]
        image_samples = np.array(image_samples).reshape((-1, image_width, channels))
        mosaic[0:image_width*len(image_samples), column*image_width:(column+1)*image_width, :] = image_samples
                   
    # Labels de título
    if class_names is not None:
        mosaic_header = np.zeros((image_height, len(classes)*image_width, channels), dtype=np.uint8)

        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 0.8
        font_color = [255] * channels
        line_type = 2

        for cls_id in range(len(classes)):
            cv.putText(mosaic_header, class_names[cls_id][1], (cls_id*image_width, image_height//2),
                       font, font_scale, font_color, line_type)

        mosaic = np.concatenate((mosaic_header, mosaic), axis=0)
        
    if channels == 1:
        mosaic = mosaic.reshape((mosaic.shape[0], mosaic.shape[1]))
    
    if display:
        cv.imshow('Image', mosaic)
        cv.waitKey(0)
        cv.destroyAllWindows()
        
    return mosaic


def visual_describe():
    pass



