import copy


# Creating the class to processing
class image_processor_pgm:
    def __init__(self, path):
        self.__path = path
        self.data = []
        self.count_items = 0
        self.width = None
        self.height = None
        self.image_matrix = []
        self.max_color = None
        self.marker = None

    # Read the image file and stores in the "image_matrix" attribute
    def read(self):
        with open(self.__path, "r") as f:
            # here is the header being read and stored
            self.marker = f.readline()
            f.readline()

            dimensions = (f.readline()).split()
            self.width = int(dimensions[0])
            self.height = int(dimensions[1])

            self.max_color = int(f.readline())

            # here starts the image read

            self.data = f.read().split()

            for _ in range(self.height):
                self.image_matrix.append(self.data[: self.width])
                self.data = self.data[self.width :]

    # saves a matrix as a image into a given path
    # path_to_save = path where the matrix will be saved as a image
    # matrix = matrix of pixels
    # width - if not given, will use the one that was read on the original image header
    # height - same as width
    def save(self, path_to_save, matrix, width=None, height=None):
        with open(path_to_save, "w+") as f:
            f.write(str(self.marker) + "\n")
            if width is None:
                width = self.width
            if height is None:
                height = self.height

            f.write(str(width) + " " + str(height) + "\n")
            f.write(str(self.max_color) + "\n")
            for row in matrix:
                for elem in row:
                    f.write(str(elem) + " ")
                f.write("\n")

    # subtract a value of all the pixels
    def get_darker(self, how_much_darker):
        copy_image_matrix = copy.deepcopy(self.image_matrix)
        for i in range(self.height):
            for j in range(self.width):
                if int(copy_image_matrix[i][j]) - how_much_darker < 0:
                    copy_image_matrix[i][j] = 0
                else:
                    copy_image_matrix[i][j] = (
                        int(copy_image_matrix[i][j]) - how_much_darker
                    )
        return copy_image_matrix

    # sum a value in all of the pixels
    def get_lighter(self, how_much_lighter):
        copy_image_matrix = copy.deepcopy(self.image_matrix)
        for i in range(self.height):
            for j in range(self.width):
                if int(copy_image_matrix[i][j]) + how_much_lighter > 255:
                    copy_image_matrix[i][j] = 255
                else:
                    copy_image_matrix[i][j] = (
                        int(copy_image_matrix[i][j]) + how_much_lighter
                    )
        return copy_image_matrix

    def rotate(self, degrees):
        times = int(degrees / 90)
        if times > 4 or times < -4:
            times = times / 4
        if times < 0:
            times = times + 4

        rotated_image_matrix = [
            [0 for i in range(self.height)] for j in range(self.width)
        ]  # criando a nova matriz
        for _ in range(times):  # para cada vez no numero total de vezes
            for i in range(self.height):
                for j in range(self.width):
                    rotated_image_matrix[j][
                        self.height - 1 - i
                    ] = self.image_matrix[i][j]

        rotated_width = self.height
        rotated_height = self.width
        return rotated_image_matrix, rotated_width, rotated_height


##TEST AREA

if __name__ == "__main__":
    # WARNING: ASCII PGM IMAGE PATH, CHANGE TO YOUR IMAGE PATH HERE
    image_path = "ctskull-256.pgm"

    # Creating image processor object giving the path to the test image

    processor = image_processor_pgm(image_path)

    # reading image to the memory
    processor.read()

    # darker image by 100 grey levels
    darker_image = processor.get_darker(100)
    # saving the darker image
    processor.save("darker-image.pgm", darker_image)

    # rotating image by 90 degrees
    rotated_image, rotated_width, rotated_height = processor.rotate(90)
    # saving rotated image
    processor.save(
        "rotated-image.pgm", rotated_image, rotated_width, rotated_height
    )
