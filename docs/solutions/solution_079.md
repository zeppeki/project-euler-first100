# Problem 079: Passcode derivation

## 問題

オンラインバンキングで使用される一般的なセキュリティ手法は、ユーザーにパスコードから3つのランダムな文字を要求することです。例えば、パスコードが531278の場合、2番目、3番目、5番目の文字を要求すると、期待される回答は「317」になります。

テキストファイル「keylog.txt」には、50回の成功したログイン試行が含まれています。

3つの文字は常に順序通りに要求されることを前提として、ファイルを分析して、未知の長さの最短の秘密パスコードを決定してください。

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Naive Approach)

この問題は**グラフ理論**の**トポロジカルソート**問題として捉えることができます。

**アプローチ：**
1. **依存関係グラフの構築**：各ログイン試行から、数字間の順序関係を抽出
2. **トポロジカルソート**：Kahn's algorithmを使用して正しい順序を決定

**実装詳細：**
```python
def build_dependency_graph(attempts):
    # 各数字が後に来る必要がある数字を記録
    dependencies = {}
    for attempt in attempts:
        for i in range(len(attempt)):
            for j in range(i + 1, len(attempt)):
                dependencies[attempt[i]].add(attempt[j])
    return dependencies

def topological_sort(dependencies):
    # 入次数を計算し、0の数字から開始
    # 辞書順で安定ソートを保証
```

**時間計算量：** O(V + E) where V=数字の種類、E=依存関係の数
**空間計算量：** O(V + E)

### 2. 最適化解法 (Optimized Approach)

基本的なアルゴリズムは既に最適であるため、同じ手法を使用します。トポロジカルソートは有向非環グラフ（DAG）の順序付けにおいて最も効率的なアルゴリズムです。

**最適化ポイント：**
- 辞書順による安定ソートで一意解を保証
- セットを使用した高速な重複除去
- 早期終了条件なし（全ての数字を含む必要があるため）

### 3. 数学的解法 (Mathematical Approach)

グラフ理論における**トポロジカルソート**を数学的に厳密に適用した解法です。

**数学的背景：**
- **有向非環グラフ（DAG）**：ログイン試行から構築される順序関係
- **偏順序関係**：数字間の「前に来る」関係
- **線形拡張**：偏順序を全順序に拡張する問題

**Kahn's Algorithm：**
1. **初期化**：入次数が0の頂点をキューに追加
2. **反復**：キューから頂点を取り出し、隣接頂点の入次数を減らす
3. **終了**：全ての頂点が処理されるまで継続

**数学的保証：**
- アルゴリズムがDAGで終了することの証明
- 辞書順選択による一意解の存在

## 学習ポイント

### グラフ理論
- **トポロジカルソート**の実用的応用
- **依存関係解決**問題としての抽象化
- **Kahn's Algorithm**の実装と理解

### アルゴリズム設計
- 問題の**グラフ理論的モデル化**
- **安定ソート**による一意解の保証
- **データ構造選択**（辞書 vs リスト）

### 実装技術
- **ファイル読み込み**と文字列処理
- **辞書とセット**の効率的使用
- **型ヒント**による保守性向上

## 検証

実装した解答は以下の条件を満たします：

1. **完全性**：全てのログイン試行を満たす
2. **最短性**：必要最小限の数字のみを含む
3. **一意性**：辞書順による安定した結果
4. **効率性**：O(V + E)の最適時間計算量

## 関連問題

- **依存関係解決**：ソフトウェアパッケージ管理
- **スケジューリング**：タスクの実行順序決定
- **コンパイラ設計**：依存関係のあるモジュールのコンパイル順序

このような順序決定問題は、コンピュータサイエンスの多くの分野で応用される重要な概念です。
