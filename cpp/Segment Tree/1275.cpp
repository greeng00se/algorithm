#include <bits/stdc++.h>

#define int long long
#define endl "\n"

const int maxN = 100001;
int arr[maxN];
int st[4 * maxN];

using namespace std;

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
    
    st[si] = st[si * 2] + st[si * 2 + 1];
}

int query(int si, int ss, int se, int qs, int qe)
{
    if (ss > qe || se < qs) return 0;
    if (ss >= qs && se <= qe) return st[si];
    
    int mid = (ss + se) / 2;
    int l = query(si * 2, ss, mid, qs, qe);
    int r = query(si * 2 + 1, mid + 1, se, qs, qe);
    
    return l + r;
}

void update(int si, int ss, int se, int qi, int newVal)
{
    if (ss == se)
    {
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

signed main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q, l, r, a, b;
    cin >> n >> q;
    
    for (int i = 1; i <= n; i++) 
        cin >> arr[i];
    
    buildTree(1, 1, n);
    
    while(q--)
    {
        cin >> l >> r >> a >> b;
        if (l < r)
            cout << query(1, 1, n, l, r) << endl;
        else    
            cout << query(1, 1, n, r, l) << endl;
        update(1, 1, n, a, b);
    }
    
    return 0;
}