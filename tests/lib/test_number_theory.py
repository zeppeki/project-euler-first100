"""
数論ライブラリモジュールのテスト

problems.lib.number_theory モジュールの全関数に対する
包括的なテストケースを提供する。
"""

import pytest

from problems.lib.number_theory import (
    carmichael_lambda,
    chinese_remainder_theorem,
    continued_fraction_sqrt,
    convergents_from_continued_fraction,
    euler_totient,
    euler_totient_sieve,
    extended_gcd,
    is_carmichael_number,
    jacobi_symbol,
    mobius_function,
    modular_exponentiation,
    modular_inverse,
    solve_pell_equation,
)


class TestExtendedGCD:
    """拡張ユークリッド互除法のテスト"""

    def test_extended_gcd_basic(self) -> None:
        """基本的な拡張GCD"""
        gcd, x, y = extended_gcd(30, 18)
        assert gcd == 6
        assert 30 * x + 18 * y == gcd

        gcd, x, y = extended_gcd(35, 15)
        assert gcd == 5
        assert 35 * x + 15 * y == gcd

    def test_extended_gcd_coprime(self) -> None:
        """互いに素な数の拡張GCD"""
        gcd, x, y = extended_gcd(7, 13)
        assert gcd == 1
        assert 7 * x + 13 * y == 1

    def test_extended_gcd_zero(self) -> None:
        """0を含む拡張GCD"""
        gcd, x, y = extended_gcd(5, 0)
        assert gcd == 5
        assert x == 1 and y == 0

    def test_extended_gcd_identical(self) -> None:
        """同じ数の拡張GCD"""
        gcd, x, y = extended_gcd(12, 12)
        assert gcd == 12
        assert 12 * x + 12 * y == 12


class TestModularInverse:
    """モジュラー逆元のテスト"""

    def test_modular_inverse_basic(self) -> None:
        """基本的なモジュラー逆元"""
        inv = modular_inverse(3, 11)
        assert (3 * inv) % 11 == 1

        inv = modular_inverse(7, 13)
        assert (7 * inv) % 13 == 1

    def test_modular_inverse_large(self) -> None:
        """大きな数のモジュラー逆元"""
        inv = modular_inverse(123, 1000)
        assert (123 * inv) % 1000 == 1

    def test_modular_inverse_not_exists(self) -> None:
        """逆元が存在しない場合"""
        with pytest.raises(ValueError):
            modular_inverse(6, 9)  # gcd(6, 9) = 3 ≠ 1

        with pytest.raises(ValueError):
            modular_inverse(4, 8)  # gcd(4, 8) = 4 ≠ 1


class TestChineseRemainderTheorem:
    """中国剰余定理のテスト"""

    def test_chinese_remainder_theorem_basic(self) -> None:
        """基本的な中国剰余定理"""
        result = chinese_remainder_theorem([2, 3, 2], [3, 5, 7])
        assert result % 3 == 2
        assert result % 5 == 3
        assert result % 7 == 2

    def test_chinese_remainder_theorem_two_moduli(self) -> None:
        """2つの法の中国剰余定理"""
        result = chinese_remainder_theorem([1, 4], [3, 5])
        assert result % 3 == 1
        assert result % 5 == 4

    def test_chinese_remainder_theorem_single(self) -> None:
        """単一の合同式"""
        result = chinese_remainder_theorem([2], [5])
        assert result == 2

    def test_chinese_remainder_theorem_empty(self) -> None:
        """空の入力"""
        result = chinese_remainder_theorem([], [])
        assert result == 0

    def test_chinese_remainder_theorem_invalid_input(self) -> None:
        """不正な入力"""
        with pytest.raises(ValueError):
            chinese_remainder_theorem([1, 2], [3])  # 長さが異なる


