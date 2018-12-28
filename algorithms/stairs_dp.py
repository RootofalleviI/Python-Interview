private static int getNumberOfWaysToClimbStairs(int n) {
		int a = 1, b = 2, c = 4, d = 0;

		if (n == 0 || n == 1 || n == 2)
			return n;
		if (n == 3)
			return c;

		for (int i = 0; i < n - 3; i++) {
			d = c + b + a;
			a = b;
			b = c;
			c = d;
		}
		return d;
	}
