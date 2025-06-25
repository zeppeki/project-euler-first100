# Problem 019: Counting Sundays

## 問題概要

20世紀（1901年1月1日〜2000年12月31日）において、月の初日（1日）が日曜日だった回数を求める問題です。

### 問題文

以下の情報が与えられています：
- 1900年1月1日は月曜日
- 各月の日数ルール：
  - 9月、4月、6月、11月は30日
  - その他は31日（2月を除く）
  - 2月は28日（うるう年は29日）
- うるう年の定義：
  - 4で割り切れる年
  - ただし世紀年（100の倍数）は400で割り切れる必要がある

### 制約条件

- 基準日：1900年1月1日は月曜日
- 対象期間：1901年1月1日〜2000年12月31日（20世紀）
- 計算対象：各月の1日が日曜日だった回数

## 解法

### 1. 素直な解法 (solve_naive)

**アプローチ**: 日付を順次カウントして曜日を追跡

```python
def solve_naive(start_year: int, end_year: int) -> int:
    # 1900年1月1日は月曜日（0=月曜日, 6=日曜日）
    current_day_of_week = 0
    sundays_count = 0

    # 1900年をスキップして1901年から開始
    for month in range(1, 13):  # 1900年の12ヶ月をスキップ
        days = days_in_month(1900, month)
        current_day_of_week = (current_day_of_week + days) % 7

    # 1901年から2000年まで
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if current_day_of_week == 6:  # Sunday
                sundays_count += 1

            days = days_in_month(year, month)
            current_day_of_week = (current_day_of_week + days) % 7

    return sundays_count
```

**特徴**:
- 時間計算量: O(n) - nは日数
- 空間計算量: O(1)
- 基準日から順次カウントして曜日を追跡
- 各月の初日が日曜日かをチェック

### 2. 最適化解法 (solve_optimized)

**アプローチ**: Zellerの公式を使用した直接計算

```python
def solve_optimized(start_year: int, end_year: int) -> int:
    def zeller_day_of_week(year: int, month: int, day: int) -> int:
        if month < 3:
            month += 12
            year -= 1

        k = year % 100
        j = year // 100

        h = (day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - 2 * j) % 7
        return h

    sundays_count = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            day_of_week = zeller_day_of_week(year, month, 1)
            if day_of_week == 1:  # Sunday in Zeller's formula
                sundays_count += 1

    return sundays_count
```

**特徴**:
- 時間計算量: O(n) - nは月数
- 空間計算量: O(1)
- Zellerの公式で各日付の曜日を直接計算
- 累積計算が不要

### 3. 数学的解法 (solve_mathematical)

**アプローチ**: Python datetimeモジュールを活用

```python
def solve_mathematical(start_year: int, end_year: int) -> int:
    sundays_count = 0

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            date = datetime(year, month, 1)
            if date.weekday() == 6:  # Sunday
                sundays_count += 1

    return sundays_count
```

**特徴**:
- 時間計算量: O(n) - nは月数
- 空間計算量: O(1)
- Python標準ライブラリの活用
- 最も実装が簡潔で信頼性が高い

## アルゴリズム解説

### うるう年の判定

正確なうるう年判定が重要：

```python
def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
```

**ルール**:
1. 400で割り切れる年はうるう年
2. 100で割り切れるが400で割り切れない年は平年
3. 4で割り切れる年はうるう年
4. その他は平年

### Zellerの公式

任意の日付の曜日を直接計算する公式：

```
h = (q + ⌊13(m+1)/5⌋ + K + ⌊K/4⌋ + ⌊J/4⌋ - 2J) mod 7
```

ここで：
- h: 曜日（0=土曜日, 1=日曜日, ..., 6=金曜日）
- q: 日
- m: 月（3=3月, 4=4月, ..., 14=2月）
- K: 年の下2桁
- J: 年の上2桁

### 各月の日数計算

```python
def days_in_month(year: int, month: int) -> int:
    if month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    elif month == 2:  # February
        return 29 if is_leap_year(year) else 28
    else:  # January, March, May, July, August, October, December
        return 31
```

## 実装のポイント

### 1. 基準日の処理

- 1900年1月1日は月曜日が基準
- 問題の対象期間は1901年から開始
- 1900年の12ヶ月分を事前に計算してスキップ

### 2. 曜日の表現

- 素直な解法：0=月曜日, 6=日曜日
- Zeller公式：0=土曜日, 1=日曜日
- datetime：0=月曜日, 6=日曜日

### 3. エッジケースの処理

- 世紀年のうるう年判定（1900年は平年、2000年はうるう年）
- 月末から翌月初への曜日計算
- 2月の日数の正確な計算

## パフォーマンス分析

| 解法 | 時間計算量 | 空間計算量 | 100年での実行時間 |
|------|------------|------------|-------------------|
| 素直な解法 | O(日数) | O(1) | <0.001秒 |
| 最適化解法 | O(月数) | O(1) | <0.001秒 |
| 数学的解法 | O(月数) | O(1) | <0.001秒 |

## 発展的考察

### 周期性の活用

曜日パターンには周期性があり、より大きな範囲では以下が活用可能：
- 400年周期：グレゴリオ暦の完全周期
- 28年周期：通常の曜日パターンの周期

### 他の日付計算問題への応用

- 特定曜日の発生回数計算
- 営業日計算
- 祝日・記念日の曜日判定

## 関連問題

- 日付計算全般
- カレンダー算法
- 周期性を利用した最適化問題

## 学習ポイント

1. **日付計算アルゴリズムの理解**
2. **うるう年ルールの正確な実装**
3. **Zellerの公式などの数学的手法**
4. **標準ライブラリの効果的活用**
5. **エッジケースの網羅的テスト**

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **対象期間**: 1901年1月1日〜2000年12月31日
- **総月数**: 1,200ヶ月
- **解答**: [隠匿]
- **検証**: ✓ 全解法で一致確認