class TestModularExponentiation:
    """モジュラー指数法のテスト"""

    def test_modular_exponentiation_basic(self) -> None:
        """基本的なモジュラー指数法"""
        result = modular_exponentiation(2, 10, 1000)
        assert result == 24  # 2^10 = 1024 ≡ 24 (mod 1000)

        result = modular_exponentiation(3, 4, 5)
        assert result == 1  # 3^4 = 81 ≡ 1 (mod 5)

    def test_modular_exponentiation_large(self) -> None:
        """大きな指数のモジュラー指数法"""
        result = modular_exponentiation(2, 100, 1000000007)
        assert result == pow(2, 100, 1000000007)  # Python標準と比較

    def test_modular_exponentiation_zero_exponent(self) -> None:
        """指数が0の場合"""
        result = modular_exponentiation(5, 0, 7)
        assert result == 1

    def test_modular_exponentiation_modulus_one(self) -> None:
        """法が1の場合"""
        result = modular_exponentiation(5, 3, 1)
        assert result == 0


class TestEulerTotient:
    """オイラーのファイ関数のテスト"""

    def test_euler_totient_basic(self) -> None:
        """基本的なファイ関数"""
        assert euler_totient(1) == 1
        assert euler_totient(2) == 1  # φ(2) = 1
        assert euler_totient(3) == 2  # φ(3) = 2
        assert euler_totient(4) == 2  # φ(4) = 2
        assert euler_totient(5) == 4  # φ(5) = 4
        assert euler_totient(6) == 2  # φ(6) = 2

    def test_euler_totient_prime(self) -> None:
        """素数のファイ関数"""
        assert euler_totient(7) == 6
        assert euler_totient(11) == 10
        assert euler_totient(13) == 12

    def test_euler_totient_prime_power(self) -> None:
        """素数の冪のファイ関数"""
        assert euler_totient(8) == 4  # φ(2³) = 2³ - 2² = 4
        assert euler_totient(9) == 6  # φ(3²) = 3² - 3¹ = 6
        assert euler_totient(25) == 20  # φ(5²) = 5² - 5¹ = 20

    def test_euler_totient_composite(self) -> None:
        """合成数のファイ関数"""
        assert euler_totient(12) == 4  # φ(12) = φ(4)φ(3) = 2×2 = 4
        assert euler_totient(15) == 8  # φ(15) = φ(3)φ(5) = 2×4 = 8
        assert euler_totient(20) == 8  # φ(20) = φ(4)φ(5) = 2×4 = 8


class TestEulerTotientSieve:
    """ファイ関数篩のテスト"""

    def test_euler_totient_sieve_basic(self) -> None:
        """基本的なファイ関数篩"""
        result = euler_totient_sieve(10)
        expected = [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4]
        assert result == expected

    def test_euler_totient_sieve_consistency(self) -> None:
        """個別計算との一致性確認"""
        sieve_result = euler_totient_sieve(20)
        for i in range(1, 21):
            assert sieve_result[i] == euler_totient(i)


class TestMobiusFunction:
    """メビウス関数のテスト"""

    def test_mobius_function_basic(self) -> None:
        """基本的なメビウス関数"""
        assert mobius_function(1) == 1  # μ(1) = 1
        assert mobius_function(2) == -1  # μ(2) = -1 (1つの素因数)
        assert mobius_function(3) == -1  # μ(3) = -1 (1つの素因数)
        assert mobius_function(4) == 0  # μ(4) = 0 (2²を含む)
        assert mobius_function(5) == -1  # μ(5) = -1 (1つの素因数)
        assert mobius_function(6) == 1  # μ(6) = 1 (2×3, 2つの素因数)

    def test_mobius_function_square_free(self) -> None:
        """平方因子を持たない数"""
        assert mobius_function(10) == 1  # μ(10) = 1 (2×5, 2つの素因数)
        assert mobius_function(14) == 1  # μ(14) = 1 (2×7, 2つの素因数)
        assert mobius_function(15) == 1  # μ(15) = 1 (3×5, 2つの素因数)

    def test_mobius_function_with_squares(self) -> None:
        """平方因子を含む数"""
        assert mobius_function(8) == 0  # μ(8) = 0 (2³を含む)
        assert mobius_function(9) == 0  # μ(9) = 0 (3²を含む)
        assert mobius_function(12) == 0  # μ(12) = 0 (2²を含む)


