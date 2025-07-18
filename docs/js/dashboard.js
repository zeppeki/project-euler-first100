// Project Euler Dashboard JavaScript

// Dashboard data - this would typically come from an API or build process
const dashboardData = {
  progress: {
    completed: 100,
    total: 100,
    percentage: 100
  },
  stats: {
    solutions: 252, // 99 naive + 97 optimized + 56 mathematical = 252解法
    testCases: 1362, // 実際のテスト関数数
    documentation: 101, // 100問の解説 + README
    codeQuality: 100
  },
  problems: [
    { number: '001', title: 'Multiples of 3 and 5', learningPoint: '数学的公式の活用' },
    { number: '002', title: 'Even Fibonacci numbers', learningPoint: '数列の性質の観察' },
    { number: '003', title: 'Largest prime factor', learningPoint: '素因数分解の効率化' },
    { number: '004', title: 'Largest palindrome product', learningPoint: '回文の性質と効率的な探索' },
    { number: '005', title: 'Smallest multiple', learningPoint: '最小公倍数の計算' },
    { number: '006', title: 'Sum square difference', learningPoint: '数学的公式による最適化' },
    { number: '007', title: '10001st prime', learningPoint: '素数生成と6k±1最適化' },
    { number: '008', title: 'Largest product in a series', learningPoint: 'スライディングウィンドウとゼロスキップ' },
    { number: '009', title: 'Special Pythagorean triplet', learningPoint: 'ピタゴラス数の性質' },
    { number: '010', title: 'Summation of primes', learningPoint: 'エラトステネスの篩' },
    { number: '011', title: 'Largest product in a grid', learningPoint: '二次元配列の効率的な走査' },
    { number: '012', title: 'Highly divisible triangular number', learningPoint: '約数の個数と三角数' },
    { number: '013', title: 'Large sum', learningPoint: '大きな数の演算' },
    { number: '014', title: 'Longest Collatz sequence', learningPoint: 'メモ化による最適化' },
    { number: '015', title: 'Lattice paths', learningPoint: '組み合わせ論と格子経路' },
    { number: '016', title: 'Power digit sum', learningPoint: '大きな数の桁和計算' },
    { number: '017', title: 'Number letter counts', learningPoint: '英語数詞の規則性' },
    { number: '018', title: 'Maximum path sum I', learningPoint: '動的計画法' },
    { number: '019', title: 'Counting Sundays', learningPoint: '日付計算のアルゴリズム' },
    { number: '020', title: 'Factorial digit sum', learningPoint: '階乗と桁和' },
    { number: '021', title: 'Amicable numbers', learningPoint: '約数の和と友愛数' },
    { number: '022', title: 'Names scores', learningPoint: 'ソートと文字列処理' },
    { number: '023', title: 'Non-abundant sums', learningPoint: '過剰数の性質' },
    { number: '024', title: 'Lexicographic permutations', learningPoint: '順列の辞書順' },
    { number: '025', title: '1000-digit Fibonacci number', learningPoint: 'フィボナッチ数列の成長' },
    { number: '026', title: 'Reciprocal cycles', learningPoint: '循環小数の周期' },
    { number: '027', title: 'Quadratic primes', learningPoint: '二次式と素数生成' },
    { number: '028', title: 'Number spiral diagonals', learningPoint: '螺旋と数列の規則性' },
    { number: '029', title: 'Distinct powers', learningPoint: '冪乗の重複排除' },
    { number: '030', title: 'Digit fifth powers', learningPoint: '桁の冪乗和' },
    { number: '031', title: 'Coin sums', learningPoint: '動的計画法による組み合わせ' },
    { number: '032', title: 'Pandigital products', learningPoint: 'パンデジタル数の性質' },
    { number: '033', title: 'Digit cancelling fractions', learningPoint: '分数の約分と桁消去' },
    { number: '034', title: 'Digit factorials', learningPoint: '桁の階乗和' },
    { number: '035', title: 'Circular primes', learningPoint: '回転素数の生成' },
    { number: '036', title: 'Double-base palindromes', learningPoint: '複数進法での回文数' },
    { number: '037', title: 'Truncatable primes', learningPoint: '切り詰め可能素数' },
    { number: '038', title: 'Pandigital multiples', learningPoint: 'パンデジタル倍数' },
    { number: '039', title: 'Integer right triangles', learningPoint: '整数直角三角形の数え上げ' },
    { number: '040', title: 'Champernowne\'s constant', learningPoint: '連結数列の性質' },
    { number: '041', title: 'Pandigital prime', learningPoint: 'パンデジタル素数の探索' },
    { number: '042', title: 'Coded triangle numbers', learningPoint: '三角数と文字列符号化' },
    { number: '043', title: 'Sub-string divisibility', learningPoint: '部分文字列の性質' },
    { number: '044', title: 'Pentagon numbers', learningPoint: '五角数の差と和' },
    { number: '045', title: 'Triangular, pentagonal, and hexagonal', learningPoint: '多角数の共通項' },
    { number: '046', title: 'Goldbach\'s other conjecture', learningPoint: 'ゴールドバッハ予想の変形' },
    { number: '047', title: 'Distinct primes factors', learningPoint: '素因数の個数' },
    { number: '048', title: 'Self powers', learningPoint: '自己冪の和' },
    { number: '049', title: 'Prime permutations', learningPoint: '素数の順列' },
    { number: '050', title: 'Consecutive prime sum', learningPoint: '連続素数和の最適化' },
    { number: '051', title: 'Prime digit replacements', learningPoint: '数字置換による素数族' },
    { number: '052', title: 'Permuted multiples', learningPoint: '倍数の桁順列' },
    { number: '053', title: 'Combinatorial selections', learningPoint: '組み合わせ数の計算' },
    { number: '054', title: 'Poker hands', learningPoint: 'ポーカー手札の評価' },
    { number: '055', title: 'Lychrel numbers', learningPoint: 'リクレル数の性質' },
    { number: '056', title: 'Powerful digit sum', learningPoint: '冪乗の桁和' },
    { number: '057', title: 'Square root convergents', learningPoint: '連分数収束' },
    { number: '058', title: 'Spiral primes', learningPoint: '螺旋上の素数密度' },
    { number: '059', title: 'XOR decryption', learningPoint: 'XOR暗号の解読' },
    { number: '060', title: 'Prime pair sets', learningPoint: '素数ペア集合' },
    { number: '061', title: 'Cyclical figurate numbers', learningPoint: '循環多角数' },
    { number: '062', title: 'Cubic permutations', learningPoint: '立方数の桁順列' },
    { number: '063', title: 'Powerful digit counts', learningPoint: '冪乗の桁数' },
    { number: '064', title: 'Odd period square roots', learningPoint: '平方根の連分数展開' },
    { number: '065', title: 'Convergents of e', learningPoint: 'eの連分数収束' },
    { number: '066', title: 'Diophantine equation', learningPoint: 'ペル方程式の解法' },
    { number: '067', title: 'Maximum path sum II', learningPoint: '大規模な経路問題' },
    { number: '068', title: 'Magic 5-gon ring', learningPoint: 'マジック多角形' },
    { number: '069', title: 'Totient maximum', learningPoint: 'オイラーファイ関数の最大化' },
    { number: '070', title: 'Totient permutation', learningPoint: 'ファイ関数と順列' },
    { number: '071', title: 'Ordered fractions', learningPoint: '分数の順序付け' },
    { number: '072', title: 'Counting fractions', learningPoint: '既約分数の数え上げ' },
    { number: '073', title: 'Counting fractions in a range', learningPoint: '範囲内分数の数え上げ' },
    { number: '074', title: 'Digit factorial chains', learningPoint: '桁階乗チェーン' },
    { number: '075', title: 'Singular integer right triangles', learningPoint: '一意整数直角三角形' },
    { number: '076', title: 'Counting summations', learningPoint: '整数分割と動的計画法' },
    { number: '077', title: 'Prime summations', learningPoint: '素数分割と動的計画法' },
    { number: '078', title: 'Coin partitions', learningPoint: 'オイラーの五角数定理' },
    { number: '079', title: 'Passcode derivation', learningPoint: 'トポロジカルソート' },
    { number: '080', title: 'Square root digital expansion', learningPoint: '高精度計算' },
    { number: '081', title: 'Path sum: two ways', learningPoint: '動的計画法と最短経路' },
    { number: '082', title: 'Path sum: three ways', learningPoint: '動的計画法と3方向移動' },
    { number: '083', title: 'Path sum: four ways', learningPoint: 'Dijkstra法' },
    { number: '084', title: 'Monopoly odds', learningPoint: 'モンテカルロ法' },
    { number: '085', title: 'Counting rectangles', learningPoint: '組み合わせ論と二分探索' },
    { number: '086', title: 'Cuboid route', learningPoint: '立体幾何学とピタゴラス数' },
    { number: '087', title: 'Prime power triples', learningPoint: '素数生成と探索範囲' },
    { number: '088', title: 'Product-sum numbers', learningPoint: '積和数と再帰的探索' },
    { number: '089', title: 'Roman numerals', learningPoint: 'ローマ数字と文字列処理' },
    { number: '090', title: 'Cube digit pairs', learningPoint: '立方数と組み合わせ' },
    { number: '091', title: 'Right triangles with integer coordinates', learningPoint: '格子点と直角三角形' },
    { number: '092', title: 'Square digit chains', learningPoint: 'サイクル検出' },
    { number: '093', title: 'Arithmetic expressions', learningPoint: '算術式の評価' },
    { number: '094', title: 'Almost equilateral triangles', learningPoint: 'ペル方程式' },
    { number: '095', title: 'Amicable chains', learningPoint: '友愛数列とサイクル' },
    { number: '096', title: 'Su Doku', learningPoint: 'バックトラッキング' },
    { number: '097', title: 'Large non-Mersenne prime', learningPoint: 'モジュラー計算' },
    { number: '098', title: 'Anagramic squares', learningPoint: 'アナグラムと平方数' },
    { number: '099', title: 'Largest exponential', learningPoint: '対数比較' },
    { number: '100', title: 'Arranged probability', learningPoint: 'ペル方程式の応用' }
  ]
};

