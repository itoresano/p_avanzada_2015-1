import csv


class Estudiante:

    def __init__(self, nombre, paterno, materno):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno


class RescueSiding:

    def __init__(self, file_name='alumnos.csv'):
        self.students = [student for student in self.lector(file_name)]

    def lector(self, file_name='alumnos.csv'):
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                nombre = self.preparar_string(row['Nombre'])
                paterno = self.preparar_string(row['Apellido paterno'])
                materno = self.preparar_string(row['Apellido materno'])
                yield (Estudiante(nombre, paterno, materno))

    @classmethod
    def preparar_string(cls, string):
        result = cls.pasar_a_mayusculas(string)
        result = cls.corregir_numero_de_erres(result)
        result = cls.remover_numero_random_if_present(result)
        return result

    @classmethod
    def remover_numero_random_if_present(cls, string):
        #############
        # COMPLETAR #
        #############
        if string[0].isdigit():
            string = string[1:]
            return cls.remover_numero_random_if_present(string)
        if string[0].isspace():
            string = string[1:]
            return cls.remover_numero_random_if_present(string)

        return string

    @classmethod
    def corregir_numero_de_erres(cls, string):
        if string.isupper():
            string = string.replace("RR", "R")
        if not string.isupper():
            string = string.replace("rr", "r")
        return string

    @classmethod
    def pasar_a_mayusculas(cls, string):
        #############
        # COMPLETAR #
        #############
        string = string.upper()
        return string

    def to_latex(self, file_name='alumnos.tex'):
        #############
        # COMPLETAR #
        #############
        with open(file_name, "w") as file:
            file.write("\\begin{table}[h]\n")
            file.write("\\begin{tabular}{|l|l|l|}\n")
            file.write("\\hline\n")
            file.write("Apellido paterno & Apellido materno & Nombre \\\\ \\hline\n")
            for estudiante in self.students:
                file.write("{0} & {1} & {2} \\\\ \\hline\n".format(estudiante.paterno, estudiante.materno,
                                                              estudiante.nombre))
            file.write("\end{tabular}\n")
            file.write("\end{table}\n")



    def to_html(self, file_name='alumnos.html'):
        #############
        # COMPLETAR #
        #############
        with open(file_name, "w") as file:
            file.write("<table>\n")
            file.write("<tr>\n")
            file.write("<th>Apellido paterno</th>\n")
            file.write("<th>Apellido materno</th>\n")
            file.write("<th>Nombre</th>\n")
            file.write("</tr>\n")
            for estudiante in self.students:
                file.write("<tr>\n")
                file.write("<td>{0}</td>\n".format(estudiante.paterno))
                file.write("<td>{0}</td>\n".format(estudiante.materno))
                file.write("<td>{0}</td>\n".format(estudiante.nombre))
                file.write("</tr>\n")
            file.write("</table>\n")


    def to_markdown(self, file_name='alumnos.md'):
        with open(file_name, "w") as file:
            file.write("| Apellido paterno | Apellido materno | Nombre|\n")
            file.write("|----|---|---|\n")
            for estudiante in self.students:
                file.write("| {0} | {1} | {2} |\n".format(estudiante.paterno, estudiante.materno, estudiante.nombre))



if __name__ == '__main__':
    rescue_siding = RescueSiding()
    rescue_siding.to_latex()
    rescue_siding.to_html()
    rescue_siding.to_markdown()
