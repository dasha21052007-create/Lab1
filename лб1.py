import math

EPS = 1e-6
N_MAX = 5


def sqrt_newton_residual(a, eps=EPS, n_max=N_MAX, verbose=False):
    """Метод Ньютона для sqrt(a). Критерий остановки — по невязке."""
    if a < 0:
        raise ValueError("a должно быть >= 0")
    if a == 0:
        return 0.0, 0

    x = 17.0
    for n in range(1, n_max + 1):
        x_new = 0.5 * (x + a / x)
        residual = abs(x_new * x_new - a)
        if verbose:
            print(f"    n={n}: x={x_new:.10f}, невязка={residual:.3e}")
        if residual < eps:
            return x_new, n
        x = x_new

    # ВАЖНО: raise стоит ВНЕ цикла (отступ как у for)
    raise RuntimeError(
        f"sqrt({a}): точность {eps} не достигнута за {n_max} итераций"
    )


def find_min_nmax(func, a, eps=EPS, limit=1000):
    """Подбирает минимальное n_max, при котором достигается точность eps."""
    for nmax in range(1, limit + 1):
        try:
            func(a, eps=eps, n_max=nmax)
            return nmax
        except RuntimeError:
            continue
    return None


if __name__ == "__main__":
    a = 17
    print(f"Вариант 7: a={a}, eps={EPS}, N_max={N_MAX}")
    print("Критерий: по невязке (для корней)\n")

    print("=== Расчёт при N_max = 5 ===")
    try:
        val, n = sqrt_newton_residual(a, n_max=N_MAX)
        print(f"  sqrt({a}) = {val:.10f}, итераций = {n}")
    except RuntimeError as e:
        print(f"  sqrt({a}): {e}")

    print("\n=== Минимальный N_max для eps = 1e-6 ===")
    print(f"  sqrt({a}): min N_max = {find_min_nmax(sqrt_newton_residual, a)}")

    print("\n=== Итоговая таблица ===")
    print(f"{'Функция':<8}{'Аргумент':>10}{'Результат':>16}"
          f"{'Эталон':>16}{'Погрешность':>14}{'Итераций':>10}")
    print("-" * 74)

    val, n = sqrt_newton_residual(a, n_max=10000)
    ref = math.sqrt(a)
    err = abs(val - ref)
    print(f"{'sqrt':<8}{a:>10}{val:>16.10f}{ref:>16.10f}"
          f"{err:>14.2e}{n:>10}")