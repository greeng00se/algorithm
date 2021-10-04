#include <bits/stdc++.h>

#define endl "\n"
#define int long long

using namespace std;

int cnt[10101];
int arr[303030], ans[10101];
int rt;

struct query {
	int l, r, idx;
	bool operator<(const query &o) const {
		int x = r / rt;
		int y = o.r / rt;
		return x == y ? l < o.l : x < y;
	}
} q[10101];

bool cmp(query &a, query &b) {
	if (a.r / rt != b.r / rt) {
		return a.r / rt < b.r / rt;
	}
	return a.l < b.l;
}

void moplus(int idx) {
	cnt[arr[idx]]++;
}

void mominus(int idx) {
	cnt[arr[idx]]--;
}

signed main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, m, c;
	
	cin >> n >> c;
	rt = sqrt(n);
	
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}
	
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> q[i].l >> q[i].r;
		q[i].idx = i;
	}
	
	sort(q, q + m, cmp);
	
	int lo = 1, hi = 0;
	for (int i = 0; i < m; i++) {
		while (q[i].l < lo)
			moplus(--lo);
		while (q[i].l > lo)
			mominus(lo++);
		while (q[i].r < hi)
			mominus(hi--);
		while (q[i].r > hi)
			moplus(++hi);
		
		for (int j = 1; j <= c; j++) {	
			if (cnt[j] > (q[i].r - q[i].l + 1) / 2) {
				ans[q[i].idx] = j;
				break;
			}
		}
	}
	
	for (int i = 0; i < m; i++) {
		if (ans[i])
			cout << "yes " << ans[i] << endl;
		else cout << "no" << endl;	
	}
	return 0;
}