#include <bits/stdc++.h>

#define endl "\n"
#define int long long

using namespace std;

const int mod = 1e9 + 7;
int arr[101010];
int st[4 * 101010];
int lazy[4 * 101010][2];

void buildTree(int si, int ss, int se)
{
    if (ss == se)
    {
        st[si] = arr[ss];
        return;
    }
    
    int mid = (ss + se) / 2;
    
    buildTree(si * 2, ss, mid);
    buildTree(si * 2 + 1, mid + 1, se);
    
    st[si] = (st[si * 2] + st[si * 2 + 1]) % mod;
}

void update_lazy(int si, int ss, int se) {
	int &mul = lazy[si][0];
	int &add = lazy[si][1];
	if (mul == 1 && add == 0) return;
	if (ss != se) {
		for (int i = 0; i < 2; i++) {
			lazy[2 * si + i][0] *= mul;
			lazy[2 * si + i][1] *= mul;
			lazy[2 * si + i][1] += add;
			lazy[2 * si + i][0] %= mod;
			lazy[2 * si + i][1] %= mod;
		}
	}
	st[si] = mul * st[si] + (se - ss + 1) * add;
	st[si] %= mod;
	mul = 1, add = 0;
}

int query(int si, int ss, int se, int qs, int qe)
{
    update_lazy(si, ss, se);
    if (ss > qe || se < qs) return 0;
    if (ss >= qs && se <= qe) return st[si] % mod;
    
    int mid = (ss + se) / 2;
    int l = query(si * 2, ss, mid, qs, qe);
    int r = query(si * 2 + 1, mid + 1, se, qs, qe);
    
    return (l + r) % mod;
}

void update(int si, int ss, int se, int qs, int qe, int mul, int add) {
    update_lazy(si, ss, se);
    if (ss > qe || se < qs) return;
    if (ss >= qs && se <= qe) {
		lazy[si][0] *= mul;
		lazy[si][1] *= mul;
		lazy[si][1] += add;
		lazy[si][0] %= mod;
		lazy[si][1] %= mod;
		update_lazy(si, ss, se);
        return;
    }
    
    int mid = (ss + se) / 2;
    update(2 * si, ss, mid, qs, qe, mul, add);
    update(2 * si + 1, mid + 1, se, qs, qe, mul, add);
	
	st[si] = (st[si * 2] + st[si * 2 + 1]) % mod;
}

signed main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q, code, l, r, k;
    cin >> n;
    
    for (int i = 1; i <= n; i++) 
        cin >> arr[i];
    
	for (int i = 0; i < 404040; i++) 
		lazy[i][0] = 1, lazy[i][1] = 0;
	
    buildTree(1, 1, n);
    
    cin >> q;
    while(q--) {
        cin >> code;
		cin >> l >> r;
        if (code == 4) {
			cout << query(1, 1, n, l, r) << endl;
        } else {
			cin >> k;
			if (code == 1) update(1, 1, n, l, r, 1, k);    
			if (code == 2) update(1, 1, n, l, r, k, 0);
			if (code == 3) update(1, 1, n, l, r, 0, k);
		}
    }
	
    return 0;
}