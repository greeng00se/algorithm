#include <bits/stdc++.h>

#define endl "\n"
#define int long long

using namespace std;

const int MAX = 1e7 + 9;
int arr[MAX];
int block[MAX];
int rt;

void update(int idx, int val) {
	block[idx / rt] += val - arr[idx];
	arr[idx] = val;
}

int query(int l, int r) {
	int result = 0;
	
	while (l % rt != 0 && l <= r) {
		result += arr[l++];
	}
	while (r % rt != rt - 1 && l <= r) {
		result += arr[r--];
	}
	while (l <= r) {
		result += block[l / rt];
		l += rt;
	}
	return result;
}

signed main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, m, k;
	
	cin >> n >> m >> k;
	rt = sqrt(n);
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		block[i / rt] += arr[i];
	}
	
	int flag, l, r;
	int q = m + k;
	while(q--) {
		cin >> flag >> l >> r;
		if (flag == 1) {
			l--;
			update(l, r);
		} else {
			l--;
			r--;
			cout << query(l, r) << endl;
		}
	}
	
	return 0;
}