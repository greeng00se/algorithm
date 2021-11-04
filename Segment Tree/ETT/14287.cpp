#include <bits/stdc++.h>

using namespace std;

#define int long long

const int N = 101010;
vector<int> adj[N];
int s[N], e[N];
int st[4 * N];
int lazy[4 * N];

void dfs(int v, int& num) {
    s[v] = ++num;
    for (int next : adj[v]) {
        dfs(next, num);
    }
    e[v] = num;
}

void update_lazy(int si, int ss, int se) {
	if (lazy[si] != 0) {
		int dx = lazy[si];
		lazy[si] = 0;
		st[si] += dx * (se - ss + 1);
		
		if (ss != se) {
			lazy[2 * si] += dx;
			lazy[2 * si + 1] += dx;
		}
	}
}

int query(int si, int ss, int se, int qs, int qe) {
    update_lazy(si, ss, se);
    if (ss > qe || se < qs) return 0;
    if (ss >= qs && se <= qe) return st[si];
    
    int mid = (ss + se) / 2;
    int l = query(si * 2, ss, mid, qs, qe);
    int r = query(si * 2 + 1, mid + 1, se, qs, qe);
    
    return l + r;
}

void update(int si, int ss, int se, int qs, int qe, int val) {
    update_lazy(si, ss, se);
    if (ss > qe || se < qs) return;
    if (ss >= qs && se <= qe) {
        lazy[si] = val;
        update_lazy(si, ss, se);
		return;
    }
    int mid = (ss + se) / 2;
    update(2 * si, ss, mid, qs, qe, val);
    update(2 * si + 1, mid + 1, se, qs, qe, val);
	
	st[si] = st[si * 2] + st[si * 2 + 1];
}

signed main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q, code, idx, k;
    cin >> n >> q;
    
    for (int i = 1; i <= n; i++) {
		cin >> idx;
		if (idx == -1) continue;
		adj[idx].push_back(i);
	}
	int num = 0;
    dfs(1, num);

    while(q--) {
        cin >> code;
        if (code == 1) {
            cin >> idx >> k;
            update(1, 1, n, s[idx], s[idx], k);
        } else {
            cin >> idx;
            cout << query(1, 1, n, s[idx], e[idx]) << '\n';
        }
    }
    
    return 0;
}