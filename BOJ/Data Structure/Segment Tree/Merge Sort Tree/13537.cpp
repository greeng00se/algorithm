#include <bits/stdc++.h>

#define endl "\n"
#define pb push_back
#define vi vector<int>

using namespace std;

const int maxN = 100001;
int arr[maxN];
vi st[4 * maxN];

void buildTree(int si, int ss, int se) {
    if (ss == se) {
        st[si].pb(arr[ss]);
        return;
    }
    
    int mid = (ss + se) / 2;
    
    buildTree(si * 2, ss, mid);
    buildTree(si * 2 + 1, mid + 1, se);
    
    int i = 0;
    int j = 0;
    
    while (i < st[2 * si].size() && j < st[2 * si + 1].size()) {
        if (st[2 * si][i] <= st[2 * si + 1][j]) {
            st[si].pb(st[2 * si][i]);
            i++;
        } else {
            st[si].pb(st[2 * si + 1][j]);
            j++;
        }
    }
    
    while (i < st[2 * si].size()) {
        st[si].pb(st[2 * si][i]);
        i++;
    }
    while (j < st[2 * si + 1].size()) {
        st[si].pb(st[2 * si + 1][j]);
        j++;
    }
    
    return;
}

int query(int si, int ss, int se, int qs, int qe, int k)
{
    if (ss > qe || se < qs) return 0;
    if (ss >= qs && se <= qe) {
        int res = st[si].end() - upper_bound(st[si].begin(), st[si].end(), k);
        return res;
    }
    
    int mid = (ss + se) / 2;
    int l = query(si * 2, ss, mid, qs, qe, k);
    int r = query(si * 2 + 1, mid + 1, se, qs, qe, k);
    
    return l + r;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q, code, l, r, k;
    cin >> n;
    
    for (int i = 1; i <= n; i++) 
        cin >> arr[i];
    
    buildTree(1, 1, n);
    
    cin >> q;
    while(q--) {
        cin >> l >> r >> k;
        cout << query(1, 1, n, l, r, k) << endl;
    }
    
    return 0;
}