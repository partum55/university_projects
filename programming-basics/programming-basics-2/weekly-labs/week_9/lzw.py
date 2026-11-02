from PIL import Image


class GrayscaleImage:
    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.pixels = [[0 for _ in range(ncols)] for _ in range(nrows)]

    def width(self):
        """
        Returns the width of the image (number of columns).
        """
        return self.ncols

    def height(self):
        """
        Returns the height of the image (number of rows).
        """
        return self.nrows

    def clear(self, value):
        """
        Clears the image by setting each pixel to the given value.
        The value must be between 0 and 255.
        """
        if not (0 <= value <= 255):
            raise ValueError("Value must be between 0 and 255.")
        for i in range(self.nrows):
            for j in range(self.ncols):
                self.pixels[i][j] = value

    def __getitem__(self, index):
        row, col = index
        if not (0 <= row < self.nrows and 0 <= col < self.ncols):
            raise IndexError("Pixel coordinates out of image bounds.")
        return self.pixels[row][col]

    def __setitem__(self, index, value):
        row, col = index
        if not (0 <= value <= 255):
            raise ValueError("Value must be between 0 and 255.")
        if not (0 <= row < self.nrows and 0 <= col < self.ncols):
            raise IndexError("Pixel coordinates out of image bounds.")
        self.pixels[row][col] = value

    @classmethod
    def from_file(cls, path):
        """
        Creates an instance of GrayscaleImage from an image file (png or jpg).
        The image is converted to grayscale.
        """
        img = Image.open(path).convert('L')
        ncols, nrows = img.size
        instance = cls(nrows, ncols)
        pixels = list(img.getdata())
        for i in range(nrows):
            instance.pixels[i] = pixels[i * ncols:(i + 1) * ncols]
        return instance

    def flatten(self):
        """
        Returns the pixels of the image as a flat list.
        """
        return [pixel for row in self.pixels for pixel in row]

    def lzw_compression(self):
        """
        Compresses the image using the Lempel-Ziv-Welch (LZW) algorithm.
        The algorithm operates on the flattened list of pixel values.
        Returns a list of integer codes representing the compressed data.
        """
        data = self.flatten()
        dictionary = {(i,): i for i in range(256)}
        dict_size = 256
        w = ()
        result = []
        for k in data:
            wk = w + (k,)
            if wk in dictionary:
                w = wk
            else:
                result.append(dictionary[w])
                dictionary[wk] = dict_size
                dict_size += 1
                w = (k,)
        if w:
            result.append(dictionary[w])
        return result

    def lzw_decompression(self, compressed):
        """
        Reconstructs the image from the compressed data produced by the LZW algorithm.
        Returns a new GrayscaleImage instance with the decompressed pixel data.
        """
        dictionary = {i: (i,) for i in range(256)}
        dict_size = 256
        w = (compressed[0],)
        result = list(w)
        for k in compressed[1:]:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = w + (w[0],)
            else:
                raise ValueError("Invalid code in compressed data: %s" % k)
            result.extend(entry)
            dictionary[dict_size] = w + (entry[0],)
            dict_size += 1
            w = entry

        if len(result) != self.nrows * self.ncols:
            raise ValueError("Decompressed image size does not match original dimensions.")
        new_image = GrayscaleImage(self.nrows, self.ncols)
        for i in range(self.nrows):
            new_image.pixels[i] = result[i * self.ncols:(i + 1) * self.ncols]
        return new_image


def evaluate_compression(image: GrayscaleImage):
    """
    Evaluates the quality of LZW compression by calculating the ratio of the length of
    the compressed data (number of codes) to the total number of pixels in the original image.
    Prints and returns the compression ratio.
    """
    compressed = image.lzw_compression()
    original_size = image.width() * image.height()
    compression_ratio = len(compressed) / original_size
    print("Compression Ratio:", compression_ratio)
    return compression_ratio


if __name__ == "__main__":
    image = GrayscaleImage(10, 10)
    for i in range(image.height()):
        for j in range(image.width()):
            image[i, j] = (i * image.width() + j) % 256
    compressed_data = image.lzw_compression()
    print("Length of Compressed Data:", len(compressed_data))
    evaluate_compression(image)
    decompressed_image = image.lzw_decompression(compressed_data)
    assert decompressed_image.flatten() == image.flatten(), "Error: The image was not decompressed correctly."
    print("Image decompression was successful.")
