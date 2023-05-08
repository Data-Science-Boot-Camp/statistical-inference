"""
Funtions for module 3 of the Data Science bootcamp
"""
import random

from constants import STUDENTS_DS


def z_or_t_score(
        p:float, distribution: str = 'N'
) -> float:
    """
    Compute Z or T score depending on the
    distribution inputed by the user. The Z or
    T score are used to compute confidence intervals.


    """

    pass

def random_student() -> str:
    """"
    Seleccionar un estudiante al azar de la lista de estudiantes
    de data science.

    RETURNS
    name: Nombre del estudiante seleccionado
    """

    name = random.choice(STUDENTS_DS)

    return name


def n_random_students(n_students: int) -> list:
    """
    Seleccionar n estudiantes al azar de la lista de estudiantes
    de data science.

    INPUT
    n_students: Cantidad de estudiantes a seleccionar

    RETURNS

    students: Lista con los nombres de los estudiantes seleccionados
    """

    students = random.sample(STUDENTS_DS, n_students)

    return students
