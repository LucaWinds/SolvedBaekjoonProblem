#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;
typedef long long int ll;

const ll mod = 10007;

int d[1001][1001];

int main() {
	int n, m;
	cin >> n >> m;

	for (int i = 0; i <= n; i++) {
		d[i][0] = d[i][i] = 1;
		for (int j = 1; j <= i - 1; j++) {
			d[i][j] = d[i - 1][j - 1] + d[i - 1][j];
			d[i][j] %= mod;
		}
	}

	int ans = d[n][m];
	cout << ans << '\n';
	return 0;
}