#include <bits/stdc++.h>

#define endl "\n"
#define int long long
#define ff first
#define ss second

using namespace std;

const int maxN = 100001;
int arr[maxN];
pair<int, int> st[4 * maxN];

void buildTree(int si, int ss, int se)
{
    if (ss == se)
    {
        st[si] = {arr[ss], arr[ss]};
        return;
    }
    
    int mid = (ss + se) / 2;
    
    buildTree(si * 2, ss, mid);
    buildTree(si * 2 + 1, mid + 1, se);
    
    st[si].ff = min(st[2 * si].ff, st[2 * si + 1].ff);
    st[si].ss = max(st[2 * si].ss, st[2 * si + 1].ss);
}

int getMin(int si, int ss, int se, int qs, int qe)
{
    if (ss > qe || se < qs) return 0x3f3f3f3f;
    if (ss >= qs && se <= qe) return st[si].ff;
    
    int mid = (ss + se) / 2;
    int l = getMin(si * 2, ss, mid, qs, qe);
    int r = getMin(si * 2 + 1, mid + 1, se, qs, qe);
    
    return min(l, r);
}

int getMax(int si, int ss, int se, int qs, int qe)
{
    if (ss > qe || se < qs) return 0;
    if (ss >= qs && se <= qe) return st[si].ss;
    
    int mid = (ss + se) / 2;
    int l = getMax(si * 2, ss, mid, qs, qe);
    int r = getMax(si * 2 + 1, mid + 1, se, qs, qe);
    
    return max(l, r);
}

signed main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q, l, r;
    cin >> n >> q;
    
    for (int i = 1; i <= n; i++) 
        cin >> arr[i];
    
    buildTree(1, 1, n);
    
    while(q--)
    {
        cin >> l >> r;
        cout << getMin(1, 1, n, l, r) << " " << getMax(1, 1, n, l, r) << endl;
    }
    
    return 0;
}