#include <bits/stdc++.h>

#define endl "\n"
#define int long long
#define ff first
#define ss second

using namespace std;

const int N = 101010;
int arr[N];
int st[4 * N];
pair<int, int> lazy[4 * N];

void buildTree(int si, int ss, int se) {
    if (ss == se) {
        st[si] = arr[ss];
        return;
    }
    
    int mid = (ss + se) / 2;
    
    buildTree(si * 2, ss, mid);
    buildTree(si * 2 + 1, mid + 1, se);
    
    st[si] = (st[si * 2] + st[si * 2 + 1]);
}

void update_lazy(int si, int ss, int se) {
	if (lazy[si].ff != 0) {
		int idx = lazy[si].ff;
		int visit = lazy[si].ss;
		lazy[si].ff = 0;
		lazy[si].ss = 0;
		
		st[si] += (visit * (ss + 1)) - idx;
		if (ss != se) {
			lazy[2 * si].ff += idx;
			lazy[2 * si].ss += visit;
			lazy[2 * si + 1].ff += idx;
			lazy[2 * si + 1].ss += visit;
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

void update(int si, int ss, int se, int qs, int qe, int idx) {
    update_lazy(si, ss, se);
    if (ss > qe || se < qs) return;
    if (ss >= qs && se <= qe) {
        lazy[si].ff = idx;
		lazy[si].ss = 1;
        update_lazy(si, ss, se);
		return;
    }
    int mid = (ss + se) / 2;
    update(2 * si, ss, mid, qs, qe, idx);
    update(2 * si + 1, mid + 1, se, qs, qe, idx);
	
	st[si] = st[si * 2] + st[si * 2 + 1];
}

signed main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q, code, l, r, k;
    cin >> n;
    
    for (int i = 1; i <= n; i++) 
        cin >> arr[i];
	
    buildTree(1, 1, n);
    
    cin >> q;
    while(q--) {
        cin >> code;
        if (code == 1) {
			cin >> l >> r;
			update(1, 1, n, l, r, l);
        } else {
			cin >> l;
			cout << query(1, 1, n, l, l) << endl; 
		}
    }
	
    return 0;
}