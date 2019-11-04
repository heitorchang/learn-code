function wordBoggle(board, words) {
  const trie = {};

  for (const word of words) {
    let node = trie;

    for (const letter of word) {
      if (!(letter in node)) node[letter] = {};
      node = node[letter];
    }

    node["$"] = word;
  }

  const wordsFound = new Set();

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      const letter = board[i][j];
      if (letter in trie) seek(i, j, trie[letter]);
    }
  }

  function seek(x, y, node, visited = new Set()) {
    const hash = 5 * x + y;
    visited.add(hash);

    if ("$" in node) wordsFound.add(node["$"]);

    for (let dx = -1; dx <= 1; dx++) {
      for (let dy = -1; dy <= 1; dy++) {
        if ((dx || dy) && x + dx in board && y + dy in board[0]) {
          const nextHash = 5 * (x + dx) + y + dy;
          const letter = board[x + dx][y + dy];

          if (letter in node && !visited.has(nextHash)) {
            seek(x + dx, y + dy, node[letter], visited);
          }
        }
      }
    }
    visited.delete(hash);
  }

  return [...wordsFound].sort();
}
