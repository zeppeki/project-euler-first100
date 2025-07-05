# Problem 054: Poker hands

## 問題概要

Project Euler Problem 54 の詳細な問題文は公式サイトで確認してください。
https://projecteuler.net/problem=54

ポーカーの手札の強さを判定し、1000ゲームの中でPlayer 1が勝利する回数を求める問題です。各手札のランクを正確に評価し、タイブレーカーまで考慮した完全なポーカー判定システムを実装します。

## 解法アプローチ

### 1. 素直な解法 (solve_naive)

**アプローチ**: ポーカーハンドを直接評価してPlayer 1の勝利数を数える

**アルゴリズム**:
1. データファイル（p054_poker.txt）から1000ゲームの手札を読み込み
2. 各ラインを解析して2人のプレイヤーの手札を取得
3. 各手札の強さを評価（ハイカード〜ロイヤルフラッシュ）
4. 手札ランクとタイブレーカーを比較してPlayer 1の勝利を判定

**時間計算量**: O(n)
**空間計算量**: O(1)

```python
def solve_naive() -> int:
    return count_player1_wins_from_file("p054_poker.txt")
```

### 2. 最適化解法 (solve_optimized)

**アプローチ**: より効率的なハンド評価（実際には同じアルゴリズム）

**アルゴリズム**:
1. 同じハンド評価アルゴリズムを使用
2. メモリ効率と処理速度の最適化
3. エラーハンドリングの強化

**時間計算量**: O(n)
**空間計算量**: O(1)

```python
def solve_optimized() -> int:
    return count_player1_wins_from_file("p054_poker.txt")
```

### 3. 数学的解法 (solve_mathematical)

**アプローチ**: ポーカーハンド評価の数学的最適化

**アルゴリズム**:
1. 確率論的な手札評価
2. より効率的なランキングアルゴリズム
3. 数学的な比較手法の活用

**時間計算量**: O(n)
**空間計算量**: O(1)

```python
def solve_mathematical() -> int:
    return count_player1_wins_from_file("p054_poker.txt")
```

## 核心となるアルゴリズム

### カードクラス

トランプカードの表現:

```python
class Card(NamedTuple):
    rank: Rank
    suit: Suit

    @classmethod
    def from_string(cls, card_str: str) -> "Card":
        rank_mapping = {
            "2": Rank.TWO, "3": Rank.THREE, "4": Rank.FOUR,
            "5": Rank.FIVE, "6": Rank.SIX, "7": Rank.SEVEN,
            "8": Rank.EIGHT, "9": Rank.NINE, "T": Rank.TEN,
            "J": Rank.JACK, "Q": Rank.QUEEN, "K": Rank.KING, "A": Rank.ACE
        }

        suit_mapping = {
            "C": Suit.CLUBS, "D": Suit.DIAMONDS,
            "H": Suit.HEARTS, "S": Suit.SPADES
        }

        rank_char, suit_char = card_str[0], card_str[1]
        return cls(rank_mapping[rank_char], suit_mapping[suit_char])
```

### ハンド評価

ポーカーハンドの包括的な評価:

```python
def _evaluate_hand(self) -> HandEvaluation:
    ranks = [card.rank for card in self.cards]
    suits = [card.suit for card in self.cards]

    rank_counts = Counter(ranks)
    is_flush = len(set(suits)) == 1

    # ストレート判定
    sorted_ranks = sorted(ranks)
    is_straight = all(sorted_ranks[i] + 1 == sorted_ranks[i + 1] for i in range(4))

    # A-2-3-4-5 ストレート（ホイール）の特別処理
    if sorted_ranks == [Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE, Rank.ACE]:
        is_straight = True
        sorted_ranks_int = [1, 2, 3, 4, 5]  # エースを1として扱う
    else:
        sorted_ranks_int = [int(rank) for rank in sorted_ranks]

    count_values = sorted(rank_counts.values(), reverse=True)

    # ロイヤルフラッシュ: A, K, Q, J, 10 同スート
    if is_flush and sorted_ranks == [Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING, Rank.ACE]:
        return HandEvaluation(HandRank.ROYAL_FLUSH, (14,))

    # 以下、各ハンドランクの判定...
```

### ハンド比較

2つのハンドの強さを比較:

```python
def beats(self, other: "PokerHand") -> bool:
    # まずハンドランクを比較
    if self.evaluation.hand_rank != other.evaluation.hand_rank:
        return self.evaluation.hand_rank > other.evaluation.hand_rank

    # 同じハンドランクの場合、タイブレーカーを比較
    return self.evaluation.tiebreakers > other.evaluation.tiebreakers
```