// Initialize dashboard when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  initializeDashboard();
});

function initializeDashboard() {
  createProgressSection();
  createStatsSection();
  createProblemsSection();
  createPerformanceChart();

  // Add animations
  animateElements();
}

function createProgressSection() {
  const container = document.getElementById('progress-dashboard');
  if (!container) return;

  const { completed, total, percentage } = dashboardData.progress;

  container.innerHTML = `
    <div class="progress-section">
      <div class="progress-circle-container fade-in">
        <div class="progress-label">完了率</div>
        <div class="progress-circle">
          <svg viewBox="0 0 120 120">
            <circle class="progress-circle-bg" cx="60" cy="60" r="50"></circle>
            <circle class="progress-circle-fill" cx="60" cy="60" r="50"
                    stroke-dasharray="314.159"
                    stroke-dashoffset="${314.159 - (314.159 * percentage / 100)}"></circle>
          </svg>
          <div class="progress-text">${percentage}%</div>
        </div>
        <div class="progress-details">${completed}/${total} 問題完了</div>
      </div>
    </div>
  `;
}

function createStatsSection() {
  const container = document.getElementById('stats-dashboard');
  if (!container) return;

  const { solutions, testCases, documentation, codeQuality } = dashboardData.stats;

  container.innerHTML = `
    <div class="stats-grid">
      <div class="stat-card success slide-in">
        <div class="stat-number">${solutions}</div>
        <div class="stat-label">実装済み解法</div>
      </div>
      <div class="stat-card accent slide-in">
        <div class="stat-number">${testCases}</div>
        <div class="stat-label">テストケース</div>
      </div>
      <div class="stat-card warning slide-in">
        <div class="stat-number">${documentation}</div>
        <div class="stat-label">ドキュメント</div>
      </div>
      <div class="stat-card slide-in">
        <div class="stat-number">${codeQuality}%</div>
        <div class="stat-label">コード品質スコア</div>
      </div>
    </div>
  `;
}

