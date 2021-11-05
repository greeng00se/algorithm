#include <bits/stdc++.h>

using namespace std;

#define int long long

const int N = 101010;
vector<int> adj[N];
int s[N], e[N];
int st1[4 * N];
int st2[4 * N];
int lazy1[4 * N];
int lazy2[4 * N];

void dfs(int v, int& num) {
    s[v] = ++num;
    for (int next : adj[v]) {
        dfs(next, num);
    }
    e[v] = num;
}

void update_lazy(int si, int ss, int se, int* lazy, int* st) {
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

int query(int si, int ss, int se, int qs, int qe, int* lazy, int* st) {
    update_lazy(si, ss, se, lazy, st);
    if (ss > qe || se < qs) return 0;
    if (ss >= qs && se <= qe) return st[si];
    
    int mid = (ss + se) / 2;
    int l = query(si * 2, ss, mid, qs, qe, lazy, st);
    int r = query(si * 2 + 1, mid + 1, se, qs, qe, lazy, st);
    
    return l + r;
}

void update(int si, int ss, int se, int qs, int qe, int val, int* lazy, int* st) {
    update_lazy(si, ss, se, lazy, st);
    if (ss > qe || se < qs) return;
    if (ss >= qs && se <= qe) {
        lazy[si] = val;
        update_lazy(si, ss, se, lazy, st);
		return;
    }
    int mid = (ss + se) / 2;
    update(2 * si, ss, mid, qs, qe, val, lazy, st);
    update(2 * si + 1, mid + 1, se, qs, qe, val, lazy, st);
	
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
    
    int flag = 1;
    while(q--) {
        cin >> code;
        if (code == 3) {
            flag ^= 1;
        } else if (code == 1) {
            cin >> idx >> k;
            if (flag) {
                update(1, 1, n, s[idx], e[idx], k, lazy1, st1);    
            } else {
                update(1, 1, n, s[idx], s[idx], k, lazy2, st2);    
            }
        } else {
            cin >> idx;
            cout << query(1, 1, n, s[idx], s[idx], lazy1, st1) + query(1, 1, n, s[idx], e[idx], lazy2, st2) << '\n';
        }
    }
    
    return 0;
}