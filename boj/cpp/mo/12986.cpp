#include <bits/stdc++.h>

#define endl "\n"
#define int long long

using namespace std;

int cnt[202020];				// cnt[i] : 수 i가 해당 범위에서 몇 번 등장했는가?
int cnt2[202020]; 				// cnt2[i] : 갯수가 i인 수가 몇 개인가?
int arr[101010], ans[101010];
int rt, maxcnt;

const int p = 100000;

struct query {
	int l, r, idx;
	bool operator<(const query &o) const {
		int x = r / rt;
		int y = o.r / rt;
		return x == y ? l < o.l : x < y;
	}
} q[101010];

void mo_add(int idx) {
	int n = arr[idx];
	cnt2[cnt[n]]--;
	cnt[n]++;
	cnt2[cnt[n]]++;
	maxcnt = max(maxcnt, cnt[n]);
}

void mo_erase(int idx) {
	int n = arr[idx];
	cnt2[cnt[n]]--;
	if (cnt2[cnt[n]] == 0 && maxcnt == cnt[n])
		maxcnt--;
	cnt[n]--;
	cnt2[cnt[n]]++;
}

signed main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, m, k;
	
	cin >> n >> m;
	rt = sqrt(n);
	
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}
	
	for (int i = 0; i < m; i++) {
		cin >> q[i].l >> q[i].r;
		q[i].idx = i;
	}
	
	sort(q, q + m);
	
	int lo = 1, hi = 0;
	for (int i = 0; i < m; i++) {
		while (q[i].l < lo)
			mo_add(--lo);
		while (q[i].l > lo)
			mo_erase(lo++);
		while (q[i].r < hi)
			mo_erase(hi--);
		while (q[i].r > hi)
			mo_add(++hi);
		ans[q[i].idx] = maxcnt;
	}
	
	for (int i = 0; i < m; i++)
		cout << ans[i] << endl;
	
	return 0;
}