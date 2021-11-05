#include <bits/stdc++.h>

#define endl "\n"
#define int long long

using namespace std;

const int MAX = 0x3f3f3f3f;
const int maxN = 1010101;
int arr[maxN];
int st[4 * maxN];
int lazy[4 * maxN];

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
    if (lazy[si] != 0)
    {
        int dx = lazy[si];
        lazy[si] = 0;
        st[si] += dx * (se - ss + 1);
        
        if (ss != se)
        {
            lazy[2 * si] += dx;
            lazy[2 * si + 1] += dx;
        }
    }
    
    if (ss > qe || se < qs) return 0;
    if (ss >= qs && se <= qe) return st[si];
    
    int mid = (ss + se) / 2;
    int l = query(si * 2, ss, mid, qs, qe);
    int r = query(si * 2 + 1, mid + 1, se, qs, qe);
    
    return l + r;
}

void update(int si, int ss, int se, int qs, int qe, int val)
{
    if (lazy[si] != 0)
    {
        int dx = lazy[si];
        lazy[si] = 0;
        st[si] += dx * (se - ss + 1);
        
        if (ss != se)
        {
            lazy[2 * si] += dx;
            lazy[2 * si + 1] += dx;
        }
    }
    
    if (ss > qe || se < qs) return;
    if (ss >= qs && se <= qe)
    {
        int dx = (se - ss + 1) * val;
        st[si] += dx;
        
        if (ss != se)
        {
            lazy[2 * si] += val;
            lazy[2 * si + 1] += val;
        }
        return;
    }
    
    int mid = (ss + se) / 2;
    update(2 * si, ss, mid, qs, qe, val);
    update(2 * si + 1, mid + 1, se, qs, qe, val);
    
    st[si] = st[si * 2] + st[si * 2 + 1];
}

signed main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q, code, l, r;
    int q1, q2;
    cin >> n >> q1 >> q2;
    q = q1 + q2;
    
    for (int i = 1; i <= n; i++) 
        cin >> arr[i];
    
    buildTree(1, 1, n);
    
    while(q--)
    {
        cin >> code >> l >> r;
        if (code == 1)
        {
            update(1, 1, n, l, l, r);
        }
        else
        {
            cout << query(1, 1, n, l, r) << endl;
        }
    }
    
    return 0;
}