class TestJacobiSymbol:
    """ヤコビ記号のテスト"""

    def test_jacobi_symbol_basic(self) -> None:
        """基本的なヤコビ記号"""
        assert jacobi_symbol(1, 3) == 1
        assert jacobi_symbol(2, 3) == -1
        assert jacobi_symbol(3, 5) == -1
        assert jacobi_symbol(4, 5) == 1

    def test_jacobi_symbol_quadratic_residues(self) -> None:
        """二次剰余の確認"""
        # (2/5) = -1, (3/5) = -1, (4/5) = 1
        assert jacobi_symbol(2, 5) == -1
        assert jacobi_symbol(3, 5) == -1
        assert jacobi_symbol(4, 5) == 1

    def test_jacobi_symbol_invalid_input(self) -> None:
        """不正な入力"""
        with pytest.raises(ValueError):
            jacobi_symbol(1, 4)  # nが偶数

        with pytest.raises(ValueError):
            jacobi_symbol(1, -3)  # nが負


class TestContinuedFraction:
    """連分数のテスト"""

    def test_continued_fraction_sqrt_basic(self) -> None:
        """基本的な平方根の連分数"""
        a0, period = continued_fraction_sqrt(2)
        assert a0 == 1
        assert period == [2]

        a0, period = continued_fraction_sqrt(3)
        assert a0 == 1
        assert period == [1, 2]

    def test_continued_fraction_sqrt_perfect_square(self) -> None:
        """完全平方数の連分数"""
        a0, period = continued_fraction_sqrt(4)
        assert a0 == 2
        assert period == []

        a0, period = continued_fraction_sqrt(9)
        assert a0 == 3
        assert period == []

    def test_continued_fraction_sqrt_invalid(self) -> None:
        """不正な入力"""
        with pytest.raises(ValueError):
            continued_fraction_sqrt(-1)


class TestConvergents:
    """収束分数のテスト"""

    def test_convergents_basic(self) -> None:
        """基本的な収束分数"""
        # √2 = [1; 2, 2, 2, ...]
        convergents = convergents_from_continued_fraction(1, [2], 5)
        expected = [(1, 1), (3, 2), (7, 5), (17, 12), (41, 29)]
        assert convergents == expected

    def test_convergents_empty_period(self) -> None:
        """周期部分が空の場合"""
        convergents = convergents_from_continued_fraction(3, [], 1)
        assert convergents == [(3, 1)]

    def test_convergents_zero_count(self) -> None:
        """収束分数の個数が0の場合"""
        convergents = convergents_from_continued_fraction(1, [2], 0)
        assert convergents == []


class TestPellEquation:
    """ペル方程式のテスト"""

    def test_solve_pell_equation_basic(self) -> None:
        """基本的なペル方程式"""
        x, y = solve_pell_equation(2)
        assert x * x - 2 * y * y == 1
        assert x == 3 and y == 2  # 最小解

        x, y = solve_pell_equation(3)
        assert x * x - 3 * y * y == 1
        assert x == 2 and y == 1  # 最小解

    def test_solve_pell_equation_larger(self) -> None:
        """より大きなDのペル方程式"""
        x, y = solve_pell_equation(5)
        assert x * x - 5 * y * y == 1
        assert x == 9 and y == 4  # 最小解

    def test_solve_pell_equation_perfect_square(self) -> None:
        """完全平方数でのペル方程式"""
        with pytest.raises(ValueError):
            solve_pell_equation(4)  # 完全平方数

        with pytest.raises(ValueError):
            solve_pell_equation(9)  # 完全平方数


