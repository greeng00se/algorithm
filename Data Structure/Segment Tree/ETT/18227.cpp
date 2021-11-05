#include <bits/stdc++.h>

using namespace std;

#define int long long

const int N = 202020;
vector<int> adj[N];
int s[N], e[N], d[N], visited[N];
int st[4 * N];

void dfs(int v, int& num, int depth) {
    s[v] = ++num;
	d[v] = depth;
	visited[v] = 1;
    for (int next : adj[v]) {
        if (visited[next]) continue;
		dfs(next, num, depth + 1);
    }
    e[v] = num;
}

int query(int si, int ss, int se, int qs, int qe) {
    if (ss > qe || se < qs) return 0;
    if (ss >= qs && se <= qe) return st[si];
    
    int mid = (ss + se) / 2;
    int l = query(si * 2, ss, mid, qs, qe);
    int r = query(si * 2 + 1, mid + 1, se, qs, qe);
    
    return l + r;
}

void update(int si, int ss, int se, int qs, int qe, int val) {
    if (ss > qe || se < qs) return;
	st[si] += val;
	if (ss == se) return;
    
	int mid = (ss + se) / 2;
    update(2 * si, ss, mid, qs, qe, val);
    update(2 * si + 1, mid + 1, se, qs, qe, val);
	
	return;
}

signed main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, c, q, l, r;
    cin >> n >> c;
    
    for (int i = 1; i < n; i++) {
		cin >> l >> r;
		adj[l].push_back(r);
		adj[r].push_back(l);
	}
	int num = 0;
    dfs(c, num, 1);

	cin >> q;
    while(q--) {
        cin >> l >> r;
        if (l == 1) {
            update(1, 1, n, s[r], s[r], 1);
        } else {
            cout << query(1, 1, n, s[r], e[r]) * d[r] << '\n';
        }
    }
    return 0;
}