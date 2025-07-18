# Problem 084: Monopoly odds

## 問題の概要

モノポリーゲームにおいて、4面ダイスを2つ使用した場合の各マスの到達確率を計算し、最も訪問頻度の高い3つのマスを特定します。通常の6面ダイスではなく4面ダイスを使用することで、移動パターンと確率分布が変化します。

## 解法の説明

### 1. 素直な解法 (Monte Carlo Simulation)

```python
def solve_naive(dice_sides: int = 4, num_simulations: int = 1000000) -> str:
```

- **アプローチ**: モンテカルロシミュレーション
- **時間計算量**: O(n) - シミュレーション回数に比例
- **空間計算量**: O(1) - 固定サイズのカウンタ

大量のゲームをシミュレーションして統計的に最頻訪問マスを特定します。

### 2. 最適化解法 (Markov Chain)

```python
def solve_optimized(dice_sides: int = 4) -> str:
```

- **アプローチ**: マルコフ連鎖による定常分布計算
- **時間計算量**: O(n³) - 行列演算による
- **空間計算量**: O(n²) - 遷移行列

各マス間の遷移確率を行列で表現し、定常状態での確率分布を計算します。

## モノポリーボードの構成

40マスのボード配置：
```
00: GO    01: A1    02: CC1   03: A2    04: T1
05: R1    06: B1    07: CH1   08: B2    09: B3
10: JAIL  11: C1    12: U1    13: C2    14: C3
15: R2    16: D1    17: CC2   18: D2    19: D3
20: FP    21: E1    22: CH2   23: E2    24: E3
25: R3    26: F1    27: F2    28: U2    29: F3
30: G2J   31: G1    32: G2    33: CC3   34: G3
35: R4    36: CH3   37: H1    38: T2    39: H2
```

## 特殊マスのルール

### 1. Go To Jail (G2J)
- マス30に到着すると強制的にJAIL（マス10）に移動

### 2. Community Chest (CC)
- マス2, 17, 33
- 1/16の確率でGOへ移動
- 1/16の確率でJAILへ移動
- 14/16の確率でそのまま滞在

### 3. Chance (CH)
- マス7, 22, 36
- 様々な移動効果（GO、JAIL、特定マス、次の鉄道など）

### 4. 連続ダブル
- 3回連続でダブル（同じ目）を出すとJAILに送られる

## 数学的背景

### モンテカルロ法
大数の法則により、十分な試行回数で真の確率に収束：
- 試行回数nに対して標準誤差は O(1/√n)
- 1,000,000回のシミュレーションで十分な精度を確保

### マルコフ連鎖
各マスを状態とする確率過程：
- 遷移行列P[i][j] = マスiからマスjへ移動する確率
- 定常分布π = πP を満たすπが長期的な滞在確率

## 実装のポイント

1. **ランダム性の制御**: 再現可能な結果のため固定シード使用
2. **特殊ルールの実装**: 各カードの効果を正確にモデル化
3. **効率的なシミュレーション**: 大量試行を高速実行
4. **結果フォーマット**: 6桁文字列（上位3マスを2桁ずつ）

## パフォーマンス比較

- **モンテカルロ法**: 実装が簡単、結果が直感的
- **マルコフ連鎖**: 理論的に厳密、計算が複雑

## 6面ダイス vs 4面ダイス

ダイスの面数変更による影響：
- **移動距離分布**: 4面ダイスでは2-8の範囲（6面では2-12）
- **特定マス到達確率**: より短い移動により近距離マスの訪問頻度上昇
- **ゲーム性**: より頻繁な周回、異なる戦略的価値

## 学習のポイント

1. **確率シミュレーション**: 複雑なルールを持つ確率系の解析
2. **マルコフ連鎖**: 状態遷移システムの数学的モデル化
3. **大数の法則**: 統計的手法による近似解の信頼性
4. **ゲーム理論**: ルールベースシステムの確率的解析

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力**: 4面ダイス2個を使用したモノポリーゲーム
- **解答**: [隠匿]
- **検証**: ✓
