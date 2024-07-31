const words = [
  [0.5, 0.05],
  [0.4, 0.03],
  [0.3, 0.02],

  // [0.1, 0.20],
  // [0.1, 0.20],
  // [0.1, 0.20],

  // [0.1, 0.20],
  // [0.1, 0.20],
  // [0.1, 0.20],

  // [0.1, 0.30],
  // [0.1, 0.10],
  // [0.1, 0.10],

  // [0.1, 0.10],
  // [0.1, 0.10],
  // [0.1, 0.10],

  // [0.1, 0.10],
  // [0.1, 0.10],
  // [0.1, 0.10],
]

// 各个单词的条件概率
function PCond(w1: number, w2: number) {
  return w1 / (w1 + w2)
}

function spam(words: number[][]) {
  const p_list = words.map((e) => PCond(e[0], e[1]))
  console.log(p_list)


  const a = p_list.reduce((acc, cur) => acc * cur, 1)
  const b = p_list.reduce((acc, cur) => acc * (1 - cur), 1)
  console.log(a,b)

  return a / (a + b)
}

const p = spam(words)
console.log(p)