class TestCarmichaelFunction:
    """カーマイケル関数のテスト"""

    def test_carmichael_lambda_basic(self) -> None:
        """基本的なカーマイケル関数"""
        assert carmichael_lambda(1) == 1
        assert carmichael_lambda(2) == 1
        assert carmichael_lambda(3) == 2
        assert carmichael_lambda(4) == 2
        assert carmichael_lambda(5) == 4

    def test_carmichael_lambda_composite(self) -> None:
        """合成数のカーマイケル関数"""
        assert carmichael_lambda(15) == 4  # λ(15) = lcm(λ(3), λ(5))
        assert carmichael_lambda(21) == 6  # λ(21) = lcm(λ(3), λ(7))

    def test_carmichael_lambda_power_of_two(self) -> None:
        """2の冪のカーマイケル関数"""
        assert carmichael_lambda(8) == 2  # λ(8) = φ(8)/2 = 4/2 = 2
        assert carmichael_lambda(16) == 4  # λ(16) = φ(16)/2 = 8/2 = 4


class TestCarmichaelNumber:
    """カーマイケル数のテスト"""

    def test_is_carmichael_number_basic(self) -> None:
        """基本的なカーマイケル数判定"""
        assert is_carmichael_number(561) is True  # 最小のカーマイケル数
        assert is_carmichael_number(1105) is True  # 2番目のカーマイケル数
        assert is_carmichael_number(1729) is True  # 3番目のカーマイケル数

    def test_is_carmichael_number_non_carmichael(self) -> None:
        """カーマイケル数でない数"""
        assert is_carmichael_number(15) is False
        assert is_carmichael_number(21) is False
        assert is_carmichael_number(35) is False

    def test_is_carmichael_number_primes(self) -> None:
        """素数（カーマイケル数ではない）"""
        assert is_carmichael_number(7) is False
        assert is_carmichael_number(11) is False
        assert is_carmichael_number(13) is False

    def test_is_carmichael_number_small_numbers(self) -> None:
        """小さな数での判定"""
        assert is_carmichael_number(1) is False
        assert is_carmichael_number(2) is False
        assert is_carmichael_number(4) is False


class TestEdgeCases:
    """エッジケースのテスト"""

    def test_small_inputs(self) -> None:
        """小さな入力値のテスト"""
        assert euler_totient(1) == 1
        assert mobius_function(1) == 1
        assert carmichael_lambda(1) == 1

    def test_moderately_large_inputs(self) -> None:
        """中程度の大きな入力値のテスト"""
        # パフォーマンステスト
        result = euler_totient(1000)
        assert result == 400  # φ(1000) = φ(8)φ(125) = 4×100 = 400

        result = mobius_function(1000)
        assert result == 0  # 1000 = 2³×5³ は平方因子を含む

    def test_consistency_checks(self) -> None:
        """異なる実装間の一致性確認"""
        # ファイ関数の篩と個別計算の一致性
        sieve_result = euler_totient_sieve(50)
        for i in range(1, 51):
            assert sieve_result[i] == euler_totient(i)


class TestPracticalExamples:
    """実用的な例のテスト"""

    def test_project_euler_related(self) -> None:
        """Project Euler問題関連のテスト"""
        # Problem 069関連: φ(n)/n の計算
        for n in [2, 3, 4, 5, 6]:
            phi_n = euler_totient(n)
            ratio = phi_n / n
            assert 0 < ratio <= 1

        # Problem 066関連: ペル方程式
        for d in [2, 3, 5, 6, 7]:
            if d not in [1, 4, 9]:  # 完全平方数を除く
                x, y = solve_pell_equation(d)
                assert x * x - d * y * y == 1

    def test_cryptographic_applications(self) -> None:
        """暗号学的応用のテスト"""
        # RSA関連: モジュラー逆元
        p, q = 17, 19
        n = p * q
        phi_n = (p - 1) * (q - 1)

        e = 5  # 公開指数
        d = modular_inverse(e, phi_n)  # 秘密指数

        # 暗号化・復号化のテスト
        message = 42
        encrypted = modular_exponentiation(message, e, n)
        decrypted = modular_exponentiation(encrypted, d, n)
        assert decrypted == message
