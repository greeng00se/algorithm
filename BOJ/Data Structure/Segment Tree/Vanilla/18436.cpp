#include <bits/stdc++.h>

#define endl "\n"
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
        if (arr[ss] % 2 == 1)
            st[si] = {1, 0};
        else
            st[si] = {0, 1};
        return;
    }
    
    int mid = (ss + se) / 2;
    
    buildTree(si * 2, ss, mid);
    buildTree(si * 2 + 1, mid + 1, se);
    
    st[si].ff = st[2 * si].ff + st[2 * si + 1].ff;
    st[si].ss = st[2 * si].ss + st[2 * si + 1].ss;
}

int getEven(int si, int ss, int se, int qs, int qe)
{
    if (ss > qe || se < qs) return 0;
    if (ss >= qs && se <= qe) return st[si].ss;
    
    int mid = (ss + se) / 2;
    int l = getEven(si * 2, ss, mid, qs, qe);
    int r = getEven(si * 2 + 1, mid + 1, se, qs, qe);
    
    return l + r;
}

int getOdd(int si, int ss, int se, int qs, int qe)
{
    if (ss > qe || se < qs) return 0;
    if (ss >= qs && se <= qe) return st[si].ff;
    
    int mid = (ss + se) / 2;
    int l = getOdd(si * 2, ss, mid, qs, qe);
    int r = getOdd(si * 2 + 1, mid + 1, se, qs, qe);
    
    return l + r;
}

void update(int si, int ss, int se, int qi, int newVal)
{
    if (ss == se)
    {
        if (newVal % 2 == 1)
            st[si] = {1, 0};
        else
            st[si] = {0, 1};
        arr[ss] = newVal;
        return;
    }
    
    int mid = (ss + se) / 2;
    if (qi <= mid) 
        update(2 * si, ss, mid, qi, newVal);
    else 
        update(2 * si + 1, mid + 1, se, qi, newVal);
    
    st[si].ff = st[2 * si].ff + st[2 * si + 1].ff;
    st[si].ss = st[2 * si].ss + st[2 * si + 1].ss;
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, q, code, l, r;
    cin >> n;
    
    for (int i = 1; i <= n; i++) 
        cin >> arr[i];
    
    buildTree(1, 1, n);
    
    cin >> q;
    while(q--)
    {
        cin >> code >> l >> r;
        if (code == 1)
            if (arr[l] % 2 == r % 2)
                continue;
            else
                update(1, 1, n, l, r);
        else if (code == 2)
            cout << getEven(1, 1, n, l, r) << endl;
        else
            cout << getOdd(1, 1, n, l, r) << endl;
    }
    
    return 0;
}