function createProblemsSection() {
  const container = document.getElementById('problems-dashboard');
  if (!container) return;

  const problemsHTML = dashboardData.problems.map(problem => `
    <div class="problem-card fade-in">
      <div class="problem-header">
        <div class="problem-number">Problem ${problem.number}</div>
        <div class="problem-status">完了</div>
      </div>
      <div class="problem-title">${problem.title}</div>
      <div class="problem-learning">学習ポイント: ${problem.learningPoint}</div>
    </div>
  `).join('');

  container.innerHTML = `<div class="problems-grid">${problemsHTML}</div>`;
}

function createPerformanceChart() {
  const container = document.getElementById('performance-chart');
  if (!container) return;

  // Check if performance data is available
  if (typeof performanceData === 'undefined' || !performanceData.problems) {
    container.innerHTML = `
      <div class="chart-container">
        <div class="chart-title">実測パフォーマンス比較</div>
        <div class="chart-controls">
          <p>ベンチマークデータが利用できません。</p>
          <p>データを生成するには: <code>python scripts/generate_dashboard_data.py</code></p>
        </div>
      </div>
    `;
    return;
  }

  container.innerHTML = `
    <div class="chart-container">
      <div class="chart-title">実測パフォーマンス比較</div>
      <div class="chart-controls">
        <button id="timesModeBtn" class="chart-mode-btn active">実行時間 (ms)</button>
        <button id="relativeModeBtn" class="chart-mode-btn">相対速度</button>
        <button id="tableViewBtn" class="chart-mode-btn">表形式</button>
      </div>
      <div class="chart-info">
        <span id="chartInfo">データ生成: ${performanceData.metadata.generated_from}</span>
      </div>
      <div id="chartContent">
        <canvas id="performanceCanvas" class="chart-canvas"></canvas>
      </div>
    </div>
  `;

  let currentMode = 'times';
  let isTableView = false;

  function formatTime(ms) {
    if (ms === null || ms === undefined) return 'N/A';
    if (ms < 1) return ms.toFixed(3) + ' ms';
    if (ms < 1000) return ms.toFixed(1) + ' ms';
    return (ms / 1000).toFixed(2) + ' s';
  }

  function formatRelative(value) {
    if (value === null || value === undefined) return 'N/A';
    return value.toFixed(2) + 'x';
  }

  function createTable() {
    const problems = performanceData.problems;
    const times = performanceData.times;
    const relative = performanceData.relative;

    let tableHTML = `
      <div class="performance-table-container">
        <div class="table-controls">
          <input type="text" id="problemFilter" placeholder="問題番号で検索 (例: 001, 025)" class="table-filter">
          <select id="solutionFilter" class="table-filter">
            <option value="all">すべての解法</option>
            <option value="naive">素直な解法のみ</option>
            <option value="optimized">最適化解法のみ</option>
            <option value="mathematical">数学的解法のみ</option>
          </select>
        </div>
        <table class="performance-table" id="performanceTable">
          <thead>
            <tr>
              <th class="sortable" data-sort="problem">問題番号 <span class="sort-arrow">↕</span></th>
              <th class="sortable" data-sort="naive">素直な解法 (Naive) <span class="sort-arrow">↕</span></th>
              <th class="sortable" data-sort="optimized">最適化解法 (Optimized) <span class="sort-arrow">↕</span></th>
              <th class="sortable" data-sort="mathematical">数学的解法 (Mathematical) <span class="sort-arrow">↕</span></th>
              <th class="sortable" data-sort="fastest">最速解法 <span class="sort-arrow">↕</span></th>
            </tr>
          </thead>
          <tbody id="tableBody">
    `;

    for (let i = 0; i < problems.length; i++) {
      const problem = problems[i];
      const naiveTime = times.naive[i];
      const optimizedTime = times.optimized[i];
      const mathematicalTime = times.mathematical[i];

      // Find fastest solution
      const timesArray = [naiveTime, optimizedTime, mathematicalTime].filter(t => t !== null);
      const fastestTime = timesArray.length > 0 ? Math.min(...timesArray) : null;
      let fastestSolution = 'N/A';

      if (fastestTime !== null) {
        if (naiveTime === fastestTime) fastestSolution = 'Naive';
        else if (optimizedTime === fastestTime) fastestSolution = 'Optimized';
        else if (mathematicalTime === fastestTime) fastestSolution = 'Mathematical';
      }

      const naiveDisplay = currentMode === 'times' ? formatTime(naiveTime) : formatRelative(relative.naive[i]);
      const optimizedDisplay = currentMode === 'times' ? formatTime(optimizedTime) : formatRelative(relative.optimized[i]);
      const mathematicalDisplay = currentMode === 'times' ? formatTime(mathematicalTime) : formatRelative(relative.mathematical[i]);

      tableHTML += `
        <tr data-problem="${problem}" data-naive="${naiveTime || 'null'}" data-optimized="${optimizedTime || 'null'}" data-mathematical="${mathematicalTime || 'null'}" data-fastest="${fastestSolution}">
          <td class="problem-number">Problem ${problem}</td>
          <td class="naive-cell ${naiveTime === fastestTime ? 'fastest' : ''}">${naiveDisplay}</td>
          <td class="optimized-cell ${optimizedTime === fastestTime ? 'fastest' : ''}">${optimizedDisplay}</td>
          <td class="mathematical-cell ${mathematicalTime === fastestTime ? 'fastest' : ''}">${mathematicalDisplay}</td>
          <td class="fastest-solution">${fastestSolution}</td>
        </tr>
      `;
    }

    tableHTML += `
          </tbody>
        </table>
      </div>
    `;

    return tableHTML;
  }

  function addTableInteractivity() {
    const problemFilter = document.getElementById('problemFilter');
    const solutionFilter = document.getElementById('solutionFilter');
    const tableBody = document.getElementById('tableBody');
    const sortableHeaders = document.querySelectorAll('.sortable');

    // Filter functionality
    function filterTable() {
      const problemQuery = problemFilter.value.toLowerCase();
      const solutionQuery = solutionFilter.value;
      const rows = tableBody.querySelectorAll('tr');

      rows.forEach(row => {
        const problem = row.dataset.problem.toLowerCase();
        const naive = row.dataset.naive !== 'null';
        const optimized = row.dataset.optimized !== 'null';
        const mathematical = row.dataset.mathematical !== 'null';

        const matchesProblem = problem.includes(problemQuery);
        const matchesSolution = solutionQuery === 'all' ||
          (solutionQuery === 'naive' && naive) ||
          (solutionQuery === 'optimized' && optimized) ||
          (solutionQuery === 'mathematical' && mathematical);

        row.style.display = matchesProblem && matchesSolution ? '' : 'none';
      });
    }

    problemFilter.addEventListener('input', filterTable);
    solutionFilter.addEventListener('change', filterTable);

    // Sort functionality
    let sortDirection = {};

    sortableHeaders.forEach(header => {
      header.addEventListener('click', () => {
        const sortKey = header.dataset.sort;
        const currentDirection = sortDirection[sortKey] || 'asc';
        const newDirection = currentDirection === 'asc' ? 'desc' : 'asc';
        sortDirection[sortKey] = newDirection;

        // Update sort arrows
        sortableHeaders.forEach(h => {
          const arrow = h.querySelector('.sort-arrow');
          if (h === header) {
            arrow.textContent = newDirection === 'asc' ? '↑' : '↓';
          } else {
            arrow.textContent = '↕';
          }
        });

        // Sort rows
        const rows = Array.from(tableBody.querySelectorAll('tr'));
        rows.sort((a, b) => {
          let aValue, bValue;

          if (sortKey === 'problem') {
            aValue = parseInt(a.dataset.problem);
            bValue = parseInt(b.dataset.problem);
          } else if (sortKey === 'fastest') {
            aValue = a.dataset.fastest;
            bValue = b.dataset.fastest;
          } else {
            aValue = parseFloat(a.dataset[sortKey]);
            bValue = parseFloat(b.dataset[sortKey]);

            // Handle null values
            if (isNaN(aValue)) aValue = newDirection === 'asc' ? Infinity : -Infinity;
            if (isNaN(bValue)) bValue = newDirection === 'asc' ? Infinity : -Infinity;
          }

          if (newDirection === 'asc') {
            return aValue < bValue ? -1 : aValue > bValue ? 1 : 0;
          } else {
            return aValue > bValue ? -1 : aValue < bValue ? 1 : 0;
          }
        });

        // Re-append sorted rows
        rows.forEach(row => tableBody.appendChild(row));

        // Re-apply filter
        filterTable();
      });
    });
  }

  function createChart() {
    if (typeof Chart === 'undefined') {
      return '<p>Chart.js が読み込まれていません。</p>';
    }

    return '<canvas id="performanceCanvas" class="chart-canvas"></canvas>';
  }

  function updateDisplay() {
    const chartContent = document.getElementById('chartContent');

    if (isTableView) {
      chartContent.innerHTML = createTable();
      // Add interactivity after table is created
      setTimeout(() => {
        addTableInteractivity();
      }, 100);
    } else {
      chartContent.innerHTML = createChart();

      if (typeof Chart !== 'undefined') {
        initializeChart();
      }
    }
  }

  function initializeChart() {
    const canvas = document.getElementById('performanceCanvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const data = currentMode === 'times' ? performanceData.times : performanceData.relative;

    const datasets = [];

    // Add datasets only if they have data
    if (data.naive && data.naive.some(v => v !== null)) {
      datasets.push({
        label: '素直な解法 (Naive)',
        data: data.naive,
        backgroundColor: 'rgba(25, 118, 210, 0.6)',
        borderColor: 'rgba(25, 118, 210, 1)',
        borderWidth: 1,
        skipNull: true
      });
    }

    if (data.optimized && data.optimized.some(v => v !== null)) {
      datasets.push({
        label: '最適化解法 (Optimized)',
        data: data.optimized,
        backgroundColor: 'rgba(76, 175, 80, 0.6)',
        borderColor: 'rgba(76, 175, 80, 1)',
        borderWidth: 1,
        skipNull: true
      });
    }

    if (data.mathematical && data.mathematical.some(v => v !== null)) {
      datasets.push({
        label: '数学的解法 (Mathematical)',
        data: data.mathematical,
        backgroundColor: 'rgba(255, 152, 0, 0.6)',
        borderColor: 'rgba(255, 152, 0, 1)',
        borderWidth: 1,
        skipNull: true
      });
    }

    const chartData = {
      labels: performanceData.problems,
      datasets: datasets
    };

    const yAxisTitle = currentMode === 'times' ? '実行時間 (ms)' : '相対速度 (最速解法 = 1.0)';

    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      interaction: {
        intersect: false,
        mode: 'index'
      },
      scales: {
        y: {
          type: 'linear',
          beginAtZero: true,
          title: {
            display: true,
            text: yAxisTitle
          },
          ticks: {
            callback: function(value) {
              if (currentMode === 'relative') {
                return value.toFixed(1) + 'x';
              } else {
                return value < 1 ? value.toFixed(3) : value.toFixed(1);
              }
            }
          }
        },
        x: {
          title: {
            display: true,
            text: '問題番号'
          }
        }
      },
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: false
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              const label = context.dataset.label || '';
              const value = context.parsed.y;

              if (value === null || value === undefined) {
                return label + ': データなし';
              }

              if (currentMode === 'relative') {
                return label + ': ' + value.toFixed(2) + 'x';
              } else {
                if (value < 1) {
                  return label + ': ' + value.toFixed(3) + ' ms';
                } else if (value < 1000) {
                  return label + ': ' + value.toFixed(1) + ' ms';
                } else {
                  return label + ': ' + (value / 1000).toFixed(2) + ' s';
                }
              }
            }
          }
        }
      },
      animation: {
        duration: 800,
        easing: 'easeInOutQuart'
      }
    };

    new Chart(ctx, {
      type: 'bar',
      data: chartData,
      options: chartOptions
    });
  }

  // Initialize display
  updateDisplay();

  // Add event listeners for mode switching
  document.getElementById('timesModeBtn').addEventListener('click', () => {
    currentMode = 'times';
    isTableView = false;
    document.querySelectorAll('.chart-mode-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById('timesModeBtn').classList.add('active');
    updateDisplay();
  });

  document.getElementById('relativeModeBtn').addEventListener('click', () => {
    currentMode = 'relative';
    isTableView = false;
    document.querySelectorAll('.chart-mode-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById('relativeModeBtn').classList.add('active');
    updateDisplay();
  });

  document.getElementById('tableViewBtn').addEventListener('click', () => {
    isTableView = true;
    document.querySelectorAll('.chart-mode-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById('tableViewBtn').classList.add('active');
    updateDisplay();
  });
}

function animateElements() {
  // Animate progress circle
  setTimeout(() => {
    const progressFill = document.querySelector('.progress-circle-fill');
    if (progressFill) {
      const percentage = dashboardData.progress.percentage;
      const circumference = 314.159;
      const offset = circumference - (circumference * percentage / 100);
      progressFill.style.strokeDashoffset = offset;
    }
  }, 500);

  // Stagger animation for cards
  const cards = document.querySelectorAll('.fade-in, .slide-in');
  cards.forEach((card, index) => {
    card.style.animationDelay = `${index * 0.1}s`;
  });
}

// Utility function to update dashboard data (for future API integration)
function updateDashboardData(newData) {
  Object.assign(dashboardData, newData);
  initializeDashboard();
}

// Export for potential module usage
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    dashboardData,
    initializeDashboard,
    updateDashboardData
  };
}
