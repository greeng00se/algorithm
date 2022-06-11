#include <bits/stdc++.h>

#define endl "\n"
#define int long long

using namespace std;

int cnt[1010101];
int arr[101010], ans[101010];
int rt, cur;

struct query {
	int l, r, idx;
	bool operator<(const query &o) const {
		int x = r / rt;
		int y = o.r / rt;
		return x == y ? l < o.l : x < y;
	}
} q[101010];

bool cmp(query &a, query &b) {
	if (a.r / rt != b.r / rt) {
		return a.r / rt < b.r / rt;
	}
	return a.l < b.l;
}

void moplus(int idx) {
	if (cnt[arr[idx]]++ == 0)
		cur++;
}

void mominus(int idx) {
	if (--cnt[arr[idx]] == 0)
		cur--;
}

signed main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, m, k;
	
	cin >> n;
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
		ans[q[i].idx] = cur;
	}
	
	for (int i = 0; i < m; i++)
		cout << ans[i] << endl;
	
	return 0;
}