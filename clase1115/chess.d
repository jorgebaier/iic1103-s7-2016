enum int N = 8;
int[N][N] board;

struct Position {
	size_t x,y;
	bool legal() {
		return 0<=x&&x<N && 0<=y&&y<N;
	}
}

Position[] delta = [
	Position( 2,  1),
	Position(-1,  1),

	Position(-2,  0),
	Position(-1, -1),

	Position( 0, -2),
	Position( 1, -1),

	Position( 2,  0),
	Position( 1,  1)
];

bool solve(Position p, int n) {
	// Solution was already found!
	if(n>N*N)
		return true;

	if(!p.legal()) {
		writeln(p);
		return false;
	}

	if(board[p.y][p.x]!=0)
		return false;

	// Try
	auto y = p.y;  // Save position (y:-2 x:+1 at the end is ugly)
	auto x = p.x;
	board[y][x]=n;

	foreach(d; delta) {
		p.y += d.y;
		p.x += d.x;
		if(p.legal() && solve(p, n+1))
			return true;
	}
	// Attempt failed, restore
	board[y][x]=0;
	return false;
}

void printBoard(int[N][N] b=board) {
	writeln("Board:");
	for(int y=N-1; y>=0; y--) {
		for(int x=0; x<N; x++)
			writef("%2d ", b[y][x]);
		writeln();
	}
	writeln();
}

import std.stdio;
void main() {
	if(solve(Position(0,0), 1))
		printBoard();
	else
		writeln("No solution found");
}
