# Problems Directory

このディレクトリには、Project Eulerの問題の解答コードが含まれます。

## 構造

各問題は以下の命名規則に従います：
- `problem_001.py` - Pythonでの解答
- `problem_001.js` - JavaScriptでの解答
- `problem_001.java` - Javaでの解答
- など

## 解答の形式

各解答ファイルには以下の要素を含めてください：
1. 問題の説明
2. 解答の実装
3. 実行結果
4. 計算時間（オプション）

## 例

```python
# Problem 1: Multiples of 3 and 5
# Find the sum of all the multiples of 3 or 5 below 1000.

def solve():
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

if __name__ == "__main__":
    result = solve()
    print(f"Answer: {result}")
``` 