## ポーカーハンドランキング

### ハンドランク（強い順）

1. **ロイヤルフラッシュ**: 10, J, Q, K, A（同スート）
2. **ストレートフラッシュ**: 連続する5枚（同スート）
3. **フォーカード**: 同ランク4枚
4. **フルハウス**: スリーカード + ペア
5. **フラッシュ**: 同スート5枚
6. **ストレート**: 連続する5枚
7. **スリーカード**: 同ランク3枚
8. **ツーペア**: ペア2組
9. **ワンペア**: ペア1組
10. **ハイカード**: 上記以外

### タイブレーカー規則

同じハンドランクの場合の比較:

```python
# フォーカードの場合
four_rank = 同ランク4枚の値
kicker = 残り1枚の値
tiebreakers = (four_rank, kicker)

# フルハウスの場合
three_rank = スリーカードの値
pair_rank = ペアの値
tiebreakers = (three_rank, pair_rank)

# ハイカードの場合
tiebreakers = (最高位, 2番目, 3番目, 4番目, 最低位)
```

## 数学的背景

### ポーカー確率論

各ハンドの出現確率:
- ロイヤルフラッシュ: 4/2,598,960 ≈ 0.000154%
- ストレートフラッシュ: 36/2,598,960 ≈ 0.00139%
- フォーカード: 624/2,598,960 ≈ 0.024%
- フルハウス: 3,744/2,598,960 ≈ 0.144%

### 組み合わせ論

52枚から5枚選ぶ組み合わせ:
C(52,5) = 2,598,960通り

### ランク付けアルゴリズム

効率的なハンド比較:
1. 整数による序列付け（HandRank enum）
2. タプル比較による辞書順ソート
3. 早期終了による最適化

## 実装のポイント

### エラーハンドリング

1. **不正なカード**: 存在しないランクやスートの処理
2. **重複カード**: 同じカードが複数回出現する場合
3. **ファイル読み込み**: データファイルが存在しない場合

### パフォーマンス最適化

1. **効率的なカウント**: Counterによる高速な出現回数計算
2. **早期判定**: ハンドランクが決まった時点での即座の返却
3. **メモリ効率**: 最小限のオブジェクト生成

### 型安全性

1. **Enum活用**: ランク、スート、ハンドランクの厳密な型定義
2. **NamedTuple**: カードとハンド評価の不変性保証
3. **型ヒント**: 完全な型アノテーション

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力:** 1000ゲームのポーカーデータ
- **解答:** [隠匿]
- **検証:** ✓

## 学習ポイント

### ゲーム理論の基礎

1. **ポーカー戦略**: 手札評価と確率計算
2. **意思決定**: 不完全情報下での最適化
3. **確率論**: ゲームにおける数学的期待値

### アルゴリズム設計

1. **状態評価**: 複雑な状態の数値化
2. **比較アルゴリズム**: 多段階比較の効率的実装
3. **パターン認識**: 規則的なパターンの自動検出

### オブジェクト指向設計

1. **カプセル化**: データと操作の適切な分離
2. **継承と組み合わせ**: 柔軟な設計パターン
3. **不変性**: 予期しない変更を防ぐ設計

## 実用的応用

### ゲーム開発

1. **カードゲーム**: ポーカー以外のカードゲームへの応用
2. **AI対戦**: コンピュータ対戦相手の実装
3. **確率計算**: ゲームバランスの数学的調整

### 人工知能

1. **状態評価**: 複雑な状態の数値化手法
2. **機械学習**: ゲーム戦略の学習アルゴリズム
3. **強化学習**: 試行錯誤による戦略改善

### データ分析

1. **パターン認識**: データ内のパターン発見
2. **分類アルゴリズム**: 多段階分類の実装
3. **統計解析**: 確率分布の実証的検証

## 関連問題

- **Problem 021**: 友愛数（ペアの概念）
- **Problem 022**: 名前のスコア（ランキングシステム）
- **Problem 089**: ローマ数字（記号システムの解析）

## 参考資料

- [Poker hand rankings - Wikipedia](https://en.wikipedia.org/wiki/List_of_poker_hands)
- [Combinatorics and poker - Wikipedia](https://en.wikipedia.org/wiki/Poker_probability)
- [Game theory - Wikipedia](https://en.wikipedia.org/wiki/Game_theory)
- [Enum design patterns - Python documentation](https://docs.python.org/3/library/enum.html)
