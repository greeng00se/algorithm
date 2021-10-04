#include <bits/stdc++.h>

#define endl "\n"
#define int long long

using namespace std;

const int MAX = 0x3f3f3f3f;
const int maxN = 100001;
int arr[maxN];
int st[4 * maxN];
int lazy[4 * maxN];

int query(int si, int ss, int se, int qs, int qe)
{
    if (lazy[si] != 0)
    {
        int dx = lazy[si];
        if (dx % 2 != 0)
        {
            st[si] = (se - ss + 1) - st[si];
        }    
        lazy[si] = 0;
        
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

void update(int si, int ss, int se, int qs, int qe)
{
    if (lazy[si] != 0)
    {
        int dx = lazy[si];
        if (dx % 2 != 0)
        {
            st[si] = (se - ss + 1) - st[si];
        }    
        lazy[si] = 0;
        
        if (ss != se)
        {
            lazy[2 * si] += dx;
            lazy[2 * si + 1] += dx;
        }
    }
    
    if (ss > qe || se < qs) return;
    if (ss >= qs && se <= qe)
    {
        int dx = (se - ss + 1);
        st[si] = dx - st[si];
        
        if (ss != se)
        {
            lazy[2 * si] += 1;
            lazy[2 * si + 1] += 1;
        }
        return;
    }
    
    int mid = (ss + se) / 2;
    update(2 * si, ss, mid, qs, qe);
    update(2 * si + 1, mid + 1, se, qs, qe);
    
    st[si] = st[si * 2] + st[si * 2 + 1];
}

signed main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q, code, l, r;
    cin >> n >> q;
    
    while(q--)
    {
        cin >> code >> l >> r;
        if (code)
            cout << query(1, 1, n, l, r) << endl;
        else
            update(1, 1, n, l, r);    
    }
    
    return 0;
}