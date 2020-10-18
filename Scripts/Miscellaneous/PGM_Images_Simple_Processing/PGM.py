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

    def read(self):
        with open(self.__path, 'r') as f:
            self.marker = f.readline()
            comment = f.readline()

            dimensions = (f.readline()).split()
            self.width = int(dimensions[0])
            self.height = int(dimensions[1])

            self.max_color = int(f.readline())

            #aqui começa a leitura da matriz

            self.data = f.read().split()

            for i in range(self.height):
                self.image_matrix.append(self.data[:self.width])
                self.data = self.data[self.width:]

            #print(len(self.image_matrix[0]))
            #print(len(self.image_matrix))
            #print(self.image_matrix)

    def save(self, path_to_save, matrix, width = None, height = None): #arrumar
        with open(path_to_save, "w+") as f:
            f.write(str(self.marker)+"\n")
            if(width == None):
                width = self.width
            if(height == None):
                height = self.height

            f.write(str(width)+" "+str(height)+"\n")
            f.write(str(self.max_color)+"\n")
            for row in matrix:
                for elem in row:
                    f.write(str(elem)+" ")
                f.write("\n")

    def get_darker(self, how_much_darker):
        copy_image_matrix = self.image_matrix
        for i in range(self.height):
            for j in range(self.width):
                if(int(copy_image_matrix[i][j]) - how_much_darker < 0):
                    copy_image_matrix[i][j] = 0
                else:
                    copy_image_matrix[i][j] = int(copy_image_matrix[i][j]) - how_much_darker
        return copy_image_matrix

    def get_lighter(self, how_much_lighter):
        copy_image_matrix = self.image_matrix
        for i in range(self.height):
            for j in range(self.width):
                if(int(copy_image_matrix[i][j]) + how_much_lighter > 255):
                    copy_image_matrix[i][j] = 255
                else:
                    copy_image_matrix[i][j] = int(copy_image_matrix[i][j]) + how_much_lighter
        return copy_image_matrix


    def rotate(self, degrees):
        times = int(degrees/90)
        if(times > 4 or times < -4):
            times = times/4
        if(times < 0):
            times = times + 4

        rotated_image_matrix = [[0 for i in range(self.height)] for j in range(self.width)] #criando a nova matriz
        aux_list = []
        for time in range(times): #para cada vez no numero total de vezes
            for i in range(self.height):
                for j in range(self.width):
                    rotated_image_matrix[j][self.height - 1 - i] = self.image_matrix[i][j]



        rotated_width = self.height
        rotated_height = self.width
        return rotated_image_matrix, rotated_width, rotated_height



##TEST AREA

#Creating image processor object giving the path to the test image

processor = image_processor_pgm("ctskull-256.pgm")

#reading image to the memory
processor.read()

#darker image by 100 grey levels
darker_image = processor.get_darker(100)
#saving the darker image
processor.save("ctskull-256-darker.pgm", darker_image)

#rotating image by 90 degrees
rotated_image, rotated_width, rotated_height = processor.rotate(90)
#saving rotated image
processor.save("ctskull-256-rotated.pgm", rotated_image, rotated_width, rotated_height)
