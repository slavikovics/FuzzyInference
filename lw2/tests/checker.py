"""
Лабораторная работа 2 по дисциплине ЛОИС

Выполнили студенты группы 321701:
- Мотолянец Кирилл Андреевич
- Пушко Максим Александрович
- Самович Вячеслав Максимович
Вариант 4

Модуль для проверки корректности работы программы на случайных данных
23.10.2025

Источники:
- Логические основы интеллектуальных систем. Практикум : учебно - метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил.
"""
from decimal import Decimal
from itertools import product
import random
from interval import Interval
from composition import FuzzyCompositionLukasiewicz
from system import System


def bruteforce_solutions(tnorm, matrix, t_values, x_ids, step=Decimal("0.1")):
    grid = [Decimal(i) * step for i in range(int(Decimal("1") / step) + 1)]

    found = []

    for point in product(grid, repeat=len(x_ids)):
        x_vec = {name: val for name, val in zip(x_ids, point)}

        ok = True
        for y, t_y in t_values.items():
            sup_val = max(tnorm.solve(x_vec[x], matrix[y][x]) for x in x_ids)
            if abs(sup_val - t_y) > Decimal("1e-9"):
                ok = False
                break

        if ok:
            found.append(x_vec)

    return found


def check_interval_coverage(solutions, brute_points, x_ids):
    uncovered = []

    for p in brute_points:
        covered = False

        for sol in solutions:
            fits = True
            for x in x_ids:
                I = sol[x]
                if not I.contains(p[x]):
                    fits = False
                    break

            if fits:
                covered = True
                break

        if not covered:
            uncovered.append(p)

    return uncovered


def generate_example(nx=3, ny=3):
    x_ids = [f"x{i + 1}" for i in range(nx)]
    y_ids = [f"y{i + 1}" for i in range(ny)]

    real_x = {x: Decimal(str(round(random.uniform(0, 1), 1))) for x in x_ids}

    matrix = {}
    for y in y_ids:
        row = {}
        for x in x_ids:
            row[x] = Decimal(str(round(random.uniform(0, 1), 1)))
        matrix[y] = row

    comp = FuzzyCompositionLukasiewicz()
    t_vals = {}
    for y in y_ids:
        best = Decimal("0")
        for x in x_ids:
            v = comp.solve(real_x[x], matrix[y][x])
            if v > best:
                best = v
        t_vals[y] = best

    return x_ids, y_ids, matrix, t_vals, real_x


def validate_solution(comp, sol, matrix, t_vals, steps=5):
    for y, t in t_vals.items():
        lists = []
        for x, inter in sol.items():
            if inter.is_empty():
                return False
            l, u = inter.lower, inter.upper
            if l == u:
                lists.append([l])
            else:
                step = (u - l) / Decimal(steps)
                lists.append([l + step * i for i in range(steps + 1)])

        for combo in product(*lists):
            sup = max(comp.solve(a, matrix[y][b]) for a, b in zip(combo, sol.keys()))
            if abs(sup - t) > Decimal("1e-6"):
                return False
    return True


def print_matrix(matrix, x_ids, y_ids):
    print("   " + "  ".join(f"{x:>5}" for x in x_ids))
    for y in y_ids:
        row = "  ".join(f"{matrix[y][x]:>5}" for x in x_ids)
        print(f"{y}: {row}")


def main_loop():
    comp = FuzzyCompositionLukasiewicz()

    while True:
        x_ids, y_ids, matrix, t_vals, real_x = generate_example()

        print("\nМатрица:")
        print_matrix(matrix, x_ids, y_ids)

        print("\nt значения:")
        for y in y_ids:
            print(f"{y}: {t_vals[y]}")

        system = System(comp, matrix, t_vals)
        solutions = system.solve()

        print(f"\nНайдено решений: {len(solutions)}\n")

        good = 0
        for i, sol in enumerate(solutions):
            ok = validate_solution(comp, sol, matrix, t_vals)
            if ok:
                good += 1
                status = "OK"
            else:
                status = "FAIL"
            print(f"{i + 1}. {status}  " + ", ".join(f"{x}:{sol[x]}" for x in x_ids))

        print(f"\nКорректных решений: {good}/{len(solutions)}")

        brute = bruteforce_solutions(FuzzyCompositionLukasiewicz, matrix, t_vals, x_ids, step=Decimal("0.1"))
        print(f"Brute-force решений: {len(brute)}")
        for point in brute:
            text = ""
            for key, value in point.items():
                text += str(value) + " "

            print(f"  {text}")

        uncovered = check_interval_coverage(solutions, brute, x_ids)

        if uncovered:
            print("!!!Есть точки, попадающие в решение brute-force, но отсутствующие в интервалах!!!")
            for u in uncovered:
                print("  ", u)
        else:
            print("Интервалы полностью покрывают пространство реальных решений.")

        print("\nНажмите ENTER для новой генерации, Ctrl+C для выхода.")
        input()


if __name__ == "__main__":
    main_loop()
