#include <bits/stdc++.h>

using namespace std;

#define int long long
#define endl "\n"

struct query {
	int l, r, k, idx;
	bool operator<(const query &o) const {
		return k == o.k ? l < o.l : k < o.k;
	}
};

const int N = 101010;
int arr[N];
int st[4 * N];
int ans[N];
query q1[101010];
query q2[101010];

void buildTree(int si, int ss, int se) {
    if (ss == se) {
        st[si] = arr[ss];
        return;
    }
    
    int mid = (ss + se) / 2;
    
    buildTree(si * 2, ss, mid);
    buildTree(si * 2 + 1, mid + 1, se);
    
    st[si] = st[si * 2] + st[si * 2 + 1];
}

int query(int si, int ss, int se, int qs, int qe) {
    if (ss > qe || se < qs) return 0;
    if (ss >= qs && se <= qe) return st[si];
    
    int mid = (ss + se) / 2;
    int l = query(si * 2, ss, mid, qs, qe);
    int r = query(si * 2 + 1, mid + 1, se, qs, qe);
    
    return l + r;
}

void update(int si, int ss, int se, int qi, int newVal) {
    if (ss == se) {
        st[si] = newVal;
        return;
    }
    
    int mid = (ss + se) / 2;
    if (qi <= mid)
        update(2 * si, ss, mid, qi, newVal);
    else 
        update(2 * si + 1, mid + 1, se, qi, newVal);
    
    st[si] = st[2 * si] + st[2 * si + 1];
}

signed main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
	
    int n, q, code, l, r;
    cin >> n;
    
    for (int i = 1; i <= n; i++) 
        cin >> arr[i];
    
	buildTree(1, 1, n);
	
	cin >> q;
	int qc1 = 1, qc2 = 1;
	for (int i = 1; i <= q; i++) {
		cin >> code;
		if (code == 1) {
			cin >> q1[qc1].l >> q1[qc1].r;
			qc1++;
		}
    	else {
			cin >> q2[qc2].k >> q2[qc2].l >> q2[qc2].r;
			q2[qc2].idx = qc2;
			qc2++;
		}
	}
	
	sort(q2, q2 + qc2);
	
	qc1 = 1;
	qc2 = 1;
    while(q--)
    {
		if (q2[qc2].k >= qc1 || q2[qc2].idx == 0) {
			update(1, 1, n, q1[qc1].l, q1[qc1].r);
			qc1++;
		} else {
			ans[q2[qc2].idx] = query(1, 1, n, q2[qc2].l, q2[qc2].r);
			qc2++;
		}
    }
	for (int i = 1; i < qc2; i++) {
		cout << ans[i] << endl;
	}
    
    return 0;
}