	class Point extends java.awt.Point {
		Point(int x, int y) {
			super(x, y);
		}

		Point(java.awt.Point point) {
			super(point);
		}
	}

	int best = 0; // maximum number of enemies that can are wounded so far

	class AttackPosition extends Point {
		Enemy enemy; // the enemy that can be attacked from this position

		AttackPosition(Point point, Enemy enemy) {
			super(point);
			this.enemy = enemy;
		}
	}

	abstract class Piece extends Point {

		Piece(int y, int x) {
			super(x, y);
		}
	}

	abstract class Attacker extends Piece {
		List<AttackPosition> possiblePositions = new ArrayList<>();
		Set<Point> visited = new HashSet<>();

		Attacker next = null;
		final int attackRange;
		final int movement;

		Attacker(int y, int x, int movement, int attackRange) {
			super(y, x);
			this.attackRange = attackRange;
			this.movement = movement;
		}

		void attack(char[][] grid, int woundedEnemies) {
			for (AttackPosition position : possiblePositions) {
				if (position.enemy != null && position.enemy.wounded)
					continue; // try next since enemy already wounded by another attacker
				if (grid[position.y][position.x] == '-') {
					// do move and attack
					grid[position.y][position.x] = 'X';
					boolean wounded = false;
					if (position.enemy != null) {
						wounded = position.enemy.wounded = true;
						woundedEnemies++;
					}

					if (next != null) {
						// trigger next attacker
						next.attack(grid, woundedEnemies);
					} else {
						if (woundedEnemies > best) {
							best = woundedEnemies;
						}
					}
					// undo attack
					if (wounded) {
						position.enemy.wounded = false;
						woundedEnemies--;
					}
					grid[position.y][position.x] = '-';
				}
			}
		}

		void calculateAttackPositions(Piece[][] piecesGrid, Point pos) {
			boolean found = false;
			Set<Enemy> enemies = new HashSet<>();
			for (int y = Math.max(0, pos.y - attackRange); y <= Math.min(piecesGrid.length - 1,
					pos.y + attackRange); y++) {
				for (int x = Math.max(0, pos.x - attackRange); x <= Math.min(piecesGrid[0].length - 1,
						pos.x + attackRange); x++) {
					if (Math.abs(y - pos.y) + Math.abs(x - pos.x) == attackRange && piecesGrid[y][x] instanceof Enemy) {
						Enemy enemy = (Enemy) piecesGrid[y][x];
						if (enemies.add(enemy)) {
							possiblePositions.add(new AttackPosition(pos, enemy));
						}
						found = true;
					}
				}
			}
			if (!found && (piecesGrid[pos.y][pos.x] == this
					|| piecesGrid[pos.y][pos.x] != null && piecesGrid[pos.y][pos.x].getClass() != getClass())) {
				// if our own position was not already added as an attacking position (see
				// above)
				// then consider it here or
				// if there is an attacker of a different type on that position then consider it
				// as a swap position
				possiblePositions.add(new AttackPosition(pos, null));
			}
		}

		boolean isPossible(Piece[][] grid, Point point) {
			int x = point.x;
			int y = point.y;
			return (y >= 0 && y < grid.length && x >= 0 && x < grid[0].length && !(grid[y][x] instanceof Enemy)
					&& !visited.contains(point));
		}

		void findReachablePieces(Piece[][] grid) {
			// Breadth First Search
			// to find either an enemy or another attacker in movement range
			Queue<Move> queue = new LinkedList<>();
			Move currentMove = new Move(this, movement);
			queue.add(currentMove);
			visited.add(currentMove);
			while (!queue.isEmpty()) {
				currentMove = queue.poll();
				calculateAttackPositions(grid, currentMove);
				if (currentMove.cost > 0) {
					Point[] nextPoints = new Point[] { new Point(currentMove.x, currentMove.y - 1),
							new Point(currentMove.x, currentMove.y + 1), new Point(currentMove.x - 1, currentMove.y),
							new Point(currentMove.x + 1, currentMove.y) };
					for (Point nextPoint : nextPoints) {
						if (isPossible(grid, nextPoint)) {
							queue.add(new Move(nextPoint, currentMove.cost - 1));
							visited.add(nextPoint);
						}
					}
				}
			}
		}
	}

	class Move extends Point {
		int cost;

		Move(Point point, int cost) {
			super(point);
			this.cost = cost;
		}
	}

	class King extends Attacker {
		King(int y, int x) {
			super(y, x, 7, 1);
		}

	}

	class Enemy extends Piece {
		boolean wounded;

		Enemy(int y, int x) {
			super(y, x);
		}
	}

	class Archer extends Attacker {
		Archer(int y, int x) {
			super(y, x, 4, 3);
		}
	}

	int swordsAndArrows(String[] g) {
		char[][] grid = new char[g.length][];
		Piece[][] piecesGrid = new Piece[g.length][];
		int[][] neededByDiffAttackers = new int[g.length][];
		for (int i = 0; i < g.length; i++) {
			grid[i] = g[i].toCharArray();
			piecesGrid[i] = new Piece[g[i].length()];
			neededByDiffAttackers[i] = new int[g[i].length()];
		}

		List<Attacker> attackers = new ArrayList<>();
		List<Enemy> enemies = new ArrayList<>();
		for (int y = 0; y < grid.length; y++) {
			for (int x = 0; x < grid[0].length; x++) {
				switch (grid[y][x]) {
				case 'K':
					King king = new King(y, x);
					attackers.add(king);
					piecesGrid[y][x] = king;
					grid[y][x] = '-';
					break;
				case 'A':
					Archer archer = new Archer(y, x);
					attackers.add(archer);
					piecesGrid[y][x] = archer;
					grid[y][x] = '-';
					break;
				case 'E':
					Enemy enemy = new Enemy(y, x);
					enemies.add(enemy);
					piecesGrid[y][x] = enemy;
					break;
				}
			}
		}

		for (Attacker attacker : attackers) {
			attacker.findReachablePieces(piecesGrid);
		}

		// optimization to reduce the number of possible attacking positions for the
		// same enemy
		// if there are multiple positions and each position is not needed with any
		// other attacker, then just use the first one and skip the others
		for (Attacker attacker : attackers) {
			Set<Point> point = new HashSet<>();
			for (AttackPosition pos : attacker.possiblePositions) {
				if (pos.enemy != null && point.add(new Point(pos.x, pos.y))) {
					neededByDiffAttackers[pos.y][pos.x]++; // how many attackers need a certain position to attack
				}
			}
		}

		for (Attacker attacker : attackers) {
			Map<Enemy, Set<AttackPosition>> attackedFromPos = new HashMap<>();

			for (AttackPosition pos : attacker.possiblePositions) {
				if (pos.enemy != null) {
					Set<AttackPosition> positions = attackedFromPos.computeIfAbsent(pos.enemy, x -> new HashSet<>());
					positions.add(pos);
				}
			}

			// check if all possible positions per enemy are used be the same attacker
			for (Enemy enemy : attackedFromPos.keySet()) {
				Set<AttackPosition> positions = attackedFromPos.get(enemy);
				boolean isOne = true;
				for (AttackPosition position : positions) {
					if (neededByDiffAttackers[position.y][position.x] > 1) {
						isOne = false;
						break;
					}
				}
				if (isOne) {
					// we attack the same enemy from multiple positions
					// and we are the only one that needs those positions
					// consider only one of them and remove the others
					attacker.possiblePositions.removeAll(positions);
					attacker.possiblePositions.add(positions.iterator().next());
				}
			}
		}

		// just chain the attackers so that they can recursively trigger the others
		Attacker last = null;
		for (Attacker attacker : attackers) {
			if (last != null) {
				last.next = attacker;
			}
			last = attacker;
		}
		attackers.iterator().next().attack(grid, 0);
		return best;
	}
