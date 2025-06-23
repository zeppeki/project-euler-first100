// Project Euler Dashboard JavaScript

// Dashboard data - this would typically come from an API or build process
const dashboardData = {
  progress: {
    completed: 8,
    total: 100,
    percentage: 8
  },
  stats: {
    solutions: 24,
    testCases: 274,
    documentation: 16,
    codeQuality: 100
  },
  problems: [
    {
      number: '001',
      title: 'Multiples of 3 and 5',
      answer: '233,168',
      learningPoint: '数学的公式の活用',
      complexities: ['O(n)', 'O(1)', 'O(1)']
    },
    {
      number: '002',
      title: 'Even Fibonacci numbers',
      answer: '4,613,732',
      learningPoint: '数列の性質の観察',
      complexities: ['O(n)', 'O(log n)', 'O(1)']
    },
    {
      number: '003',
      title: 'Largest prime factor',
      answer: '6,857',
      learningPoint: '素因数分解の効率化',
      complexities: ['O(√n)', 'O(√n)', 'O(√n)']
    },
    {
      number: '004',
      title: 'Largest palindrome product',
      answer: '906,609',
      learningPoint: '回文の性質と効率的な探索',
      complexities: ['O(n²)', 'O(n²)', 'O(n)']
    },
    {
      number: '005',
      title: 'Smallest multiple',
      answer: '232,792,560',
      learningPoint: '最小公倍数の計算',
      complexities: ['O(n²)', 'O(n log n)', 'O(n)']
    },
    {
      number: '006',
      title: 'Sum square difference',
      answer: '25,164,150',
      learningPoint: '数学的公式による最適化',
      complexities: ['O(n)', 'O(1)', 'O(1)']
    },
    {
      number: '007',
      title: '10001st prime',
      answer: '104,743',
      learningPoint: '素数生成と6k±1最適化',
      complexities: ['O(n×√m)', 'O(m×log(log(m)))', 'O(n×√m/3)']
    },
    {
      number: '008',
      title: 'Largest product in a series',
      answer: '23,514,624,000',
      learningPoint: 'スライディングウィンドウとゼロスキップ',
      complexities: ['O(n×k)', 'O(n)', 'O(n)']
    }
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
      <div class="problem-answer">解答: ${problem.answer}</div>
      <div class="problem-learning">学習ポイント: ${problem.learningPoint}</div>
      <div class="problem-complexity">
        ${problem.complexities.map(complexity =>
          `<span class="complexity-tag">${complexity}</span>`
        ).join('')}
      </div>
    </div>
  `).join('');

  container.innerHTML = `<div class="problems-grid">${problemsHTML}</div>`;
}

function createPerformanceChart() {
  const container = document.getElementById('performance-chart');
  if (!container) return;

  // Check if Chart.js is available
  if (typeof Chart === 'undefined') {
    container.innerHTML = `
      <div class="chart-container">
        <div class="chart-title">パフォーマンス比較</div>
        <p>Chart.js が読み込まれていません。グラフを表示するにはChart.jsが必要です。</p>
      </div>
    `;
    return;
  }

  container.innerHTML = `
    <div class="chart-container">
      <div class="chart-title">解法別時間計算量比較</div>
      <canvas id="performanceCanvas" class="chart-canvas"></canvas>
    </div>
  `;

  const ctx = document.getElementById('performanceCanvas').getContext('2d');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['001', '002', '003', '004', '005', '006', '007', '008'],
      datasets: [
        {
          label: '素直な解法',
          data: [1, 1, 1, 2, 2, 1, 3, 2], // Complexity scale (1=excellent, 2=good, 3=fair)
          backgroundColor: 'rgba(25, 118, 210, 0.6)',
          borderColor: 'rgba(25, 118, 210, 1)',
          borderWidth: 1
        },
        {
          label: '最適化解法',
          data: [0, 0.5, 1, 2, 1.5, 0, 2, 1],
          backgroundColor: 'rgba(76, 175, 80, 0.6)',
          borderColor: 'rgba(76, 175, 80, 1)',
          borderWidth: 1
        },
        {
          label: '数学的解法',
          data: [0, 0, 1, 1, 1, 0, 2.5, 1],
          backgroundColor: 'rgba(255, 152, 0, 0.6)',
          borderColor: 'rgba(255, 152, 0, 1)',
          borderWidth: 1
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
          max: 4,
          ticks: {
            stepSize: 1,
            callback: function(value) {
              const labels = ['O(1)', 'O(log n)', 'O(n)', 'O(n²)', 'O(n³)'];
              return labels[value] || value;
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
        }
      },
      animation: {
        duration: 2000,
        easing: 'easeInOutQuart'
      }
    }
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
