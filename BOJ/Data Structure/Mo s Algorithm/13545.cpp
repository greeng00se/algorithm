#include <bits/stdc++.h>

using namespace std;

const int rt = 300;
const int sz = 101010 / rt + 10;

struct query {
	int l, r, idx;
	bool operator<(const query &o) const {
		int x = r / rt;
		int y = o.r / rt;
		return x == y ? l < o.l : x < y;
	}
};

int n, k, m;
list<int> pos[202020];
query q[101010];
int arr[101010], ans[101010];
int cnt[101010];
int psum[101010];
int bucket[sz];

void mo_plus(int idx, bool flag) {
	int x = 101010 + psum[idx];
	auto &dq = pos[x];
	int now = 0;
	
	if (dq.size()) {
		now = dq.back() - dq.front();
		cnt[now]--;
		bucket[now/rt]--;
	}
	
	if (flag) dq.push_front(idx);
	else dq.push_back(idx);
	
	now = dq.back() - dq.front();
	cnt[now]++; 
	bucket[now/rt]++;
}

void mo_minus(int idx, bool flag) {
	int x = 101010 + psum[idx];
	auto &dq = pos[x];
	int now = dq.back() - dq.front();
	
	cnt[now]--; 
	bucket[now/rt]--;
	
	if (flag) dq.pop_front();
	else dq.pop_back();
	
	if (dq.size()) {
		now = dq.back() - dq.front();
		cnt[now]++; 
		bucket[now/rt]++;
	}
}

int query() {
	for (int i = sz - 1; i >= 0; i--) {
		if (bucket[i] == 0) continue;
		for (int j = rt - 1; j >= 0; j--) {
			if (cnt[i * rt + j] > 0) {
				return i * rt + j;
			}
		}
	}
	return 0;
}

int main(void) {
	ios::sync_with_stdio(0), cin.tie(0);
	
	cin >> n;
	
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
		psum[i] = psum[i - 1] + arr[i];
	}
	
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> q[i].l >> q[i].r;
		q[i].l = q[i].l - 1;
		q[i].idx = i;
	}
	
	sort(q, q + m);
	
	int lo = q[0].l;
	int hi = q[0].l - 1;
	while (q[0].r > hi) mo_plus(++hi, false);
	ans[q[0].idx] = query();

	for (int i = 1; i < m; i++) {
		while (q[i].l < lo) mo_plus(--lo, true);
		while (q[i].r > hi) mo_plus(++hi, false);
		while (q[i].l > lo) mo_minus(lo++, true);
		while (q[i].r < hi) mo_minus(hi--, false);
		ans[q[i].idx] = query();
	}
	
	for (int i = 0; i < m; i++)
		cout << ans[i] << "\n";
	
	return 0;
}